from setuptools import setup, Command

import gettext
import logging
import os
import platform
import site
import sys
from PyQt5.QtCore import QCoreApplication,  QTranslator
from colorama import Style, Fore
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

def change_language(language):  
    """language es un string"""
    url= "glparchis/qm/glparchis_{}.qm".format(language)
    if os.path.exists(url)==True:
        translator.load(url)
        QCoreApplication.installTranslator(translator)
        logging.info(("Language changed to {} using {}".format(language, url)))
        return
    if language!="en":
        logging.warning(Style.BRIGHT+ Fore.CYAN+ app.tr("Language ({}) couldn't be loaded in {}. Using default (en).".format(language, url)))

class Doxygen(Command):
    description = "Create/update doxygen documentation in doc/html"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Creating Doxygen Documentation")
#        os.system("""sed -i -e "41d" doc/Doxyfile""")#Delete line 41
#        os.system("""sed -i -e "41iPROJECT_NUMBER         = {}" doc/Doxyfile""".format(__version__))#Insert line 41
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
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmAbout.ui -o glparchis/ui/Ui_frmAbout.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmHelp.ui -o glparchis/ui/Ui_frmHelp.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmMain.ui -o glparchis/ui/Ui_frmMain.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmSettings.ui -o glparchis/ui/Ui_frmSettings.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmGameStatistics.ui -o glparchis/ui/Ui_frmGameStatistics.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmInitGame.ui -o glparchis/ui/Ui_frmInitGame.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmShowCasilla.ui -o glparchis/ui/Ui_frmShowCasilla.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/frmShowFicha.ui -o glparchis/ui/Ui_frmShowFicha.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/wdgGame.ui -o glparchis/ui/Ui_wdgGame.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/wdgPlayer.ui -o glparchis/ui/Ui_wdgPlayer.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/wdgPlayerDado.ui -o glparchis/ui/Ui_wdgPlayerDado.py"))
            futures.append(executor.submit(os.system, "pyuic5 glparchis/ui/wdgUserPanel.ui -o glparchis/ui/Ui_wdgUserPanel.py"))
            futures.append(executor.submit(os.system, "pyrcc5 images/glparchis.qrc -o glparchis/ui/glparchis_rc.py"))
        # Overwriting glparchis_rc
        for file in ['glparchis/ui/Ui_frmAbout.py', 'glparchis/ui/Ui_frmHelp.py', 'glparchis/ui/Ui_frmMain.py', 'glparchis/ui/Ui_frmSettings.py', 
                     'glparchis/ui/Ui_frmGameStatistics.py', 'glparchis/ui/Ui_frmInitGame.py', 'glparchis/ui/Ui_frmShowFicha.py', 'glparchis/ui/Ui_frmShowCasilla.py',
                     'glparchis/ui/Ui_wdgGame.py', 'glparchis/ui/Ui_wdgPlayer.py', 'glparchis/ui/Ui_wdgPlayerDado.py', 'glparchis/ui/Ui_wdgUserPanel.py']:
            os.system("sed -i -e 's/glparchis_rc/glparchis.ui.glparchis_rc/' {}".format(file))
        # Overwriting myQGLWidget
        os.system("sed -i -e 's/from myQGLWidget/from glparchis.ui.myQGLWidget/' glparchis/ui/Ui_wdgGame.py")
        os.system("sed -i -e 's/from myQGLWidget/from glparchis.ui.myQGLWidget/' glparchis/ui/Ui_frmAbout.py")
        # Overwriting qtablestatistics
        os.system("sed -i -e 's/from qtablestatistics/from glparchis.ui.qtablestatistics/' glparchis/ui/Ui_wdgGame.py")


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
#            os.system("rm " + prefixbin + "/glparchis*")
#        shell("rm -Rf " + prefixlib)
#        shell("rm -Rf " + prefixshare)
#        shell("rm -fr " + prefixpixmaps + "/glparchis.png")
#        shell("rm -fr " + prefixapplications +"/glparchis.desktop")

        else:
            print(_("Uninstall command only works in Linux"))

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
    ########################################################################

app=QCoreApplication(sys.argv)

app.setOrganizationName("glparchis")
app.setOrganizationDomain("glparchis.sourceforge.net")
app.setApplicationName("glparchis")
translator=QTranslator()
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

if platform.system()=="Linux":
    data_files=[]
    #('/usr/share/man/man1/', ['man/man1/glparchis.1']), 
    #            ('/usr/share/man/es/man1/', ['man/es/man1/glparchis.1'])
    #           ]
else:
    data_files=[]

## Version of officegenerator captured from commons to avoid problems with package dependencies
__version__= None
with open('glparchis/version.py', encoding='utf-8') as f:
    for line in f.readlines():
        if line.find("__version__ =")!=-1:
            __version__=line.split("'")[1]

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
    entry_points = {'console_scripts': [    'glparchis=glparchis.glparchis:main',
                                    ],
                },
    install_requires=['PyQt5', 'pyopengl','setuptools'],
    data_files=data_files,
    cmdclass={
                        'doxygen': Doxygen,
                        'doc': Doc,
                        'uninstall':Uninstall, 
                        'compile': Compile, 
                     },
    zip_safe=False,
    include_package_data=True
    )

_=gettext.gettext#To avoid warnings
