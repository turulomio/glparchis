from os import system, chdir, listdir, remove
from glparchis.version import __version__


def compile():
        import datetime
        for filename in listdir("glparchis/ui/"):
            if filename.endswith(".ui"):
                without_extension=filename[:-3]
                system("pyuic6 glparchis/ui/{0}.ui -o glparchis/ui/Ui_{0}.py".format(without_extension))
        
        # pyrcc6 does not exist in PyQt6. Use rcc from system (e.g. sudo apt install qt6-base-dev-tools)
        # system("rcc -g python glparchis/images/glparchis.qrc -o glparchis/images/glparchis_rc.py")
        system("/usr/lib64/qt6/libexec/rcc -g python glparchis/images/glparchis.qrc | sed '0,/PySide6/s//PyQt6/' > glparchis/images/glparchis_rc.py")
        # Overwriting glparchis_rc
        for filename in listdir("glparchis/ui/"):
             if filename.startswith("Ui_"):
                 system("sed -i -e 's/glparchis_rc/glparchis.images.glparchis_rc/' glparchis/ui/{}".format(filename))
                 system("sed -i -e 's/from myQGLWidget/from glparchis.ui.myQGLWidget/' glparchis/ui/{}".format(filename))
                 system("sed -i -e 's/from qtablestatistics/from glparchis.ui.qtablestatistics/' glparchis/ui/{}".format(filename))
        #print ("Copying libmanagers.py from Xulpymoney project")
        #chdir("glparchis")
        #remove("libmanagers.py")
        #system("wget https://raw.githubusercontent.com/Turulomio/xulpymoney/master/xulpymoney/libmanagers.py  --no-clobber")
        #system("sed -i -e '3i ## THIS FILE HAS BEEN DOWNLOADED AT {} FROM https://github.com/Turulomio/xulpymoney/xulpymoney/libmanagers.py.' libmanagers.py".format(datetime.datetime.now()))

        # pylupdate6 requires explicit --ts and source files. It doesn't parse .pro files.
        # for lang in ["en", "es", "fr", "ro", "ru"]:
            #system("/usr/lib64/qt6/bin/lupdate -no-obsolete -verbose -ts glparchis/i18n/glparchis_{}.ts glparchis/*.py glparchis/ui/*.py".format(lang))
        system("/usr/lib64/qt6/bin/lupdate glparchis.pro")
        
        # Ensure qt6-linguist tools are installed (e.g. sudo apt install qt6-linguist-utils). Command might be lrelease or lrelease-qt6
        system("/usr/lib64/qt6/bin/lrelease glparchis.pro")

def relase():
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
