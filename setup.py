from setuptools import setup, Command
from os import system, chdir, listdir, remove, mkdir
from platform import system as platform_system
from site import getsitepackages
from shutil import rmtree
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

## Class to define doxygen command
class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"

    user_options = [
      # The format is (long option, short option, description).
      ( 'user=', None, 'Remote ssh user'),
      ( 'directory=', None, 'Remote ssh path'),
      ( 'port=', None, 'Remote ssh port'),
      ( 'server=', None, 'Remote ssh server'),
  ]

    def initialize_options(self):
        self.user="root"
        self.directory="/var/www/html/doxygen/glparchis/"
        self.port=22
        self.server="127.0.0.1"

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
        system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
        system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
        system("rm -Rf build")
        chdir("doc")
        system("doxygen Doxyfile")      
        command=f"""rsync -avzP -e 'ssh -l {self.user} -p {self.port} ' html/ {self.server}:{self.directory} --delete-after"""
        print(command)
        system(command)
        chdir("..")


class Compile(Command):
    description = "Compile ui and images"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import datetime
        futures=[]
        with ProcessPoolExecutor(max_workers=cpu_count()+1) as executor:
            for filename in listdir("glparchis/ui/"):
                if filename.endswith(".ui"):
                    without_extension=filename[:-3]
                    futures.append(executor.submit(system, "pyuic5 glparchis/ui/{0}.ui -o glparchis/ui/Ui_{0}.py".format(without_extension)))
            futures.append(executor.submit(system, "pyrcc5 glparchis/images/glparchis.qrc -o glparchis/images/glparchis_rc.py"))
        # Overwriting glparchis_rc
        for filename in listdir("glparchis/ui/"):
             if filename.startswith("Ui_"):
                 system("sed -i -e 's/glparchis_rc/glparchis.images.glparchis_rc/' glparchis/ui/{}".format(filename))
                 system("sed -i -e 's/from myQGLWidget/from glparchis.ui.myQGLWidget/' glparchis/ui/{}".format(filename))
                 system("sed -i -e 's/from qtablestatistics/from glparchis.ui.qtablestatistics/' glparchis/ui/{}".format(filename))
        print ("Copying libmanagers.py from Xulpymoney project")
        chdir("glparchis")
        remove("libmanagers.py")
        system("wget https://raw.githubusercontent.com/Turulomio/xulpymoney/master/xulpymoney/libmanagers.py  --no-clobber")
        system("sed -i -e '3i ## THIS FILE HAS BEEN DOWNLOADED AT {} FROM https://github.com/Turulomio/xulpymoney/xulpymoney/libmanagers.py.' libmanagers.py".format(datetime.datetime.now()))


class Procedure(Command):
    description = "Uninstall installed files with install"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("""
Nueva versión:
  * Cambiar la versión y la fecha en version.py
  * Modificar el Changelog en README
  * python setup.py doc
  * linguist
  * python setup.py doc
  * python setup.py install
  * python setup.py doxygen
  * git commit -a -m 'glparchis-{0}'
  * git push
  * Hacer un nuevo tag en GitHub
  * python setup.py sdist
  * twine upload dist/glparchis-{0}.tar.gz 
  * Pasa a Windows y ejecuta setup.py pyinstaller
  * Crea un nuevo ebuild de Gentoo con la nueva versión
  * Subelo al repositorio del portage
""".format(__version__))


class Uninstall(Command):
    description = "Uninstall installed files with install"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        if platform_system()=="Linux":
            system("rm -Rf {}/glparchis*".format(getsitepackages()[0]))
            system("rm /usr/bin/glparchis")
            system("rm /usr/share/pixmaps/glparchis.png")
            system("rm /usr/share/applications/glparchis.desktop")
        else:
            print(getsitepackages())
            for file in listdir(getsitepackages()[1]):#site packages
               path=getsitepackages()[1]+"\\"+ file
               if file.find("glparchis")!=-1:
                   rmtree(path)
                   print(path,  "Erased")
            for file in listdir(getsitepackages()[0]+"\\Scripts\\"):#Scripts
               path=getsitepackages()[0]+"\\scripts\\"+ file
               if file.find("glparchis")!=-1:
                   remove(path)
                   print(path,  "Erased")

class Doc(Command):
    description = "Update man pages and translations"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        system("pylupdate5 -noobsolete -verbose glparchis.pro")
        system("lrelease -qt5 glparchis.pro")

class PyInstaller(Command):
    description = "pyinstaller file generator"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        rmtree("build")
        mkdir("build")
        system("python setup.py uninstall")
        system("python setup.py install")
        f=open("build/run.py","w")
        f.write("import glparchis.glparchis\n")
        f.write("glparchis.glparchis.main()\n")
        f.close()
        chdir("build")
        system("pyinstaller run.py -n glparchis-{} --onefile --windowed --icon ../glparchis/images/glparchis.ico --distpath ../dist".format(__version__))


    ########################################################################

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

## Version of officegenerator captured from commons to avoid problems with package dependencies
__version__= None
with open('glparchis/version.py', encoding='utf-8') as f:
    for line in f.readlines():
        if line.find("__version__ =")!=-1:
            __version__=line.split("'")[1]

if platform_system()=="Linux":
    data_files=[
#                 ('/usr/share/applications/', ['glparchis.desktop']),
#                 ('/usr/share/pixmaps/', ['glparchis/images/glparchis.png']),
               ]
    entry_points={'gui_scripts': ['glparchis=glparchis.glparchis:main', ]}
else:
    data_files=[]
    entry_points={'gui_scripts': ['glparchis=glparchis.glparchis:main', ], 'console_scripts' : [ 'glparchis_shortcuts=glparchis.shortcuts:create', ]}


setup(name='glparchis',
    version=__version__,
    description='Parchís game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'Topic :: Software Development :: Build Tools',
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Programming Language :: Python :: 3',
             ], 
    keywords='parchís game',
    url='https://github.com/turulomio/glparchis',
    author='turulomio',
    author_email='turulomio@yahoo.es',
    license='GPL-3',
    packages=['glparchis'],
    entry_points = entry_points,
    install_requires=['setuptools',
                      'pyopengl',
                      'colorama', 
                      'PyQt5', 
                      'PyQtWebEngine', 
                      'pywin32;platform_system=="Windows"',
                     ],
    data_files=data_files,
    cmdclass={
                        'doxygen': Doxygen,
                        'doc': Doc,
                        'uninstall':Uninstall, 
                        'compile': Compile, 
                        'pyinstaller': PyInstaller,
                        'procedure': Procedure,
                     },
    zip_safe=False,
    include_package_data=True
    )

