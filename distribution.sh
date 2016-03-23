#!/bin/bash
rm -Rf build
mkdir -p build/src
VERSION=`cat libglparchis.py | grep 'version="2'| cut --delimiter='"'  -f 2`
TIME=`date +%Y%m%d%H%M%S`
CWD=`pwd`
touch build/$VERSION-$TIME   #Genera fichero con versión y hora de distribución
DIRSRCLINUX=build/src # Se instala con un makefile

echo "Este script crea el fichero $FILE para ser subido a sourceforge"


make

######## sources linux
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
tar cvz  -f $CWD/build/glparchis-src-$VERSION.tar.gz * -C $CWD/build/src > /dev/null
cd $CWD

####### binaries linux
python3 setup.py build

