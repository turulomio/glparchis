#!/bin/bash

####### COPIA FILES
VERSION=`cat libglparchis.py | grep 'version="2'| cut --delimiter='"'  -f 2`
DIR=glparchis-$VERSION
FILE=$DIR.zip
echo "Este script crea el fichero $FILE para ser subido a sourceforge"
echo "Debe tener instalado una versión de wine y sobre el haber instalado"
echo "  - Python 2.xx"
echo "  - PyQt4 (ultima version)"
echo "  - pyopengl (ultima version)"
echo "  - pywin32 (ultima version)"
echo "  - Inno Setup (ultima version)"

#Genera los Ui_ y resto
make compile

#Copia los fuentes
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
echo "  * Comprimiendo codigo fuente..."
tar cvz  -f dist/glparchis-src-$VERSION.tar.gz $DIR/ -C $DIR > /dev/null
chmod 666 dist/glparchis-src-$VERSION.tar.gz

######## INSTALA
DESTDIR=$DIR/dist
DESTDIR=$DESTDIR make all

###### install pyinstaller
cd $DIR
wget https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-2.0.tar.bz2
tar xjf pyinstaller-2.0.tar.bz2
cd ..


####### binaries linux
mv $DESTDIR/bin/glparchis $DESTDIR/bin/glparchis.py
python $DIR/pyinstaller-2.0/pyinstaller.py -o $DIR/pyinstallerlinux -i $DESTDIR/share/glparchis/ficharoja.ico -w -p $DESTDIR/lib/glparchis $DESTDIR/bin/glparchis.py
cd $DIR/pyinstallerlinux/dist/
echo "Execute glparchis and play" > README.txt
echo "  * Comprimiendo binario linux..."
tar cvz  -f ../../../dist/glparchis-linux-$VERSION.tar.gz * > /dev/null
cd ../../../
###### binaries windows
echo "
@echo off
cd bin
c:/Python27/python.exe glparchis.py" > $DESTDIR/glparchis.bat

sed -i -e 's:WindowsVersion=False:WindowsVersion=True:' $DESTDIR/lib/glparchis/libglparchis.py
sed -i -e 's:WindowsVersion=False:WindowsVersion=True:' $DESTDIR/bin/glparchis.py
wine $HOME/.wine/drive_c/Python27/python.exe  $DIR/pyinstaller-2.0/pyinstaller.py -o $DIR/pyinstallerwindows -i $DESTDIR/share/glparchis/ficharoja.ico -w -p $DESTDIR/lib/glparchis $DESTDIR/bin/glparchis.py
sed -i -e "s:XXXXXXXX:$VERSION:" glparchis.iss
wine $HOME/.wine/drive_c/Program\ Files\ \(x86\)/Inno\ Setup\ 5/ISCC.exe /odist glparchis.iss
sed -i -e "s:$VERSION:XXXXXXXX:" glparchis.iss #Deja en X la versión

##### limpia directorio
rm -R $DIR
