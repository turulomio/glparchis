#!/bin/bash

####### COPIA FILES
VERSION=`cat libglparchis.py | grep 'version="2'| cut --delimiter='"'  -f 2`
TIME=`date +%Y%m%d%H%M%S`
CWD=`pwd`
DIR=/tmp/glparchis-$VERSION-$TIME
DIRSRCLINUX=$DIR/src.linux/glparchis-$VERSION/ # Se instala con un makefile
DIRSRCWINDOWS=$DIR/src.windows/glparchis-$VERSION/ # Se necesita la instalción de pyqt, python, opengl, se ejecuta con bat. Habra un bat para compilar con pyinstaller y generar con innosetup el exe
DIRBINLINUX=$DIR/bin.linux/glparchis-$VERSION # Es un directorio con el ejecutable
DIRBINWINDOWS=$DIR/bin.windows #Es un instalador windows, generado con wine, para generarlo con windows en srcwindows habrá un bat
mkdir -p $DIRSRCLINUX
mkdir -p $DIRSRCWINDOWS
mkdir -p $DIRBINLINUX
mkdir -p $DIRBINWINDOWS

echo "Este script crea el fichero $FILE para ser subido a sourceforge"
echo "Debe tener instalado una versión de wine y sobre el haber instalado"
echo "  - Python 2.xx"
echo "  - PyQt4 (ultima version)"
echo "  - pyopengl (ultima version)"
echo "  - pywin32 (ultima version)"
echo "  - Inno Setup (ultima version)"

rm $CWD/dist/*

#GENERA SRC LINUX
make compile
mkdir $DIRSRCLINUX/doc
mkdir $DIRSRCLINUX/i18n
mkdir $DIRSRCLINUX/images
mkdir $DIRSRCLINUX/ui
mkdir $DIRSRCLINUX/saves
mkdir $DIRSRCLINUX/sounds

cp      Makefile \
	AUTHORS-ES.txt \
	AUTHORS-EN.txt \
        CHANGELOG-EN.txt \
        CHANGELOG-ES.txt \
        GPL-3.txt \
        INSTALL-EN.txt \
        INSTALL-ES.txt \
        RELEASES.txt \
        glparchis.py \
        glparchis.pro \
        libglparchis.py \
        glparchis.desktop \
        $DIRSRCLINUX

cp      i18n/*.ts \
        $DIRSRCLINUX/i18n

cp 	ui/frm* \
	ui/wdg* \
	ui/q* \
	$DIRSRCLINUX/ui

cp	images/*.png \
	images/*.qrc \
	images/*.ico \
	$DIRSRCLINUX/images

cp 	sounds/* \
	$DIRSRCLINUX/sounds

cp 	saves/*.glparchis \
	$DIRSRCLINUX/saves

echo "  * Comprimiendo codigo fuente linux..."
cd $DIR/src.linux
tar cvz  -f $CWD/dist/glparchis-src-linux-$VERSION.tar.gz * -C $DIR/src.linux > /dev/null
cd $CWD

######## 
DESTDIR=$DIRSRCWINDOWS make all
mv $DIRSRCWINDOWS/bin/glparchis $DIRSRCWINDOWS/bin/glparchis.py
#sed -i -e 's:so="src.linux":so="src.windows":' $DIRSRCWINDOWS/lib/glparchis/libglparchis.py
sed -i -e 's:so="src.linux":so="src.windows":' $DIRSRCWINDOWS/bin/glparchis.py
#cp $DIRSRCWINDOWS/lib/glparchis/libglparchis.py $DIRSRCWINDOWS/lib/glparchis/libglparchis.py.src
cp $DIRSRCWINDOWS/bin/glparchis.py $DIRSRCWINDOWS/bin/glparchis.py.src

#cp $DIRSRCWINDOWS/lib/glparchis/libglparchis.py $DIRSRCWINDOWS/lib/glparchis/libglparchis.py.bin
cp $DIRSRCWINDOWS/bin/glparchis.py $DIRSRCWINDOWS/bin/glparchis.py.bin
#sed -i -e 's:so="src.windows":so="bin.windows":' $DIRSRCWINDOWS/lib/glparchis/libglparchis.py.bin
sed -i -e 's:so="src.windows":so="bin.windows":' $DIRSRCWINDOWS/bin/glparchis.py.bin

echo "
@echo off
copy /Y bin\\glparchis.py.src bin\\glparchis.py

cd bin
c:/Python27/python.exe glparchis.py
pause" > $DIRSRCWINDOWS/glparchis.bat
echo "
rem Solo con x86 no hay opengl 64
rem Instalar pyinstaller directorio en c:\ solo una vez
rem Se necesita pywin32 para pyinstaller 
rem Meter glparchis.ico
rem Cambiar ruta de pyinstaller 

cd ..
cd ..
copy /Y bin\\glparchis.py.bin bin\\glparchis.py
cd share/glparchis
rm glparchis.spec
rm logdict2.7.3.final.0-1.log
rmdir /s /q build
rmdir /s /q dist
c:\Python27\python.exe c:\pyinstaller\pyinstaller.py -i ficharoja.ico -w -p ..\..\lib\glparchis ..\..\bin\glparchis.py
copy /Y sounds\\*.wav dist\\glparchis\\
pause" > $DIRSRCWINDOWS/share/glparchis/generateexe_inno.bat



echo "  * Comprimiendo codigo fuente windows..."
cd $DIR/src.windows
zip -r $CWD/dist/glparchis-src-windows-$VERSION.zip ./ >/dev/null
cd $CWD

###### install pyinstaller
if [ ! -d "/tmp/pyinstaller" ]; then
    cd $DIR
    #wget https://github.com/downloads/pyinstaller/pyinstaller/pyinstaller-2.0.tar.bz2
    #tar xjf pyinstaller-2.0.tar.bz2
    git clone git://github.com/pyinstaller/pyinstaller.git
    #mv pyinstaller-2.0 pyinstaller
    cd $CWD
fi

####### binaries linux
#sed -i -e 's:so="src.windows":so="bin.linux":' $DIRSRCWINDOWS/lib/glparchis/libglparchis.py
DESTDIR=$DIRBINLINUX make all
sed -i -e 's:so="src.linux":so="bin.linux":' $DIRBINLINUX/bin/glparchis
python /tmp/pyinstaller/pyinstaller.py -o $DIRBINLINUX -i $DIRBINLINUX/share/glparchis/ficharoja.ico -w -p $DIRBINLINUX/lib/glparchis $DIRBINLINUX/bin/glparchis
echo "Execute glparchis and play" > $DIRBINLINUX/dist/README.txt
cp $DIRBINLINUX/share/glparchis/sounds/*.wav $DIRBINLINUX/dist/glparchis
cp $DIRBINLINUX/share/glparchis/*.qm $DIRBINLINUX/dist/glparchis
mkdir $DIRBINLINUX/dist/glparchis/phonon_backend/
cp /usr/lib64/kde4/plugins/phonon_backend/phonon_gstreamer.so $DIRBINLINUX/dist/glparchis/phonon_backend/
echo "  * Comprimiendo binario linux..."
cd $DIRBINLINUX/dist
tar cvz  -f $CWD/dist/glparchis-bin-linux-$VERSION.tar.gz * -C $DIRBINLINUX/dist > /dev/null
cd $CWD

###### binaries windows
#sed -i -e 's:so="bin.linux":so="bin.windows":' $DIRSRCWINDOWS/lib/glparchis/libglparchis.py
DESTDIR=$DIRBINWINDOWS make all
sed -i -e 's:so="src.linux":so="bin.windows":' $DIRBINWINDOWS/bin/glparchis
wine $HOME/.wine/drive_c/Python27/python.exe  /tmp/pyinstaller/pyinstaller.py -o $DIRBINWINDOWS -i $DIRBINWINDOWS/share/glparchis/ficharoja.ico -w -p $DIRBINWINDOWS/lib/glparchis $DIRBINWINDOWS/bin/glparchis
cp $DIRBINWINDOWS/share/glparchis/sounds/*.wav $DIRBINWINDOWS/dist/glparchis
cp $DIRBINWINDOWS/share/glparchis/*.qm $DIRBINWINDOWS/dist/glparchis
cp $CWD/glparchis.iss $DIRBINWINDOWS
sed -i -e "s:XXXXXXXX:$VERSION:" $DIRBINWINDOWS/glparchis.iss
cd $DIRBINWINDOWS
wine $HOME/.wine/drive_c/Program\ Files\ \(x86\)/Inno\ Setup\ 5/ISCC.exe /o$CWD/dist glparchis.iss
cd $CWD

