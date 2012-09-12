#!/bin/bash
####### COPIA FILES
VERSION=`cat libglparchis.py | grep 'version="2'| cut --delimiter='"'  -f 2`
DIR=glparchis-$VERSION
FILE=$DIR.zip
echo "Este script crea el fichero $FILE para ser subido a sourceforge"
echo "Debe tener instalado una versión de wine y sobre el haber instalado"
#echo "  - Python 2.xx"
#echo "  - PyQt4 (ultima version)"
#echo "  - pyopengl (ultima version)"
echo "  - Inno Setup (ultima version)"

mkdir $DIR
mkdir $DIR/doc
mkdir $DIR/i18n
mkdir $DIR/images
mkdir $DIR/ui
mkdir $DIR/saves
mkdir $DIR/sounds

cp      Makefile \
	AUTHORS-ES.txt \
	AUTHORS-EN.txt \
        CHANGELOG-EN.txt \
        CHANGELOG-ES.txt \
        GPL-3.txt \
        INSTALL-EN.txt \
        INSTALL-ES.txt \
        RELEASES-EN.txt \
        RELEASES-ES.txt \
        glparchis.py \
        glparchis.pro \
        libglparchis.py \
        glparchis.desktop \
        $DIR

cp      i18n/*.ts \
        $DIR/i18n

cp 	doc/*.odt \
	doc/*.odg \
        $DIR/doc

cp 	ui/frm* \
	ui/wdg* \
	ui/q* \
	$DIR/ui

cp	images/*.png \
	images/*.qrc \
	images/*.ico \
	$DIR/images

cp 	sounds/*.ogg \
	$DIR/sounds

cp 	saves/*.glparchis \
	$DIR/saves



###### sources linux. Ui se ha compilado antes
tar cvz  -f dist/glparchis-src-$VERSION.tar.gz $DIR/ -C $DIR > /dev/null
chmod 666 dist/glparchis-src-$VERSION.tar.gz

######## COMPILA
DESTDIR=$DIR/dist
PREFIXBIN=$DESTDIR/bin
PREFIXLIB=$DESTDIR/lib/glparchis
PREFIXSHARE=$DESTDIR/share/glparchis 
PREFIXSOUND=$DESTDIR/share/glparchis/sounds
mkdir -p  $DESTDIR
mkdir -p  $PREFIXBIN
mkdir -p  $PREFIXLIB
mkdir -p  $PREFIXSHARE
mkdir -p  $PREFIXSOUND

#pyuic4 $DIR/ui/frmAbout.ui > $PREFIXLIB/Ui_frmAbout.py
#pyuic4 $DIR/ui/frmInitGame.ui > $PREFIXLIB/Ui_frmInitGame.py
#pyuic4 $DIR/ui/frmMain.ui > $PREFIXLIB/Ui_frmMain.py
#pyuic4 $DIR/ui/frmSettings.ui > $PREFIXLIB/Ui_frmSettings.py
#pyuic4 $DIR/ui/frmShowCasilla.ui > $PREFIXLIB/Ui_frmShowCasilla.py
#pyuic4 $DIR/ui/frmShowFicha.ui > $PREFIXLIB/Ui_frmShowFicha.py
#pyuic4 $DIR/ui/wdgUserPanel.ui > $PREFIXLIB/Ui_wdgUserPanel.py
#pyuic4 $DIR/ui/wdgGame.ui > $PREFIXLIB/Ui_wdgGame.py
#pyrcc4 $DIR/images/glparchis.qrc > $PREFIXLIB/glparchis_rc.py
#cd $DIR
#pylupdate4 -noobsolete glparchis.pro
#lrelease glparchis.pro
#cd ..

install $DIR/glparchis.py $PREFIXBIN/glparchis
install $DIR/glparchis.bat $DESTDIR
install $DIR/libglparchis.py $PREFIXLIB
install $DIR/ui/*.py $PREFIXLIB
install $DIR/i18n/*.qm $PREFIXSHARE
install $DIR/doc/glparchis-* $PREFIXSHARE
install $DIR/AUTHORS-EN.txt  AUTHORS-ES.txt  CHANGELOG-EN.txt  CHANGELOG-ES.txt  GPL-3.txt  INSTALL-EN.txt  INSTALL-ES.txt  RELEASES-EN.txt  RELEASES-ES.txt  $PREFIXSHARE
install $DIR/sounds/*.ogg $PREFIXSOUND
install $DIR/images/*.py $PREFIXLIB
install $DIR/images/*.ico $PREFIXSHARE


####### binaries linux
mv $PREFIXBIN/glparchis $PREFIXBIN/glparchis.py
python pyinstaller-2.0/pyinstaller.py -o $DIR/pyinstallerlinux -i $DIR/dist/share/glparchis/ficharoja.ico -w -p $DIR/dist/lib/glparchis $DIR/dist/bin/glparchis.py
cd $DIR/pyinstallerlinux/dist/
tar cvz  -f ../../../dist/glparchis-linux-$VERSION.tar.gz *
cd ../../../
###### binaries windows
echo "
@echo off
cd bin
c:/Python27/python.exe glparchis.py" > $DESTDIR/glparchis.bat
sed -i -e 's:WindowsVersion=False:WindowsVersion=True:' $PREFIXLIB/libglparchis.py

wine $HOME/.wine/drive_c/Python27/python.exe  pyinstaller-2.0/pyinstaller.py -o $DIR/pyinstallerwindows -i $DIR/dist/share/glparchis/ficharoja.ico -w -p $DIR/dist/lib/glparchis $DIR/dist/bin/glparchis.py
sed -i -e "s:XXXXXXXX:$VERSION:" glparchis.iss
wine $HOME/.wine/drive_c/Program\ Files\ \(x86\)/Inno\ Setup\ 5/ISCC.exe /odist glparchis.iss
sed -i -e "s:$VERSION:XXXXXXXX:" glparchis.iss #Deja en X la versión

##### limpia directorio
rm -R $DIR
