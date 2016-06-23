#!/usr/bin/python3
import os
import sys
from PyQt5.QtCore import *

class i18n(QObject):
    """Se escribe sin acentos y sin n"""
    def __init__(self):
        QObject.__init__(self)
        self.languages=["es", "en"]
        self.translator=QTranslator()
        
        for l in self.languages:
            #### COPY CARGARQTRANSLATOR ####
            urls= ["i18n/glparchis_" + l + ".qm","/usr/share/glparchis/glparchis_" + l + ".qm"]
            for url in urls:
                if os.path.exists(url)==True:
                    print ("Found {} from {}".format(url,  os.getcwd()))
                    break
                else:
                    print ("Not found {} from {}".format(url,  os.getcwd()))        
            self.translator.load(url)
            QCoreApplication.installTranslator(self.translator);
            ###################################
            self.changelog(l)
            self.authors(l)
            self.install(l)
    def changelog(self, language):
        f=open("CHANGELOG-{}.txt".format(language.upper()), "w")
        f.write("20160623\n")
        f.write("--------\n")
        f.write(self.tr("- Anadido el script project_i18n para traducir la documentacion del proyecto")+"\n")
        f.write(self.tr("- Ahora el tablero rota por su centro pulsando la letra m")+"\n")
        f.write(self.tr("- Rendimiento mejorado")+"\n")
        f.write(self.tr("- Corregido error con el icono de fullscreen")+"\n")
        f.write("\n")

        f.write(self.tr("""
20160325
--------
- La configuracion del sonido se graba ahora en glparchis.cfg
- Se ha cambiado el makefile para que se compile con make y se instale con make install
- Ya no se van a distribuir los sources de windows
- Ahora se generan versiones de Windows de 32 bits y de 64 bits
- Se ha eliminado el soporte para phonon, ahora se utiliza QMultimedia
- Se ha migrado a PyQt5
- Se ha anadido el modo de pantalla completa
"""))

        f.write(self.tr("""
20130716
--------
- Cuando se come una ficha en la casilla de salida, esta ficha es la ultima en llegar si son dos distintas al color de la casilla
- Cambiado el pink por el fuchsia, el cyan por darkturquoise y el orange por darkorange en colores web. 
- Se ha anadido compatibilidad con los highscores que usaban los antiguos
- Se ha anadido soporte para autoguardado
- Mejorado el interfaz de usuario
- Solucionado error al cerrar la aplicacion
- Anadida opcion de que el panel de usuario siga al jugador actual o no
- Al guardar la partida se graba, el tiempo de inicio y el numero de fichas comidas.
- Se ha migrado a python3, yo lo he testeado con python 3.3

20130228
--------
- Ahora se muestra un dado en Acerca De
- Mejorado el cmdDado
- Ahora se puede tirar el dado haciendo doble click encima del tablero.
- Solucionando problema con el sistema de consultar actualizaciones
- Se ha anadido soporte para highscores
- Se ha anadido juegos de 6 y 8 jugadores

20120921
--------
- Solucionado error al buscar si hay actualizacion disponible
- Agregadas texturas numericas a las casillas
- Emite un sonido si se va por 3 seises a casa.
- Ahora permite guardar la partida cuando esta con todos jugadores IA
- Se han modificado los sonidos del juego
- Solucionado problema de un doble click en el dado
- Se ha puesto la visualizacion del dado en 3D

20120917
--------
- Solucionado bug al pulsar la tecla ESCAPE. Ahora sale de la aplicacion
- Anadido apagar / encender sonido
- Enlaces de pantalla ahora son clickables
- Nueva opcion de menu que busca actualizaciones de forma manual o cada 7 dias
- Ahora el splitter muestra el ogl por defecto
- Ahora el idioma por defecto es el ingles , pero en settings se puede cambiar el idioma y se graba en fichero de configuracion
- Se ha anadido un pequeno manual de ayuda al juego. Se puede acceder pulsando F1
- Los popup no se salen de la pantalla.

20120914
--------
- Anadida distribucion de binarios en windows y linux
- Solucionado bug al cancelar en el dialogo inicial
- Solucionados numeros bugs

20120910
--------
- Solucionado problema con directorio de partidas guardadas
- El texto del dado cambia de color segun el jugador actual
- Se ha anadido puntuacion al juego teniendo en cuenta el numero de casillas movidas. 
- Se ha anadido una corona en la tabla de estadisticas al jugador que va ganando.
- Ahora se muestra los primeros movimientos cuando empieza un jugador de AI
- Solucionados varios bugs
- Mejorada la inteligencia artificial de los jugadores virtuales, con un porcentaje de acierto en las decisiones
- Se ha anadido un contador con el tiempo de partida transcurrido
- Se ha mejorado la visualizacion de logs en pantalla

20120902
--------
- Se ha dado el soporte inicial a la aplicacion
- La aplicacion es plenamente funcional. Falta mejorar el IA de los jugadores virtuales

"""))
        f.close()        
        
        
        
        
        
        
        
        
    def authors(self, language):
        f=open("AUTHORS-{}.txt".format(language.upper()), "w")
        f.write(self.tr("""
Idea y desarrollo
----------------- 
Mariano Munoz <turulomio@yahoo.es> 

Traduccion
---------- 
English: Mariano Munoz <turulomio@yahoo.es>
French: Nadejda Adam
"""))
        f.close()
        
    def install(self, language):
        f=open("INSTALL-{}.txt".format(language.upper()), "w")
        f.write(self.tr("""
Requisitos
==========
El programa tiene las siguientes dependencias:
  - PyQt4
  - pyopengl
  - python3

Procedimiento de instalacion para fuentes linux
===============================================

Se descomprime el fichero 
Una vez en el directorio en el que esta el Makefile se ejecuta
  # make; make install

Si usas la distribucion Gentoo, te puedes bajar el ebuild desde
https://xulpymoney.svn.sourceforge.net/svnroot/xulpymoney/myportage/games-board/glparchis/

Si eres atrevido o quieres ayudarme con el desarrollo te lo puedes bajar del subversion con el siguiente comando
  # svn co https://glparchis.svn.sourceforge.net/svnroot/glparchis/pyglParchis glparchis

Para desinstalar utiliza el siguiente comando hace una desinstalacion limpia
  # make uninstall

  
  
Procedimiento de instalacion para binarios linux
================================================

Se descomprime el fichero con el comando 
  # tar xvfz glparchis-bin-linux-VERSION.tar.gz 

Se entra en el directorio glparchis, que se acaba de crear con
  # cd glparchis

y se ejecuta el fichero glparchis con
  # ./glparchis

  
  
Procedimiento de instalacion para binarios windows
==================================================



Procedimiento de instalacion para fuentes windows
=================================================

"""))
        f.close()
################
app = QCoreApplication(sys.argv)
i18n()
