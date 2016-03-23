#!/bin/bash
rm -Rf build
rm -Rf dist
mkdir -p build/src dist
VERSION=`cat libglparchis.py | grep 'version="2'| cut --delimiter='"'  -f 2`
TIME=`date +%Y%m%d%H%M%S`
CWD=`pwd`
touch build/$VERSION-$TIME dist/$VERSION-$TIME   #Genera fichero con versión y hora de distribución
DIRSRCLINUX=build/src # Se instala con un makefile
PYTHONVERSION=3.4

echo "Este script crea el fichero $FILE para ser subido a sourceforge"

######## sources linux
make > /dev/null
mkdir $DIRSRCLINUX/doc
mkdir $DIRSRCLINUX/i18n
mkdir $DIRSRCLINUX/images
mkdir $DIRSRCLINUX/ui
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
	ui/pos* \
	$DIRSRCLINUX/ui

cp	images/*.png \
	images/*.qrc \
	images/*.ico \
	$DIRSRCLINUX/images

cp 	sounds/* \
	$DIRSRCLINUX/sounds

echo "  * Comprimiendo codigo fuente linux..."
cd build/src
tar cvz  -f $CWD/dist/glparchis-src-linux-$VERSION.tar.gz * -C $CWD/build/src > /dev/null
cd $CWD

####### binaries linux
python3 setup.py build
cd build/exe.linux-x86_64-$PYTHONVERSION
tar cvz  -f $CWD/dist/glparchis-bin-linux-$VERSION.tar.gz * -C $CWD/build/exe.linux-x86_64-$PYTHONVERSION > /dev/null
cd $CWD

