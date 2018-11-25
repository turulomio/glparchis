from setuptools import setup, Command
import os
import platform
import site
import shutil
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
        os.system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
        os.system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
        os.chdir("doc")
        os.system("doxygen Doxyfile")
        os.system("rsync -avzP -e 'ssh -l turulomio' html/ frs.sourceforge.net:/home/users/t/tu/turulomio/userweb/htdocs/doxygen/glparchis/ --delete-after")
        os.chdir("..")

class Compile(Command):
    description = "Compile ui and images"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        futures=[]
        with ProcessPoolExecutor(max_workers=cpu_count()+1) as executor:
            for filename in os.listdir("glparchis/ui/"):
                if filename.endswith(".ui"):
                    without_extension=filename[:-3]
                    futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/{0}.ui -o glparchis/ui/Ui_{0}.py".format(without_extension)))
            futures.append(executor.submit(os.system, "pyrcc5 glparchis/images/glparchis.qrc -o glparchis/images/glparchis_rc.py"))
        # Overwriting glparchis_rc
        for filename in os.listdir("glparchis/ui/"):
             if filename.startswith("Ui_"):
                 os.system("sed -i -e 's/glparchis_rc/glparchis.images.glparchis_rc/' glparchis/ui/{}".format(filename))
                 os.system("sed -i -e 's/from myQGLWidget/from glparchis.ui.myQGLWidget/' glparchis/ui/{}".format(filename))
                 os.system("sed -i -e 's/from qtablestatistics/from glparchis.ui.qtablestatistics/' glparchis/ui/{}".format(filename))


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
  * git commit -a -m 'glparchis-{}'
  * git push
  * Hacer un nuevo tag en GitHub
  * python setup.py sdist upload -r pypi
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
        if platform.system()=="Linux":
            os.system("rm -Rf {}/glparchis*".format(site.getsitepackages()[0]))
            os.system("rm /usr/bin/glparchis")
            os.system("rm /usr/share/pixmaps/glparchis.png")
            os.system("rm /usr/share/applications/glparchis.desktop")
        else:
            print(site.getsitepackages())
            for file in os.listdir(site.getsitepackages()[1]):#site packages
               path=site.getsitepackages()[1]+"\\"+ file
               if file.find("glparchis")!=-1:
                   shutil.rmtree(path)
                   print(path,  "Erased")
            for file in os.listdir(site.getsitepackages()[0]+"\\Scripts\\"):#Scripts
               path=site.getsitepackages()[0]+"\\scripts\\"+ file
               if file.find("glparchis")!=-1:
                   os.remove(path)
                   print(path,  "Erased")

class Doc(Command):
    description = "Update man pages and translations"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("pylupdate5 -noobsolete -verbose glparchis.pro")
        os.system("lrelease -qt5 glparchis.pro")

class PyInstaller(Command):
    description = "pyinstaller file generator"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        shutil.rmtree("build")
        os.system("""pyinstaller glparchis/glparchis.py -n glparchis-{}  --onefile   --windowed --icon glparchis/images/glparchis.ico""".format(__version__))


    ########################################################################

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

## Version of officegenerator captured from commons to avoid problems with package dependencies
__version__= None
with open('glparchis/version.py', encoding='utf-8') as f:
    for line in f.readlines():
        if line.find("__version__ =")!=-1:
            __version__=line.split("'")[1]

if platform.system()=="Linux":
    data_files=[
                 ('/usr/share/applications/', ['glparchis.desktop']),
                 ('/usr/share/pixmaps/', ['glparchis/images/glparchis.png']),
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
    url='https://glparchis.sourceforge.io/',
    author='Turulomio',
    author_email='turulomio@yahoo.es',
    license='GPL-3',
    packages=['glparchis'],
    entry_points = entry_points,
    install_requires=['setuptools',
                      'pyopengl',
                      'PyQt5;platform_system=="Windows"',
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

