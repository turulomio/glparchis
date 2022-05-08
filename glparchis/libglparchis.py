from logging import debug
from pkg_resources import resource_filename
from OpenGL.GL import glVertex3fv, glBegin, glBindTexture, glColor3d, glDisable, glEnable, glEnd, glPopMatrix, glPopName, glPushName, glPushMatrix, glRotated, glScaled, glTexCoord2f, glTranslated, glTranslatef, glVertex3d, GL_TEXTURE_2D, GL_QUADS, GL_POLYGON, GL_LINE_LOOP
from OpenGL.GLU import gluCylinder, gluDisk, gluNewQuadric, gluQuadricDrawStyle, gluQuadricNormals, gluQuadricTexture, GLU_FILL, GLU_SMOOTH
from glparchis.ui.poscasillas8 import poscasillas8
from glparchis.ui.poscasillas4 import poscasillas4
from glparchis.ui.poscasillas3 import poscasillas3
from glparchis.ui.poscasillas6 import poscasillas6
from os import path, chdir
from random import random, seed
from configparser import ConfigParser
from datetime import datetime, date, timedelta
from math import sin, cos, tan, pi
from codecs import open as codecs_open
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5.QtCore import Qt, QObject,  pyqtSignal,  QUrl
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtMultimedia import QSoundEffect
from uuid import uuid4
from glparchis.libglparchistypes import TTextures,  TNames, TSquareTypes,  TPlayers
from glparchis.libmanagers import ObjectManager_With_Id, ObjectManager, DictObjectManager_With_Id
from glparchis.functions import swap_list_with_two_items, str2bool, qmessagebox, delay
from abc import ABC,  abstractmethod

## Class to manage game pawns
class ManagerPawnsGame(DictObjectManager_With_Id):
    def __init__(self):
        DictObjectManager_With_Id.__init__(self)



class Dado(QObject):
    """
        QGLWidget used during game
    """
    throwed=pyqtSignal()
    def __init__(self ):
        QObject.__init__(self)
        self.fake=[]
        self.lasttirada=None
        self.position=(0, 0, 0)
        self.showing=True
        
    def tirar(self):
        seed(datetime.now().microsecond)
        if len(self.fake)>0:
            resultado=self.fake[0]
            self.fake.remove(self.fake[0])
        else:
            resultado= int(random()*6)+1
        self.lasttirada=resultado
        return resultado

    def opengl(self, qglwidget):
        glPushName(TNames.Dice)
        glPushMatrix()
        glScaled(3,3,3);
        glColor3d(255, 255, 255);

        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, qglwidget.texture(TTextures.Dice))
        unter=1.0/3.0;
        doster=2.0/3.0;
        glBegin(GL_QUADS);
        v0=  (0.0, 0.0, 0.0) 
        v1=( 1.0, 0.0, 0.0) 
        v2=( 1.0, 0.0, 1.0) 
        v3=  (0.0, 0.0, 1.0) 

        v4=(0.0, 0.0, 1.0)
        v5=( 1.0, 0.0, 1.0)
        v6=( 1.0, 1.0, 1.0)
        v7=(0.0, 1.0, 1.0)

        v8=(0.0, 0.0, 0.0)
        v9=(0.0, 1.0, 0.0)
        v10=( 1.0, 1.0, 0.0)
        v11=( 1.0, 0.0, 0.0) 

        v12=(0.0, 1.0, 0.0) 
        v13=(0.0, 1.0, 1.0) 
        v14=( 1.0, 1.0, 1.0) 
        v15=( 1.0, 1.0, 0.0) 

        v16=( 1.0, 0.0, 0.0) 
        v17=( 1.0, 1.0, 0.0) 
        v18=( 1.0, 1.0, 1.0) 
        v19=( 1.0, 0.0, 1.0) 

        v20=(0.0, 0.0, 1.0) 
        v21=(0.0, 1.0, 1.0) 
        v22=(0.0, 1.0, 0.0)
        v23=(0.0, 0.0, 0.0)
        glTexCoord2f(0.0, unter);glVertex3fv(v0)
        glTexCoord2f(0.25, unter);glVertex3fv(v1)
        glTexCoord2f(0.25, doster);glVertex3fv(v2)
        glTexCoord2f(0.0, doster);glVertex3fv(v3)  
        glTexCoord2f(0.25, doster);glVertex3fv(v4)
        glTexCoord2f(0.5, doster);glVertex3fv(v5)
        glTexCoord2f(0.5, 1.0);glVertex3fv(v6)
        glTexCoord2f(0.25, 1.0);glVertex3fv(v7)  
        glTexCoord2f(0.25, doster);glVertex3fv(v8)
        glTexCoord2f(0.5, doster);glVertex3fv(v9)
        glTexCoord2f(0.5, unter);glVertex3fv(v10)
        glTexCoord2f(0.25, unter);glVertex3fv(v11)  
        glTexCoord2f(0.25, 0.0);glVertex3fv(v12)
        glTexCoord2f(0.5, 0.0);glVertex3fv(v13)
        glTexCoord2f(0.5, unter);glVertex3fv(v14)
        glTexCoord2f(0.25, unter);glVertex3fv(v15)  
        glTexCoord2f(0.5, unter);glVertex3fv(v16)
        glTexCoord2f(0.75, unter);glVertex3fv(v17)
        glTexCoord2f(0.75, doster);glVertex3fv(v18)
        glTexCoord2f(0.5, doster);glVertex3fv(v19) 
        glTexCoord2f(0.75, unter);glVertex3fv(v20)
        glTexCoord2f(1.0, unter);glVertex3fv(v21)
        glTexCoord2f(1.0, doster);glVertex3fv(v22)
        glTexCoord2f(0.75, doster);glVertex3fv(v23)
        glEnd();

        glDisable(GL_TEXTURE_2D)
        glPopMatrix();
        glPopName();
        
    def draw_alone(self, qglwidget):
        self.position=(0, 0, 0)
        self.opengl(qglwidget)
        
    def draw(self, qglwidget):
        """
            Sets position of the dice during game and showing the number
        """
        if self.showing==False:
            return
        if qglwidget.mem.maxplayers==3:
            if qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("yellow"):
                self.position=(10, 36, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("blue"):
                self.position=(37, 11, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("red"):
                self.position=(44, 48, 1)
        if qglwidget.mem.maxplayers==4:
            if qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("yellow"):
                self.position=(10, 51, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("blue"):
                self.position=(9, 10, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("red"):
                self.position=(50, 10, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("green"):
                self.position=(50, 51, 1)
        elif qglwidget.mem.maxplayers==6:
            if qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("yellow"):
                self.position=(30, 31, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("blue"):
                self.position=(23, 27, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("red"):
                self.position=(23, 18, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("green"):
                self.position=(30, 14, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("dimgray"):
                self.position=(37, 18, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("fuchsia"):
                self.position=(37, 27, 1)
        elif qglwidget.mem.maxplayers==8:
            if qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("yellow"):
                self.position=(30, 30, .9)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("blue"):
                self.position=(19, 27, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("red"):
                self.position=(15, 15, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("green"):
                self.position=(19, 3, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("dimgray"):
                self.position=(30, 0, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("fuchsia"):
                self.position=(40, 3, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("darkorange"):
                self.position=(44, 15, 1)
            elif qglwidget.mem.jugadores.actual==qglwidget.mem.jugadores.find_by_colorname("darkturquoise"):
                self.position=(40, 27, 1)
        
        glTranslatef(self.position[0],self.position[1],self.position[2]);

        if self.lasttirada==1:
            glTranslated(0, 0, 3)
            glRotated(-90.0,1.0,0.0,0.0);
        if (self.lasttirada==3):
            glTranslated(3, 0, 3)
            glRotated(180.0,0.0,1.0,0.0);
        if (self.lasttirada==4):
            glTranslated(0, 3, 0)
            glRotated(90.0,1.0,0.0,0.0);
        if (self.lasttirada==5):
            glTranslated(3, 3, 0)
            glRotated(90.0,1.0,0.0,0.0);
            glRotated(90.0,0.0,0.0,1.0);
        if (self.lasttirada==6):
            glTranslated(0, 0, 3)
            glRotated(90.0,0.0,1.0,0.0);
            
        self.opengl(qglwidget)
        
    def qicon(self, numero):
            ico = QIcon()
            ico.addPixmap(self.qpixmap(numero), QIcon.Normal, QIcon.Off) 
            return ico
            
    def qpixmap(self, numero):
        """Devulve un QPixmap segun el valor del numero 0-6"""
        if numero==1:
            pix=QPixmap(":/glparchis/cube1.png")
        elif numero==2:
            pix=QPixmap(":/glparchis/cube2.png")
        elif numero==3:
            pix=QPixmap(":/glparchis/cube3.png")
        elif numero==4:
            pix=QPixmap(":/glparchis/cube4.png")
        elif numero==5:
            pix=QPixmap(":/glparchis/cube5.png")
        elif numero==6:
            pix=QPixmap(":/glparchis/cube6.png")
        elif numero==None:              
            pix=QPixmap(":/glparchis/cube.png")
        return pix

                    
## Clase que controla las amenazas que se ciernen sobre una ficha
class Threat:
    def __init__(self,  target_pawn, attacking_pawn, tipo):
        self.target_pawn=target_pawn
        self.attacking_pawn=attacking_pawn
        self.tipo=tipo #1-6 dados, 7 seis con todas fuera,10 meter una ficha, 20 comer una ficha, 51 saca un cinco y mueve 1

    ## Returns the name of the Threat
    ## @param self This object class
    ## @param tipo Threat type id. If None returns this object tipo name
    ## @return Returns a string with the name of the threat
    def name(self, tipo=None):
        if tipo==None:
            tipo=self.tipo
        if tipo==1: return QApplication.translate("glparchis","Sacar un 1")
        if tipo==2: return QApplication.translate("glparchis","Sacar un 2")
        if tipo==3: return QApplication.translate("glparchis","Sacar un 3")
        if tipo==4: return QApplication.translate("glparchis","Sacar un 4")
        if tipo==5: return QApplication.translate("glparchis","Sacar un 5")
        if tipo==6: return QApplication.translate("glparchis","Sacar un 6")
        if tipo==7: return QApplication.translate("glparchis","Sacar un 7")
        if tipo==10: return QApplication.translate("glparchis","Contar 10")
        if tipo==20: return QApplication.translate("glparchis","Contar 20")
        if tipo==51: return QApplication.translate("glparchis","Sacar ficha")
        
    ## This function is usefull to detect duplicated threats due to same player barriers
    def stringPlayerAndSquare(self):
        return "{}#{}".format(self.attacking_pawn.jugador.color.name,self.attacking_pawn.casilla().id)

## Class that studies threats of a pawn when setting in a square
class ThreatManager(ObjectManager):
    ## @param mem Mem singleton
    ## @param target_pawn Ficha de la que se van a estudiar las amenazas
    ## @param casilla Casilla en la que queremos estudiar las amenazas tras colocar la ficha target_pawn
    def __init__(self,  mem,  target_pawn, casilla):
        ObjectManager.__init__(self)
        
        ##Pawn to study threats
        self.target_pawn=target_pawn
        
        ##Square 
        self.casilla=casilla
        self.mem=mem
        inicio=datetime.now()
        self.__detect()
        self.__removingBarriers()
        debug("Detectar amenazas de {} en {} llevó: {}".format(self.target_pawn,  self.casilla,  datetime.now()-inicio))
        
    def __append(self, attacking_pawn, type):
        self.arr.append(Threat(self.target_pawn, attacking_pawn, type))
        
    ## Removes Threat of the same player from the same square
    def __removingBarriers(self):
        strPS=[]
        newarr=[]
        for threat in self.arr:
            if threat.stringPlayerAndSquare() not in strPS:
                strPS.append(threat.stringPlayerAndSquare())
                newarr.append(threat)
        del self.arr
        self.arr=newarr
            
    def __detect(self):
        del self.arr
        self.arr=[]
        
        if self.casilla.tipo==TSquareTypes.Initial(self.mem.maxplayers) or self.casilla.tipo==TSquareTypes.Final(self.mem.maxplayers):
            return
        
        if self.casilla.rampallegada==True:
            return

        #Detecta salida con un 5 a ruta1
        if self.casilla.ruta1!=-1:
            #Busca la casilla inicial del mismo color
            casillaataque=self.mem.rutas.arr[self.casilla.ruta1].squareInitial()#Casilla inicial de la ruta del jugador con ruta1=TJugador
            if casillaataque.buzon_numfichas()>0:#Hay fichas que coman
                if self.casilla.buzon_numfichas()==2:
                    if  self.target_pawn.posruta!=1: #Si no esta en su propia ruta1, esta llena
                        position, attacking_pawn=casillaataque.buzon_fichas()[0]
                        if attacking_pawn.puedeComer(self.mem, attacking_pawn.posruta+1): #aqui chequea que sea mismo color o distinta, ultima en llegar...
                            self.__append(attacking_pawn, 51)
                        else:
                            return
                    else:#Esta en su propia ruta1
                        return
                else:
                    return
            else:
                return
        
        if self.casilla.seguro==True:#All secure squares, including "route1 squares" for the rest of enemy pawns, not only route1
            return
        
        #Detecta si hay ficha en OJO LA CASILLA QUE SE BUSCA NO ES LA ACTUAL DEL OBJETIVO sino la de parametro de entrada self.casilla
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -1)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador!=self.target_pawn.jugador and ficha.estaAutorizadaAMover(1) and ficha.puedeComer(self.mem, ficha.posruta+1):
                self.__append(ficha, 1)

        #Detecta si hay ficha en 2
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -2)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador!=self.target_pawn.jugador  and ficha.estaAutorizadaAMover(2) and ficha.puedeComer(self.mem, ficha.posruta+2):
                self.__append(ficha, 2)

        #Detecta si hay ficha en 3
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -3)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador!=self.target_pawn.jugador  and ficha.estaAutorizadaAMover(3) and ficha.puedeComer(self.mem, ficha.posruta+3):
                self.__append(ficha, 3)
    
        #Detecta si hay ficha en 4
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -4)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador!=self.target_pawn.jugador and ficha.estaAutorizadaAMover(4)  and ficha.puedeComer(self.mem, ficha.posruta+4):
                self.__append(ficha, 4)
        #Detecta si hay ficha en 5
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -5)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador.tieneFichasEnCasa(): continue
            if ficha.jugador!=self.target_pawn.jugador  and ficha.estaAutorizadaAMover(5) and ficha.puedeComer(self.mem, ficha.posruta+5):
                self.__append(ficha, 5 )
        #Detecta si hay ficha en 6 y chequea que no tiene todas fuera de casa
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -6)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador.tieneFichasEnCasa()==False:
                continue
            if ficha.jugador!=self.target_pawn.jugador  and ficha.estaAutorizadaAMover(6) and ficha.puedeComer(self.mem, ficha.posruta+6):
                self.__append(ficha, 6 )
                
        #Detecta si hay ficha en 7 y chequea que tiene todas fuera de casa
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -7)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador.tieneFichasEnCasa()==True:
                continue
            if ficha.jugador!=self.target_pawn.jugador and ficha.estaAutorizadaAMover(7)  and ficha.puedeComer(self.mem, ficha.posruta+7):
                self.__append(ficha, 7 )
        
        #Detecta si hay ficha en 10
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -10)
        for posicion, ficha in casillaataque.buzon_fichas():
            if (ficha.ruta.casillaEstaEnRuta(self.casilla) and 
                ficha.jugador.tieneFichasATiroDeLlegada() and 
                ficha.jugador!=self.target_pawn.jugador  and 
                ficha.estaAutorizadaAMover(10) and 
                ficha.puedeComer(self.mem, ficha.posruta+10) and 
                ficha.jugador.tieneFichasATiroDeLlegada()
            ):
                self.__append(ficha, 10 )
                
        #Detecta si hay ficha en 20
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -20)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.ruta.casillaEstaEnRuta(self.casilla)==False: continue
            if ficha.jugador!=self.target_pawn.jugador  and ficha.estaAutorizadaAMover(20) and ficha.puedeComer(self.mem, ficha.posruta+20):
                self.__append(ficha, 20)


class TiradaHistorica:
    """Estudio estadistico de tiradas. Lleva un array con todas los objetos TiradaTurno por cada jugador
    Se graba cuando se tira ya que es un objeto TiradaTurno que se vincula en el array de TiradaHistorica"""
    def __init__(self):
        self.arr=[]
    
    def numThrows(self):
        """Gets the number of total and historic player throws"""
        resultado=0
        for tt in self.arr:
            resultado=resultado+tt.numThrows()
        return resultado
        
    def numTimesDiceGetNumber(self, number):
        """Gets the number of times that the dice gets the number"""
        resultado=0
        for tt in self.arr:
            for t in tt.arr:
                if t.valor==number:
                    resultado=resultado+1
        return resultado
        
    def numThreeSixes(self):
        """Gets the number of times that the dice get three sixes"""
        resultado=0
        for tt in self.arr:
            if tt.tresSeises()==True:
                resultado=resultado+1
        return resultado
        
    def length(self):
        return len(self.arr)
                
class TiradaJuego:
    """Estudio estadistico de tiradas globales del juego (une todos jugadores). Se usa para temas estadisticos y recorre las tiradas
    historicas de todos los jugadores."""
    def __init__(self, mem):
        self.mem=mem
    
    def numThrows(self):
        """Gets the number of total and historic player throws"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numThrows()
        return resultado
        
    def numTimesDiceGetNumber(self, number):
        """Gets the number of times that the dice gets the number"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numTimesDiceGetNumber(number)
        return resultado
        
    def numThreeSixes(self):
        """Gets the number of times that the dice get three sixes"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numThreeSixes()
        return resultado
        
class Tirada:
    """Lanzamiento individual de un dado"""
    def __init__(self, jugador, valor,  tipo=None):
        self.jugador=jugador
        self.valor=valor
        self.tipo=tipo#None desconocido 1 turno normal, dos por seis, tres por comer, cuatro por meter

class TiradaTurno:
    """Objeto que recoge todos las tiradas de un turno"""
    def __init__(self):
        self.jugador=None
        self.arr=[]
        
    def tresSeises(self):
        """Funcion que devuelve un booleano segun haya o no salido 3 seises"""
        if len(self.arr)==3:
            if self.arr[0].valor==6 and self.arr[1].valor==6 and self.arr[2].valor==6:
                return True
        return False
        
    def ultimoEsSeis(self):
        if len (self.arr)>0:
            if self.arr[len(self.arr)-1].valor==6:
                return True
        return False
        
    def ultimoValor(self):
        """Devuelve el ultimo valor realizado y None si no ha realizado ninguno."""
        if len(self.arr)>0:
            return self.arr[len(self.arr)-1].valor
        else:
            return None
            
    def numThrows(self):
        """Gets the number of throws in the turn"""
        return len (self.arr)


class HighScore:
    """Clase que calcula gestiona todo lo relacionado con el highscore. Solo debe usarse cuando haya acabado la partida
    y haya un winner"""
    def __init__(self, mem, players):
        self.players=players
        self.mem=mem
        self.arr=[]#Cada item tendra la fecha en ordinal, nombre, tiempo de partida, color, el score
        self.load()

    def insert(self):
        """Solo se puede ejecutar, cuando haya un winner"""
        self.arr.append((date.today().toordinal(), self.mem.jugadores.winner.name, int((datetime.now()-self.mem.playedtime).total_seconds()), self.mem.jugadores.winner.color.name,  self.mem.jugadores.winner.score()))
        self.sort()
        
    def qtablewidget(self, table): 
        colores=ColorManager()#Se pinta hs,hs6 y hs8
        colores.generar_colores(8)
        table.setRowCount(len(self.arr))        
        self.sort()
        for i,  a in enumerate(self.arr):
            item=QTableWidgetItem(str(date.fromordinal(int(a[0]))))
            table.setItem(i, 0, item)
            item = QTableWidgetItem(a[1])
            item.setIcon(colores.find_by_name(a[3]).qicon())                
            table.setItem(i, 1, QTableWidgetItem(item))
            item = QTableWidgetItem(str(timedelta(seconds=int(a[2]))))
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            table.setItem(i, 2, item)
            item = QTableWidgetItem(str(a[4]))
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            table.setItem(i, 3, item)

    def load(self):
        try:
            f=codecs_open(path.expanduser("~/.glparchis/")+ "highscores"+str(self.players), "r", "utf-8")
            for line in f.readlines():
                a=line[:-1].split(";")
                self.arr.append((a[0], a[1], a[2], self.mem.colores.arr[0].compatibilityName(a[3]),  int(a[4])))
            f.close()
        except:
            print("I couldn't load highscores")
            
    def sort(self):        
        self.arr=sorted(self.arr, key=lambda a:a[4],  reverse=True)     

        
    def save(self):        
        f=codecs_open(path.expanduser("~/.glparchis/")+ "highscores"+str(self.players), "w", "utf-8")
        s=""
        print (self.arr)
        for a in self.arr[:10]:
            s=s+"{0};{1};{2};{3};{4}\n".format(a[0], a[1],  a[2], a[3], a[4])
        f.write(s)
        f.close()
                
class Jugador(QObject):
    logEmitted=pyqtSignal(str)
    def __init__(self, mem,  color):
        QObject.__init__(self)
        self.mem=mem
        self.name=None#Es el nombre de usuario no el de color
        self.color=color
        self.ia=False
        self.plays=True
        self.fichas=SetFichas(self.mem)     
        self.tiradaturno=TiradaTurno()#TiradaJugador()
        self.tiradahistorica=TiradaHistorica()
        self.LastFichaMovida=None #Se utiliza cuando se va a casa NOne si ninguna
        self.movimientos_acumulados=None#Comidas ymetidas, puede ser 10, 20 o None Cuando se cuenta se borra a None
        self.dado=None #Enlace a objeto dado de mem
        self.comidaspormi=0
        self.comidasporotro=0
        self.ruta=None#Se apunta

    def __repr__(self):
        return "Jugador {0}".format(self.color.name)

    def log(self, l):
        l="{0} {1}".format(str(datetime.now().time()).split(".")[0], l)
        self.logEmitted.emit(l)
        
    def casillasPorMover(self):
        """
            Casillas que le queda al jugador hasta ganar la partida
        """
        resultado =0
        for f in self.fichas.arr:
            resultado=resultado+f.casillasPorMover()
        return resultado
            
            
    def casillasPorMoverATodosLosDemas(self):
        """Casillas que le queda al resto de jugadores por mover. Las de este jugador no cuentan"""
        sum_pormover=0
        for j in self.mem.jugadores.arr:
            if j!=self:
                sum_pormover=sum_pormover+j.casillasPorMover()
        return sum_pormover
            
    def casillasMovidas(self):
        """
            Devuelve el número de Casillas que ha movido el jugador, puede considerarse la puntuacion del jugador
        """
        return 4*self.fichas.arr[0].ruta.length()-self.casillasPorMover()
            
        
    def hayDosJugadoresDistintosEnRuta1(self):
        ruta1=self.ruta.squareFirst()
        if ruta1.buzon_numfichas()!=2:
            return False
        if ruta1.buzon[0].jugador!=ruta1.buzon[1].jugador:
            return True
        return False
        
        
    def tirarDado(self,  number=None):
        """Tira el dado lo almacena en tirada, tiradaturno e historico y devuelve el valor
        Se usa number, cuando se hace un load .glparchis, para regenerar las estad´isticas
        """
        if number==None:
            tirada=Tirada(self, self.dado.tirar())
        else:
            tirada=Tirada(self, number)#Se usa cuando se hace un load, para regenerar las estad´isticas
        self.tiradaturno.arr.append(tirada)
        if self.tiradaturno not in self.tiradahistorica.arr:
            self.tiradahistorica.arr.append(self.tiradaturno)
        return tirada.valor

    def barreras(self):
        """Devuelve una lista con las casillas en las que el jugador tiene barrera"""
        resultado=[]
        for f in self.fichas.arr:
            if f.casilla().tieneBarrera()==True:
                resultado.append(f.casilla())
        return resultado
                
    def score(self):
        """Da la puntuacion de un jugador"""
        return 500+(self.comidaspormi-self.comidasporotro)*40+ self.casillasMovidas()*2+ self.casillasPorMoverATodosLosDemas()*5

    def tieneBarreras(self):
        if len(self.barreras())>0:
            return True
        return False

    def tieneFichasEnCasa(self):
        for f in self.fichas.arr:
            if f.estaEnCasa()==True:
                return True
        return False
        
    def tieneFichasEnRampaLlegada(self):
        """Devuelve un booleano si el jugador tiene fichas en la rampa de llegada"""
        for f in self.fichas.arr:
            if f.casilla().rampallegada==True:
                return True
        return False
        
    def tieneFichasATiroDeLlegada(self):
        """Devuelve un booleano segun el jugador tenga fichas a tiro de llegada o no"""
        for f in self.fichas.arr:
            if f.estaATiroDeLlegada()==True:
                return True
        return False
        
    def DefaultName(self):
        d={}
        d["yellow"]="Yellowy"
        d["blue"]="Bluey"
        d["red"]="Redy"
        d["green"]="Greeny"
        d["dimgray"]="Graye"
        d["fuchsia"]="Pinky"
        d["darkorange"]="Orangy"
        d["darkturquoise"]="Cyanny"
        return d[self.color.name]

    def HaGanado(self):
        for f in self.fichas.arr:
            if f.estaEnMeta()==False:
                return False
        return True
        
    ## Funcion que devuelve la ficha seleccionada por la IA. Si devuelve None es que ninguna se puede mover 
    def IASelectFicha(self):
        def azar():
            """Funcion que saca un numero al azar de entre 1 y 100. Si es mayor del tope devuelve true. Sino devuelve false. Es decir tope 85 es una probabilidad del 85%"""
            seed(datetime.now().microsecond)
            numero=int(random()*100)
            if numero<self.mem.difficulty:
                return True
            return False
        ####################################
        fichas=self.fichas.fichasAutorizadasAMover()
        if fichas.length()==0:
            return None
        fichas.order_by_posruta(reverse=True)
        
        # Hay porcentajes de acierto si falla pasa a la siguiente prioridad
        #1 prioridad. Puede comer IA 85%
        if azar():
            for f in fichas.arr:#Recorre las que pueden mover
                movimiento=f.estaAutorizadaAMover()[1]
                (puede, fichaacomer)=f.puedeComer(self.mem, f.posruta+movimiento)
                if puede:
                    print (f, "seleccionada por azar comer")
                    return f

        #2 prioridad. Mueve fichas que disminuyen en numero de amenazas en la nueva posicion
        if azar():  
            fichas.order_by_numero_amenazas(reverse=True)
            for f in fichas.arr:
                movimiento=f.estaAutorizadaAMover()[1]
                antes=f.amenazas()
                despues=f.amenazasDestino(movimiento)
                if antes.length()>despues.length():
                    print (f, "seleccionada por azar al mejorar numero de fichas la pueden comer. Pasa de {0} a {1}".format(antes.length(), despues.length()))
                    return f
        
        
        #3 prioridad Asegura IA  de ultima a primera 85%
        fichas.order_by_posruta(reverse=True)
        if azar():
            for f in fichas.arr:
                movimiento=f.estaAutorizadaAMover()[1]
                if f.casilla().esSegura(self.mem, self, True)==False  and  f.casilla(f.posruta+movimiento).esSegura(self.mem, self, False)==True:
                    print (f,"seleccionado por azar asegurar")
                    return f
        
        #4 Alguna ficha no asegurada puede mover
        if azar():
            for f in fichas.arr:
                if f.casilla().esSegura(self.mem, f.jugador, True)==False:
                    print(f,"seleccionado por azar ficha no asegurada")
                    return f
        
        #5 prioridad Mueve la ultima IA 100%
        print (fichas.first(), "Sin azar. Ultima ficha")
        return fichas.first()

## Clase con un array de casillas en self.arr de la ruta de un color.
class Ruta:
    def __init__(self, color, mem):
        self.arr=[] #Array ordenado
        self.color=color
        self.mem=mem
        
    def append_id(self,  arr):
        """Funcion que recibe un arr con los id de la ruta"""
        for id in arr:
            self.arr.append(self.mem.casillas.find_by_id(id))
            
    def length(self):
        """Saca el numero de casillas """
        return len(self.arr)
        
    def squareInitial(self):
        return self.arr[0]
        
    ## Devuelve la primera casilla de la ruta, a la que se sale con un 5.
    def squareFirst(self):
        return self.arr[1]
        
    def squareFinal(self):
        return self.arr[self.length()-1]
        
    ## Localiza una casilla de la ruta dando una casilla y su posición relativa.
    ## @param casilla Casilla used to locate
    ## @param position Número de casillas a mover adelante o atrás
    def locate(self, square, position):
        try:
            return self.arr[self.arr.index(square)+position]
        except:
            print ("I couldn't find the square at position {} from square {}".format(position, square))
    
    ## Returns the position in the route of the final square
    def squareFinalPosition(self):
        return self.length()-1
    
    ##Devuelve si la casilla esta en la ruta
    def casillaEstaEnRuta(self, casilla):
        if casilla in self.arr:
            return True
        return False
    
class ColorManager(ObjectManager):
    def __init__(self):
        ObjectManager.__init__(self)
    
    def generar_colores(self, maxplayers):
        self.arr.append(Color( 255, 255, 50, "yellow"))
        self.arr.append(Color(50, 60, 180, "blue"))
        self.arr.append(Color(255, 50, 50, "red"))
        if maxplayers>3:
            self.arr.append(Color(50, 255, 50, "green"))
        if maxplayers>4:#Para 6
            self.arr.append(Color(64, 64, 64, "dimgray"))
            self.arr.append(Color(255, 50, 255, "fuchsia"))
        if maxplayers>6:# Para 8
            self.arr.append(Color(255, 128, 50, "darkorange"))
            self.arr.append(Color(50, 255, 255, "darkturquoise"))

    ## Find color by name
    ## @param name Can be: yellow, blue, red, green, dimgray, fuchsia, darkorange, darkturquoise
    def find_by_name(self, name=None):
        for c in self.arr:
            if c.name==name:
                return c
        print ("No se ha encontrado el color de nombre {0}".format(name))
        
class SetJugadores(ObjectManager):
    """Agrupacion de jugadores"""
    def __init__(self, mem):
        ObjectManager.__init__(self)
        self.mem=mem
        self.actual=None
        self.winner=None
        
    def numPlays(self):
        """Number of players playing"""
        r=0
        for j in self.arr:
            if j.plays==True:
                r=r+1
        return r
        
    def cambiarJugador(self):
        index=self.arr.index(self.actual)
        if index==len(self.arr)-1:#Index position
            self.actual=self.arr[0]
        else:
            self.actual=self.arr[index+1]
            
        if self.actual.plays==False:
            self.cambiarJugador()
            return
        else:
            self.actual.tiradaturno=TiradaTurno()#Se crea otro objeto porque asi el anterior queda vinculada< a TiradaHistorica.
            self.actual.movimientos_acumulados=None
            self.actual.LastFichaMovida=None

    def vaGanando(self):
        """Devuelve el objeto del jugador que va ganando"""
        resultado=self.arr[0]#Selecciona primer jugador
        maxpunt=resultado.casillasMovidas()
        for j in self.arr:
            if j.casillasMovidas()>maxpunt:
                maxpunt=j.casillasMovidas()
                resultado=j
        return resultado
        
    def find_by_colorname(self, colorname):
        for j in self.arr:
            if j.color.name==colorname:
                return j
        return None
        
    def alguienHaGanado(self):
        for j in self.arr:
            if j.HaGanado()==True:
                return True
        return False
        
        
        
class SetRutas(ObjectManager):
    def __init__(self, numplayers,  mem):
        """Mem se necesita para identificar los colores"""
        ObjectManager.__init__(self)
        self.mem=mem
        self.numplayers=numplayers
        self.generar_rutas()
        
    def ruta(self, id):        
        """id es el mismo que el orden de los colores"""
        return self.arr[id]
        
    def generar_rutas(self):
        if self.numplayers==3:
            self.generar_rutas3()
        if self.numplayers==4:
            self.generar_rutas4()
        elif self.numplayers==6:
            self.generar_rutas6()
        elif self.numplayers==8:
            self.generar_rutas8()

    def generar_rutas3(self):    
        r=Ruta(self.mem.colores.arr[TPlayers.Yellow], self.mem)
        r.append_id( [76]+list(range(5, 59+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Blue], self.mem)
        r.append_id([77]+ list(range(22, 51+1))+list(range(1, 17+1))+list(range(60, 67+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Red], self.mem)
        r.append_id( [78]+list(range(39, 51+1))+list(range(1, 34+1))+list(range(68, 75+1)))
        self.arr.append(r)    
        
    def generar_rutas4(self):    
        r=Ruta(self.mem.colores.arr[TPlayers.Yellow], self.mem)
        r.append_id( [101]+list(range(5, 76+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Blue], self.mem)
        r.append_id([102]+ list(range(22, 68+1))+list(range(1, 17+1))+list(range(77, 84+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Red], self.mem)
        r.append_id( [103]+list(range(39, 68+1))+list(range(1, 34+1))+list(range(85, 92+1)))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.arr[TPlayers.Green], self.mem)
        r.append_id([104]+list(range(56, 68+1))+list(range(1, 51+1))+list(range(93, 100+1)))
        self.arr.append(r)        
            

    def generar_rutas6(self):    
        r=Ruta(self.mem.colores.arr[TPlayers.Yellow], self.mem)
        r.append_id([151]+list(range(5, 110+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Blue], self.mem)
        r.append_id([152]+list(range(22, 102+1))+list(range(1, 17+1))+list(range(111, 118+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Red], self.mem)
        r.append_id( [153]+list(range(39, 102+1))+list(range(1, 34+1))+list(range(119, 126+1)))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.arr[TPlayers.Green], self.mem)
        r.append_id([154]+list(range(56, 102+1))+list(range(1, 51+1))+list(range(127, 134+1)))
        self.arr.append(r)      
        r=Ruta(self.mem.colores.arr[TPlayers.Gray], self.mem)
        r.append_id([155]+list(range(73, 102+1))+list(range(1, 68+1))+list(range(135, 142+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Fuchsia], self.mem)
        r.append_id([156]+list(range(90, 102+1))+list(range(1, 85+1))+list(range(143, 150+1)))
        self.arr.append(r)       

    def generar_rutas8(self):    
        r=Ruta(self.mem.colores.arr[TPlayers.Yellow], self.mem)
        r.append_id([201]+list(range(5, 144+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Blue], self.mem)
        r.append_id([202]+list(range(22, 136+1))+list(range(1, 17+1))+list(range(145, 152+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Red], self.mem)
        r.append_id( [203]+list(range(39, 136+1))+list(range(1, 34+1))+list(range(153, 160+1)))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.arr[TPlayers.Green], self.mem)
        r.append_id([204]+list(range(56, 136+1))+list(range(1, 51+1))+list(range(161, 168+1)))
        self.arr.append(r)            
        r=Ruta(self.mem.colores.arr[TPlayers.Gray], self.mem)
        r.append_id([205]+list(range(73, 136+1))+list(range(1, 68+1))+list(range(169, 176+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Fuchsia], self.mem)
        r.append_id([206]+list(range(90, 136+1))+list(range(1, 85+1))+list(range(177, 184+1)))
        self.arr.append(r)
        r=Ruta(self.mem.colores.arr[TPlayers.Orange], self.mem)
        r.append_id([207]+list(range(107, 136+1))+list(range(1, 102+1))+list(range(185, 192+1)))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.arr[TPlayers.Turquoise], self.mem)
        r.append_id([208]+list(range(124, 136+1))+list(range(1, 119+1))+list(range(193, 200+1)))
        self.arr.append(r)    

class CasillaManager(ObjectManager_With_Id):
    def __init__(self, numplayers, mem):
        ObjectManager_With_Id.__init__(self)
        self.mem=mem
        self.numplayers=numplayers
        if self.numplayers==3:
            self.number=79
        elif self.numplayers==4:
            self.number=105
        elif self.numplayers==6:
            self.number=157
        elif self.numplayers==8:
            self.number=209
        self.generar_casillas()

    def generar_casillas(self):
        if self.numplayers==6:
            self.generar_casillas6()
        elif self.numplayers==8:
            self.generar_casillas8()
        elif self.numplayers==4:
            self.generar_casillas4()
        elif self.numplayers==3:
            self.generar_casillas3()
                                
    def generar_casillas3(self):
        def defineRutas1(id):
            """Es igual para 3, 4,6,8"""
            if id==5: return TPlayers.Yellow
            if id==22: return TPlayers.Blue
            if id==39: return TPlayers.Red
            return -1
                
        def defineSeguro( id):
            if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51:
                return True
            elif id>=52 and id<=78:#Las de la rampa de llegada tambien son seguras
                return True
            else:
                return False
    
        def defineMaxFichas( id):
            if id==76 or id==77 or id==78 or id==59 or id==67 or id==75:
                return 4
            else:
                return 2
    
        def defineRampaLlegada(id):
            if id>=52 and id<= 75:
               return True
            return False
    
        def defineTipo( id):
            if id==76 or id==77 or id==78 :
               return TSquareTypes.Initial3 #Casilla inicial
            elif id==59 or id==67 or id==75:
               return TSquareTypes.Final3 #Casilla final
            else:
                return TSquareTypes.Normal #Casilla Normal
    
        def defineColor( id):
            if id==5 or (id>=52 and id<=59) or id==76:
               return self.mem.colores.arr[TPlayers.Yellow]
            elif id==22 or (id>=60 and id<=67) or id==77:
               return self.mem.colores.arr[TPlayers.Blue]
            elif id==39 or (id>=68 and id<=75) or id==78:
               return self.mem.colores.arr[TPlayers.Red]
            else:
                return Color(255, 255, 255)            
                
        def defineRotatePN(id):
            """EStablece si debe rotar el panel numerico"""
            if id in range(9, 42+1) :#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):#, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,  61, 62, 63, 64, 65, 66, 67, 68 ):
                return True
            return False
                 
        def defineRotate( id):
            if (id in range(9, 25+1) or id in range(60, 66+1) ):
               return 120
            elif id==75:
                return 60
            elif (id in range(26, 42+1) or id in range(68, 75+1) or id==78):
               return 240
            elif id in (59, ):
                return 180
            elif id in (77, ):
                return 120
            elif id in (67, ):
                return 300
            else:
                return 0        
                
        ## Swaps pawn coords in square when needed
        ## In Color Ramp we set first pawn opposite to initial square
        ## First coord inside route
        def swapPawnCoordsInSquare(c):
            if c.id in [1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24, 25, 34, 35, 36, 37, 38, 39, 40, 41, 42]:
                swap_list_with_two_items(c.pawncoords)
        ##############################       
        posCasillas=poscasillas3(self.number)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            c=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), defineRutas1(i))
            swapPawnCoordsInSquare(c)
            self.arr.append(c)
            
    def generar_casillas4(self):
        def defineRutas1(id):
            """Es igual para 4,6,8"""
            if id==5: return TPlayers.Yellow
            if id==22: return TPlayers.Blue
            if id==39: return TPlayers.Red
            if id==56: return TPlayers.Green
            return -1
                
        def defineSeguro( id):
            if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
                return True
            elif id>=69 and id<=100:#Las de la rampa de llegada tambien son seguras
                return True
            else:
                return False
    
        def defineMaxFichas( id):
            if id==101 or id==102 or id==103 or id==104 or id==76 or id==84 or id==92 or id==100:
                return 4
            else:
                return 2
    
        def defineRampaLlegada(id):
            if id>=69 and id<= 100:
               return True
            return False
    
        def defineTipo( id):
            if id==101 or id==102 or id==103 or id==104:
               return TSquareTypes.Initial4 #Casilla inicial
            elif id==76 or id==84 or id==92 or id==100:
               return TSquareTypes.Final4 #Casilla final
            elif id==9 or  id==26 or  id==43 or  id==60:  
               return TSquareTypes.ObliqueLeft4 #Casilla oblicuai
            elif id==8 or  id==25 or  id==42 or  id==59:  
               return TSquareTypes.ObliqueRight4 #Casilla oblicuad
            else:
                return TSquareTypes.Normal #Casilla Normal
    
        def defineColor( id):
            if id==5 or (id>=69 and id<=76) or id==101:
               return self.mem.colores.arr[TPlayers.Yellow]
            elif id==22 or (id>=77 and id<=84) or id==102:
               return self.mem.colores.arr[TPlayers.Blue]
            elif id==39 or (id>=85 and id<=92) or id==103:
               return self.mem.colores.arr[TPlayers.Red]
            elif id==56 or (id>=93 and id<=100) or id==104:
               return self.mem.colores.arr[TPlayers.Green]
            else:
                return Color(255, 255, 255)            
                
        def defineRotatePN(id):
            """EStablece si debe rotar el panel numerico"""
            if id in (1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,  61, 62, 63, 64, 65, 66, 67, 68 ):
                return True
            return False
                 
        def defineRotate( id):
            if (id>=10 and id<=24) or (id>=77 and id<=83) or(id>=43 and id <=59) or (id>=93 and id<=100):
               return 90
            if id==60 or id==8 or id==76:
                return 180
            if id==9 or id==25 or id==84:
                return 270
            else:
                return 0        
                
        ## Swaps pawn coords in square when needed
        ## In Color Ramp we set first pawn opposite to initial square
        ## First coord inside route
        def swapPawnCoordsInSquare(c):
            if c.id in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 42, 43, 44, 45, 46, 47, 48, 49, 50, 60, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 92]:
                swap_list_with_two_items(c.pawncoords)
        ##############################       
        posCasillas=poscasillas4(self.number)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            c=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), defineRutas1(i))
            swapPawnCoordsInSquare(c)
            self.arr.append(c)

    def generar_casillas6(self):
        def defineRutas1(id):
            if id==5: return TPlayers.Yellow
            if id==22: return TPlayers.Blue
            if id==39: return TPlayers.Red
            if id==56: return TPlayers.Green
            if id==73: return TPlayers.Gray
            if id==90: return TPlayers.Fuchsia
            return -1
            
        def defineSeguro( id):           
            if id  in (5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68, 73, 80, 85, 90, 97, 102) or id>=103:
                return True
            else:
                return False
    
        def defineMaxFichas( id):
            if id>=151 or id in (110, 118, 126, 134, 142, 150):
                return 4
            else:
                return 2
    
        def defineRampaLlegada(id):
            if id>=103 and id<= 150:
               return True
            return False
    
        def defineTipo( id):
            if id>=151:
               return TSquareTypes.Initial6 #Casilla inicial
            elif id in  (110, 118, 126, 134, 142, 150):
               return TSquareTypes.Final6#Casilla final
            elif id==9 or  id==26 or  id==43 or  id==60 or id==77 or id==94:  
               return TSquareTypes.ObliqueLeft6 #Casilla oblicuai
            elif id==8 or  id==25 or  id==42 or  id==59 or id==76 or id==93:  
               return TSquareTypes.ObliqueRight6 #Casilla oblicuad
            else:
                return TSquareTypes.Normal #Casilla Normal
    
        def defineColor( id):
            if id==5 or (id>=103 and id<=110) or id==151:
               return self.mem.colores.arr[TPlayers.Yellow]
            elif id==22 or (id>=111 and id<=118) or id==152:
               return self.mem.colores.arr[TPlayers.Blue]
            elif id==39 or (id>=119 and id<=126) or id==153:
               return self.mem.colores.arr[TPlayers.Red]
            elif id==56 or (id>=127 and id<=134) or id==154:
               return self.mem.colores.arr[TPlayers.Green]
            elif id==73 or (id>=135 and id<=142) or id==155:
               return self.mem.colores.arr[TPlayers.Gray]
            elif id==90 or (id>=143 and id<=150) or id==156:
               return self.mem.colores.arr[TPlayers.Fuchsia]
            else:
                return Color(255, 255, 255)            
                                
        def defineRotatePN(id):
            """EStablece si debe rotar el panel numerico"""
            if id in(8, 9, 25, 26, 42, 43, 59, 60,  76, 77, 93, 94, 110, 111, 127, 128):
                return False
            return True
        def defineRotate( id):
            if id==154:
                return 30
            if (id>=10 and id<=24) or (id>=111 and id<=117)  or id in (60, 76, 142):
               return 60
            if id==155:
                return 90
            if(id>=27 and id<=41) or (id>=119 and id<=125) or id in (77, 93, 150):
                return 120
            if id==156:
                return 150
            if(id>=44 and id<=58) or (id>=127 and id<=133) or id in (8, 94, 110):
                return 180
            if(id>=61 and id<=75) or (id>=135 and id<=141) or id in (9, 25, 118):
                return 240
            if id==151:
                return 210
            if id==152:
                return 270
            if(id>=78 and id<=92) or (id>=143 and id<=149) or id in (26, 42, 126):
                return 300
            if id==153:
                return 330
            else:
                return 0        
        ## Swaps pawn coords in square when needed
        ## In Color Ramp we set first pawn opposite to initial square
        ## First coord inside route
        def swapPawnCoordsInSquare(c):
            if c.id in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 102, 103, 104, 105, 106, 107, 108, 109, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141]:
                swap_list_with_two_items(c.pawncoords)
        ##############################        
        posCasillas=poscasillas6(self.number)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            c=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), defineRutas1(i))
            swapPawnCoordsInSquare(c)
            self.arr.append(c)
 
    def generar_casillas8(self):
        def defineSeguro( id):
            if id  in (5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68, 73, 80, 85, 90, 97, 102, 107, 114, 119, 124, 131, 136) or id>=137:
                return True
            else:
                return False
    
        def defineMaxFichas( id):
            if id in (144, 152, 160, 168, 176, 184, 192, 200,  201, 202, 203, 204, 205, 206, 207, 208):
                return 4
            else:
                return 2
    
        def defineRampaLlegada(id):
            if id>=137 and id<= 200:
               return True
            return False
    
        def defineTipo( id):
            if id in (201, 202, 203, 204, 205, 206, 207, 208):
               return TSquareTypes.Initial8 #Casilla inicial
            elif id in (144, 152, 160, 168, 176, 184, 192, 200):
               return TSquareTypes.Final8 #Casilla final
            elif id in (9, 26, 43, 60, 77, 94, 111, 128):  
               return TSquareTypes.ObliqueLeft8 #Casilla oblicuai
            elif id in (8, 25, 42, 59, 76, 93, 110, 127):  
               return TSquareTypes.ObliqueRight8 #Casilla oblicuad
            else:
                return TSquareTypes.Normal #Casilla Normal
    
        def defineColor( id):
            if id in (5,  137, 138, 139, 140, 141, 142, 143, 144, 201) :
               return self.mem.colores.arr[TPlayers.Yellow]
            elif id in (22, 145, 146, 147, 148, 149, 150, 151, 152, 202):
               return self.mem.colores.arr[TPlayers.Blue]
            elif id in (39, 153, 154,  155, 156, 157, 158, 159, 160, 203) :
               return self.mem.colores.arr[TPlayers.Red]
            elif id in (56, 161, 162, 163, 164, 165, 166, 167, 168, 204):
               return self.mem.colores.arr[TPlayers.Green]
            elif id in (73, 169, 170, 171, 172, 173, 174, 175, 176, 205):
               return self.mem.colores.arr[TPlayers.Gray]
            elif id in (90, 177, 178, 179, 180, 181, 182, 183, 184, 206):
               return self.mem.colores.arr[TPlayers.Fuchsia]
            elif id in (107, 185, 186, 187, 188, 189, 190, 191, 192, 207) :
               return self.mem.colores.arr[TPlayers.Orange]
            elif id in (124, 193, 194, 195, 196, 197, 198, 199, 200, 208) :
               return self.mem.colores.arr[TPlayers.Turquoise]
            else:
                return Color(255, 255, 255)            
                
        def defineRotatePN(id):
            """EStablece si debe rotar el panel numerico"""
            if (id>=61 and id<=75) or id in(8, 9, 25, 26, 42, 43, 59, 60,  76, 77, 93, 94, 110, 111, 127, 128):
                return False
            return True
                    
        def defineRutas1(id):
            """Es igual para 4,6,8"""
            if id==5: return TPlayers.Yellow
            if id==22: return TPlayers.Blue
            if id==39: return TPlayers.Red
            if id==56: return TPlayers.Green
            if id==73: return TPlayers.Gray
            if id==90: return TPlayers.Fuchsia
            if id==107: return TPlayers.Orange
            if id==124: return TPlayers.Turquoise
            return -1
        
        def defineRotate( id):
            if id==205:
                return 22.5
            if (id>=10 and id<=24) or (id>=145 and id <=151) or id in (77, 93, 184):
                return 45
            if id==206:
                return 67.5
            if (id>=27 and id<=41) or (id>=153 and id <=159) or id in (94, 110, 192):
                return 90
            if id==207:
                return 112.5
            if (id>=44 and id<=58) or (id>=161 and id <=167)  or id in (111, 127, 200):
                return 135
            if id==208:
                return 157.5
            if id in (128, 8 ,144):
                return 180
            if id==201:
                return 202.5
            if (id>=78 and id<=92) or (id>=177 and id <=183) or id in(25,9, 152):
                return 225
            if id==202:
                return 247.5
            if (id>=94 and id<=109) or (id>=185 and id <=191) or id in (26, 42, 160  ):
                return 270
            if id==203:
                return 292.5
            if (id>=110 and id<=126) or (id>=193 and id <=199) or id in (43, 59, 168):
                return 315
            if id==204:
                return 337.5
            else:
                return 0        
        ## Swaps pawn coords in square when needed
        ## In Color Ramp we set first pawn opposite to initial square
        ## First coord inside route
        def swapPawnCoordsInSquare(c):
            if c.id in [ 
                1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 35, 36, 37, 38, 39, 40, 41,
                42, 43, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
                76, 77,
                85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 102, 103, 104, 105, 106, 107, 108, 109,  111,
                119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 
                177, 178, 179, 180, 181, 182, 183, 
                185, 186, 187, 188, 189, 190, 191, 
            ]:
                swap_list_with_two_items(c.pawncoords)
        ##############################        
        posCasillas=poscasillas8(self.number)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            c=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), defineRutas1(i))
            swapPawnCoordsInSquare(c)
            self.arr.append(c)

## Clase que agrupa fichas
class SetFichas(ObjectManager_With_Id):
    def __init__(self, mem):
        ObjectManager_With_Id.__init__(self)
        self.mem=mem
        
    ## Busca entre las fichas que pueden mover si alguna esta obligada a mover
    def algunaEstaObligada(self):
        for f in self.arr:
            if f.estaObligada(self.mem)==True:
                return True
        return False

    def algunaEstaAutorizadaAmover(self):
        if self.fichasAutorizadasAMover().length()>0:
            return True
        return False
        
    ## Devuelve un SetFichas con las autorizadas a mover
    def fichasAutorizadasAMover(self):
        """Devuelve un arr con las fichas que pueden mover"""
        resultado=SetFichas(self.mem)
        for f in self.arr:
            if f.estaAutorizadaAMover()[0]==True:
                resultado.append(f)
        return resultado        
    
    def TodasFichasEnCasa(self):
        for f in self.arr:
            if f.posruta!=0:
                return False
        return True        
        
    def TodasFichasFueraDeCasa(self):
        for f in self.arr:
            if f.posruta==0:
                return False
        return True
        
    ## Ordena las fichas por su posición en la ruta.
    def order_by_posruta(self, reverse=False):
        fichas=sorted(self.arr, key=lambda f:f.posruta,  reverse=reverse)
        del self.arr
        self.arr=fichas

    ## Ordena por el número de amenazas, calcula las amenazas al ordenar
    def order_by_numero_amenazas(self, reverse=False):
        fichas=sorted(self.arr, key=lambda f:f.amenazas().length(),  reverse=reverse)
        del self.arr
        self.arr=fichas
        
class Ficha(QObject):
    def __init__(self, mem, id, number,  color, jugador, ruta):
        """El identificador de la ficha viene dado por el nombre del color y el id (numero de creacion), se genera en la clase Mem"""
        QObject.__init__(self)
        self.color=color
        self.mem=mem
        self.id=id
        self.number=number#indice dentro de las fichas de mismo color.
        self.ruta=ruta
        self.posruta=0#Posición en la ruta
        self.jugador=jugador
        self.oglname=self.id#Nombre usado para pick por opengl

    def amenazas(self):
        return ThreatManager(self.mem, self, self.casilla())
        
        
    def amenazasDestino(self,  desplazamiento):
        if self.posruta+desplazamiento<self.ruta.length():
            return ThreatManager(self.mem,  self, self.ruta.arr[self.posruta+desplazamiento])
        else:
            print ("No se puede ver la amenaza destino de una ruta pasada")
        
    def __repr__(self):
        return  "Ficha {0} del jugador {1}".format(self.id, self.jugador.color.name)
        
    def estaObligada(self, mem):        
        """ESta pregunta se integra dentro de puede mover. NO DEBE HABER EN SETFICHAS ALGUNAS, YA QUE SE INTEGRARiA DENTRO DE ALGUNA PUEDEMOVER"""
        if self.puedeMover()[0]==False:
            return False
            
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.ruta.arr[1].buzon_numfichas()<2:
            return True
        
        #dos jugadore distintos en inicio entonces come
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.jugador.hayDosJugadoresDistintosEnRuta1():
            return True
        
        #Comprueba que no tenga obligacion de abrir barrera
        if self.jugador.tieneBarreras()==True  and self.jugador.tiradaturno.ultimoValor()==6:
            if self.casilla() in self.jugador.barreras():
                return True
        return False
        
    def estaAutorizadaAMover(self, posibledado=None, log=False):
        """PUEDE MOVER Y ESTA OBLIGADO SON DOS CONCEPTOS INDEPENDIENTES QUE NO DEBEN DE UNIRSE 
        PORQUE GENERA RECURSIVIDADPOR ESO SE HACE AQUi
        
        Autorizada significa que puede mover y no esta obligada a hacer otras cosas"""
        
        (puede, movimiento)=self.puedeMover(posibledado,  log)
        if puede:
            if self.mem.jugadores.actual.fichas.algunaEstaObligada() :
                if self.estaObligada(self.mem)==False:
                    if self.jugador.tiradaturno.ultimoValor()==5:
                        if log: self.mem.jugadores.actual.log(self.tr("No puede mover, porque debe sacar una ficha"))
                    else:
                        if log: self.mem.jugadores.actual.log(self.tr("No puede mover, porque debe abrir una barrera"))                        
                    return (False, 0)                    
            return (puede, movimiento)
        return (puede, movimiento)
        
    def puedeMover(self, posibledado=None,  log=False):
        """Comprueba si la ficha puede mover. desde el punto de vista fisico
        Si log=True muestra los logs
        
        posibledado
        """

        #Es ficha del jugador actual. #A PARTIR DE AQUI SE PUEDE USAR SELF.JUGADOR EN VEZ DE MEM.jugadores.actual
        if  self.jugador!=self.mem.jugadores.actual:             
            if log: self.mem.jugadores.actual.log(self.tr("No es del jugador actual"))
            return (False, 0)
            
        #No se puede mover una ficha que esta en casa con puntos acumulados
        if self.mem.jugadores.actual.movimientos_acumulados!=None and self.estaEnCasa():
            return (False, 0)

        #Calcula el movimiento
        if posibledado==None:
            dado=self.jugador.tiradaturno.ultimoValor()
        else:
            dado=posibledado
        
        
        if self.mem.jugadores.actual.movimientos_acumulados!=None:
            movimiento=self.mem.jugadores.actual.movimientos_acumulados
        elif self.estaEnCasa() and dado==5:   
            movimiento= 1
        elif self.estaEnCasa()==True and dado!=5: #Saco un 5
            movimiento=0
        elif self.jugador.fichas.TodasFichasFueraDeCasa()==True and dado==6:
            movimiento=7
        else:
            movimiento=dado
            
        #Caso posibledado con 10 y 20
            if posibledado in (10, 20):
                movimiento=posibledado
                            
        if movimiento==0 or movimiento==None:
            if log: self.mem.jugadores.actual.log(self.tr("No puede mover"))
            return (False, 0)    
           
        #se ha pasado la meta
        if self.posruta+movimiento>self.ruta.length()-1:
            if log: self.mem.jugadores.actual.log(self.tr("Se ha pasado la meta"))
            return (False, 0) 
            
        #Rastrea todas las casillas de paso en busca de barrera. desde la siguiente
        for i in range(self.posruta+1, self.posruta+movimiento+1): 
            if self.ruta.arr[i].tieneBarrera()==True:
                if log: self.mem.jugadores.actual.log(self.tr("Hay una barrera"))
                return (False, 0)

        #Comprueba si hay sitio libre
        casilladestino=self.ruta.arr[self.posruta+movimiento]
        if casilladestino.posicionLibreEnBuzon()==-1:
            if self.jugador.hayDosJugadoresDistintosEnRuta1():#COmprueeba si es primera casilla en ruta y hay otra de otro color.
                if log: self.mem.jugadores.actual.log(self.tr("Obligado a sacar y a comer"))
            else:
                if log: self.mem.jugadores.actual.log(self.tr("No hay espacio en la casilla"))
                return (False, 0)
        return (True, movimiento)
        
    def mover(self, ruta, controllastficha=True,  startgame=False):
        casillaorigen=self.ruta.arr[self.posruta]
        casilladestino=self.ruta.arr[ruta]        
        self.posruta=ruta
        if controllastficha==True:
            self.jugador.LastFichaMovida=self
        if startgame==False:
            casillaorigen.buzon_remove(self)
        casilladestino.buzon_append(self)
    
        
    def opengl(self, qglwidget, qcolor):
        glPushMatrix()
        ficha=gluNewQuadric();
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, qglwidget.texture(TTextures.Wood))
        gluQuadricDrawStyle (ficha, GLU_FILL);
        gluQuadricNormals (ficha, GLU_SMOOTH);
        gluQuadricTexture (ficha, True);
        qglwidget.qglColor(QColor(255, 255, 255))
        gluCylinder (ficha, 1.4, 1.4, 0.2, 16, 5)
        glTranslated(0, 0, 0.2)
        qglwidget.qglColor(qcolor)
        gluDisk(ficha, 0, 1.4, 16, 5)
        glTranslated(0, 0, -0.2)
        glRotated(180, 1, 0, 0)# da la vuelta a la cara
        qglwidget.qglColor(QColor(127, 127, 127))
        gluDisk(ficha, 0, 1.40, 16, 5)
        glPopMatrix()
        glDisable(GL_TEXTURE_2D);
        
    def puedeComer(self, mem, destposruta):
        """Devuelve un (True, ficha a comer) or (False, None) si puede comer una ficha en la posicion ruta"""
        #Controla que la casilla de destino no sobrepase la ruta
        if destposruta>self.ruta.length()-1:
            return (False, None)
            
        casilladestino=self.casilla(destposruta)
        fichasdestino=casilladestino.buzon_fichas()
        #debe estar primero porque es una casilla segura
        if self.posruta==0 and self.jugador.tiradaturno.ultimoValor()==5 and casilladestino.buzon_numfichas()==2:                
            #Las dos fichas son del jugador actual
            if mem.jugadores.actual==fichasdestino[0][1].jugador and mem.jugadores.actual==fichasdestino[1][1].jugador:
                print ("igual0,igual1")
                return (False, None)
            elif mem.jugadores.actual==fichasdestino[0][1].jugador and mem.jugadores.actual!=fichasdestino[1][1].jugador:
                print ("igual0,noigual1")
                return (True, fichasdestino[1][1])
            elif mem.jugadores.actual!=fichasdestino[0][1].jugador and mem.jugadores.actual==fichasdestino[1][1].jugador:
                print ("noigual0,igual1")
                return (True, fichasdestino[0][1])
            else: #Las dos son distintas se escoge la ultima que entro
                print ("noigual0,noigual1")
                return (True, casilladestino.UltimaFichaEnLlegar)
                
        if casilladestino.seguro==True:
            return (False, None)
        
        if len(fichasdestino)==1:#Todavia no se ha movido
            if fichasdestino[0][1].jugador!=mem.jugadores.actual:
                return(True, fichasdestino[0][1])

        return (False, None)
                
                
    def come(self, mem,   ruta):
        """ruta, es la posicion de ruta de ficha en la que come. No se ha movido antes, come si puede y devuelve True, en caso contrario False"""
        (puede, fichaacomer)=self.puedeComer(mem, ruta)
        if puede==True:
            fichaacomer.mover(0, False)
            if self.posruta==0:
                self.mover(1, True)
            else:
                self.mover(ruta, True)
            mem.jugadores.actual.movimientos_acumulados=20
            mem.jugadores.actual.log(self.tr('He comido una ficha de {0} en la casilla {1}'.format(fichaacomer.jugador.name, self.casilla(ruta).id)))
            self.jugador.comidaspormi=self.jugador.comidaspormi+1
            fichaacomer.jugador.comidasporotro=fichaacomer.jugador.comidasporotro+1
            return True
        return False

    def puedeMeter(self, posruta):
        """Devuelve un booleano si puede meter la ficha en las casilla final"""
        if posruta==len(self.ruta.arr)-1:
            return True
        return False
        
    def mete(self, posruta):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""      
        if self.puedeMeter(posruta):
            self.mover(posruta, True)
            self.jugador.movimientos_acumulados=10
            self.jugador.log(self.tr("Una ficha ha llegado a la meta"))
            return True
        return False

    def casilla(self,  posruta=None):
        """Devuelve el objeto casilla en el que se encuentra la ficha
        Si se le pasa el parametro devuelve la casilla de la ruta de la ficha, en la posicion posruta"""
        if posruta==None:
            posruta=self.posruta
        return self.ruta.arr[posruta]

    def casillasPorMover(self):
        return self.ruta.length()-self.posruta
        
    ##Devuelve un booleano, segun la ficha este o no a tiro de llegada, es decir a 1,2,3,4,5,6,7
    def estaATiroDeLlegada(self ):
        if self.posruta in (self.ruta.squareFinalPosition()-1,  self.ruta.squareFinalPosition()-2,  self.ruta.squareFinalPosition()-3,  self.ruta.squareFinalPosition()-4,  self.ruta.squareFinalPosition()-5):
            return True
        if self.posruta==self.ruta.squareFinalPosition()-6 and self.jugador.tieneFichasEnCasa()==True:
            return True
        if self.posruta==self.ruta.squareFinalPosition()-7 and self.jugador.tieneFichasEnCasa()==False:
            return True
        return False
        
    def estaEnCasa(self):
        if self.posruta==0:
            return True
        return False

    def estaEnMeta(self):
        if self.posruta==self.ruta.squareFinalPosition():
            return True
        return False

    ## Used in frmAbout
    def draw(self, qglwidget):
        glPushName(self.id)
        glPushMatrix()
        p=(0, 0, 0)
        glTranslated(p[0], p[1], p[2])
        
        self.opengl(qglwidget, self.color.qcolor())
        glPopMatrix()
        glPopName()


class AbstractOpenglObject(ABC):
    def __init__(self, parent=None):
        self.__position=Coord3D(0, 0, 0)
        self.__color=Color(255, 255, 255, "white")
        self.__pickname=None
        
    @property
    def position(self):
        return self.__position
        
    ## Setter of position property
    ## @param value to assign to the property. Value is Coord3D object
    @position.setter
    def position(self, value):
        self.__position=value
            
    @property
    def color(self):
        return self.__color
        
    ## Setter of color property
    ## @param value to assign to the property. Value is Color object
    @color.setter
    def color(self, value):
        self.__color=value
            
    @property
    def pickname(self):
        return self.__pickname
        
    ## Setter of pickname property
    ## @param value to assign to the property. Value is a TNames property
    @pickname.setter
    def pickname(self, value):
        self.__pickname=value
        
    ## Opengl Dra function
    @abstractmethod
    def draw(self):
        pass
        
        

## Class to draw 3 player board
class Tablero3(AbstractOpenglObject):
    def __init__(self, parent=None):
        AbstractOpenglObject.__init__(self, parent)
        self.pickname=32
        self.color=Color(88, 40, 0)

    def draw(self, qglwidget): 
        pi_3=pi/3#60º
        sin_pi_3=sin(pi_3)
        cos_pi_3=cos(pi_3)
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        
        glTranslated(self.position.x,  self.position.y,  self.position.z)
        z=0
        qglwidget.qglColor(self.color.qcolor())
        #Scaling and translating
        glScaled(1.03, 1.03, 1.03)
        glTranslated(-0.9, -0.95, 0)
        verts=[     Coord3D(21, 63, z), #Clock wise
                        Coord3D(42, 63, z), 
                        Coord3D(42+24*sin_pi_3, 39-24*cos_pi_3, z), 
                        Coord3D(42+24*sin_pi_3-21*cos_pi_3, 39-24*cos_pi_3-21*sin_pi_3, z), 
                        Coord3D(42+24*sin_pi_3-21*cos_pi_3-2*24*sin_pi_3, 39-24*cos_pi_3-21*sin_pi_3, z), 
                        Coord3D(21-24*sin_pi_3, 39-24*cos_pi_3, z)]
        texverts=[Coord2D(0, 0),Coord2D(1, 0), Coord2D(1, 0.5), Coord2D(1, 1) , Coord2D(0.5, 1),  Coord2D(0, 0.5) ]
        p=Polygon().init__create(verts, self.color, TTextures.Wood, texverts)
        prism=Prism(p, 0.5)
        prism.opengl(qglwidget)
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)    



## Class to draw 4 player board
class Tablero4(AbstractOpenglObject):
    def __init__(self, parent=None):
        AbstractOpenglObject.__init__(self, parent)
        self.position=Coord3D(-1, -1, 0)
        self.pickname=32
        self.color=Color(88, 40, 0)

    def draw(self, qglwidget): 
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        glTranslated(self.position.x,  self.position.y,  self.position.z)
        verts=[Coord3D(0, 0, 0), Coord3D(0, 65, 0), Coord3D(65, 65, 0), Coord3D(65, 0, 0)]
        texverts=[Coord2D(0, 0),Coord2D(0, 1), Coord2D(1, 1), Coord2D(1, 0) ]
        p=Polygon().init__create(verts, self.color, TTextures.Wood, texverts)
        prism=Prism(p, 0.5)
        prism.opengl(qglwidget)
        glDisable(GL_TEXTURE_2D)    
        glPopMatrix()

## Class to draw 6 player board
class Tablero6(AbstractOpenglObject):
    def __init__(self, parent=None):
        AbstractOpenglObject.__init__(self, parent)
        self.position=Coord3D(31.5, 23.85, 0)
        self.pickname=TNames.Board
        self.colorbrown=Color(88, 40, 0)

    def draw(self, qglwidget): 
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        glTranslated(self.position.x,  self.position.y,  self.position.z)
        p=Polygon().init__regular(6, 47, self.colorbrown, TTextures.Wood)
        prism=Prism(p, 0.5)
        prism.opengl(qglwidget)
        glDisable(GL_TEXTURE_2D)    
        glPopMatrix()        

## Class to draw 8 player board
class Tablero8(AbstractOpenglObject):
    def __init__(self, parent=None):
        AbstractOpenglObject.__init__(self, parent)
        self.position=Coord3D(31.5, 16.5, 0)
        self.pickname=32#Nombre usado para pick por opengl
        self.color=Color(88, 40, 0)

    def draw(self, qglwidget): 
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        glTranslated(self.position.x,  self.position.y,  self.position.z)
        p=Polygon().init__regular(8, 52.5, self.color, TTextures.Wood)
        prism=Prism(p, 0.5)
        prism.opengl(qglwidget)
        glDisable(GL_TEXTURE_2D)     
        glPopMatrix()       
        
class Circulo:
    """Es el circulo publico por el que se mueven las fichas y pueden comerse entre ellas
    Es un array de casillas ordenado. que se repite ciclicamente
    numcasillas=68 para 4 jugadores"""
    def __init__(self, mem, numcasillas):
        self.arr=[]
        self.numcasillas=numcasillas
        for i in range(1, self.numcasillas+1):
            self.arr.append(mem.casillas.find_by_id(i))
    
    def casilla(self, posicion,  desplazamiento):
        """Calcula la casilla del circulo que tiene un desplazamiento positivo (hacia adelante) o negativo (hacia atras) 
        de la casilla cuya posicion (id de la casilla) se ha dado como parametro"""
        if posicion<1 or posicion>self.numcasillas:   #Si no esta en el circulo
            return None
            
        destino=posicion-1+desplazamiento
        if destino<0:
            destino=self.numcasillas+destino
        if destino>self.numcasillas-1:
            destino=destino-self.numcasillas
        return self.arr[destino]
        
class Color:
    def __init__(self,   r,  g, b, name=None):
        self.name=name
        self.r=r
        self.g=g
        self.b=b
    def glcolor(self):
        glColor3d(self.r, self.g, self.b)
        
    def qcolor(self):
        return QColor(self.r, self.g, self.b, 125)
        
    def dark(self):
        """Suma al color el incremento"""
        inc=30
        dark=Color(self.r-inc, self.g-inc,  self.b-inc)
        if dark.r<0: dark.r=0
        if dark.g<0: dark.g=0
        if dark.b<0: dark.b=0
        return dark
    
    def arraycolor(self,  size):
        """Returns and array of the seame color, poliedros."""
        arr=[]
        for i in range(size):
            arr.append(self)
        return arr
        
    def clone(self):
        return (Color(self.r, self.g, self.b, self.name))
    
    def compatibilityName(self,  color):
        #Debera desaparecer el tres versiones despues de 20130228
        if color=="gray":
            return "dimgray"
        elif color=="pink":
            return "fuchsia"
        elif color=="orange":
            return "darkorange"
        elif color=="cyan":
            return "darkturquoise"
        return color
            
    def qicon(self):
        ico = QIcon()
        ico.addPixmap(self.qpixmap(), QIcon.Normal, QIcon.Off) 
        return ico
    
    def qpixmap(self):
        """Devuelve un pixmap del color de la ficha"""
        if self.name=="yellow":
            return QPixmap(":/glparchis/fichaamarilla.png")
        elif self.name=="blue":
            return QPixmap(":/glparchis/fichaazul.png")
        elif self.name=="green":
            return QPixmap(":/glparchis/fichaverde.png")
        elif self.name=="red":
            return QPixmap(":/glparchis/ficharoja.png")
        elif self.name=="dimgray":
            return QPixmap(":/glparchis/fichagris.png")
        elif self.name=="fuchsia":
            return QPixmap(":/glparchis/ficharosa.png")
        elif self.name=="darkorange":
            return QPixmap(":/glparchis/fichanaranja.png")
        elif self.name=="darkturquoise":
            return QPixmap(":/glparchis/fichacyan.png")




class Coord3D:
    def __init__(self, x=0, y=0, z=0):
        """
            Contructs the object. If not parametes x,y,x =0
        """
        self.x=x
        self.y=y
        self.z=z

    def clone(self):
        """Returns other object with the same Coord"""
        return Coord3D(self.x, self.y,  self.z)
        
    def sum_z(self, n):
        """Suma un valor a la z y devuelve el objeto mismo syou"""
        self.z=self.z+n
        return self

class Coord2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def clone(self):
        """Returns other object with the same Coord"""
        return(Coord2D(self.x, self.y))


class Polygon:
    """
        Un quad es un polygon de cuatro vertices.
        Cumplen la regla del sacacorchos para la orientaci´on
        Cuando se vaya a hacer un prisma el poligono que se pone como par´ametro es de abajo, y va en sentido de las agujas del reloj
    """
    def __init__(self):
        """
            verts. Array de Coord3D
            color: Color del poligono is a Color object
            texture: Textura del pol´igno que es un TTextures value. Si no tiene debe valer None
            texCoord: Array de Coord2D de la textura
        """
        self.verts=None
        self.color=None
        self.texture=None
        self.texverts=None
        
    def init__create(self, verts, color,  texture, texverts):
        """
            verts. Array de Coord3D
            color: Color del poligono is a Color object
            texture: Textura del pol´igno que es un TTextures value.
            texCoord: Array de Coord2D de la textura
        """
        self.verts=verts
        self.color=color
        self.texture=texture
        self.texverts=texverts
        return self
    
    def init__regular(self, lados, radius, color, texture):
        """
            position es el centro del hex´agono en su base inferior
            reversed used to see from up in opengl
            Returns hexagon vertices
            texture: Textura del pol´igno que es un TTextures value.
            color: Color del poligono is a Color object
        """
        texverts=[]
        verts=[]
        for i in range(lados):#Reversed to see from up in opengl.
            posx=sin(i/lados*2*pi+pi/lados)
            posy=cos(i/lados*2*pi+pi/lados)
            if texture:
                texverts.append(Coord2D(posx, posy))
            verts.append(Coord3D(posx*radius, posy*radius, 0))
        return self.init__create(verts, color, texture, texverts)

    def clone(self):
        p=Polygon()
        verts=[]
        texverts=[]
        for i in range(len(self.verts)):
            verts.append(self.verts[i].clone())
            if self.texture:
                texverts.append(self.texverts[i].clone())
        return p.init__create(verts, Color(self.color.r, self.color.g, self.color.b, self.color.name), self.texture, texverts)
        
    def reverse(self):
        """
            Returns an array with reversed item, buy it doesn't change self.verts order
        """
        r=[]
        for vert in reversed(self.verts):
            r.append(vert)
        return r
        
    def opengl(self, qglwidget):
        """
            glEnable(GL_TEXTURE_2D) must be declared and closed outside
        """
        glPushMatrix()
        if self.texture:
            glEnable(GL_TEXTURE_2D);
            glBindTexture(GL_TEXTURE_2D, qglwidget.texture(self.texture))   
        qglwidget.qglColor(self.color.qcolor())
        glBegin(GL_POLYGON)
        for i, v in enumerate(self.verts):
            if self.texture:
                glTexCoord2f(self.texverts[i].x, self.texverts[i].y)
            glVertex3d(v.x, v.y, v.z)
        glEnd()
        if self.texture:
            glDisable(GL_TEXTURE_2D);
        glPopMatrix()
        
    def translate_z(self, n):
        for v in self.verts:
            v.z=v.z+n
            
    def opengl_border(self, qglwidget, z=0.001):
        """
            Draws a polygon border
            with the z position desplaced as z parameter sets
        """
        glBegin(GL_LINE_LOOP)
        glColor3d(0, 0, 0)
        for i, v in enumerate(self.verts):
            glVertex3d(v.x, v.y, v.z+z)
        glEnd()

class Prism:
    """Prisma"""
    def __init__(self,  poligon, height):
        """
            Genera un prisma a  partir del poligono
        """
        self.height=height
        
        self.bottom=poligon
        
        self.up=self.bottom.clone()
        self.up.translate_z(height)
        self.up.verts=self.up.reverse()
        
        self.bottom.color=Color(127, 127, 127, "Bottom")#Must be after cloning to mantein original color
        
        self.contour=[] #Poligon array to set contour
        #HAy que re - reverse
        rere=self.up.clone()
        rere.verts=rere.reverse()
        for i, v in enumerate(self.up.verts):#Laterales
            pverts=[]
            texverts=[Coord2D(0, 0),Coord2D(1, 0), Coord2D(1, 1), Coord2D(0, 1) ]
            pverts.append(rere.verts[i].clone())
            pverts.append(rere.verts[(i+1) % len(rere.verts)].clone())
            pverts.append(self.bottom.verts[(i+1) % len(self.bottom.verts)].clone())
            pverts.append(self.bottom.verts[i].clone())
            self.contour.append(Polygon().init__create(pverts, Color(200, 200, 200), self.bottom.texture, texverts))
        
        
        
    def opengl(self, qglwidget):
        self.up.opengl(qglwidget)
        self.bottom.opengl(qglwidget)
        for f in self.contour:
            f.opengl(qglwidget)
            
    def opengl_border(self, qglwidget, face=None):
        """
            Face is an Integer 
            Face 0: up
            Face 1: down
            Face n, donde n numero vertices.
        """
        if face==None:
            self.up.opengl_border(qglwidget)
            self.bottom.opengl_border(qglwidget)
            for f in self.contour:
                f.opengl_border(qglwidget)
        else:
            zpos=0.201
            if face==0:
                self.up.opengl_border(qglwidget, zpos)
            elif face==1:
                self.bottom.opengl_border(qglwidget, zpos)


        

## Square object where pawns objects are displayed
## Manage pawns and its drawings
class Casilla(QObject):    
    def __init__(self, id, maxfichas, color,  position, rotate, rotatepn,  rampallegada, tipo, seguro, ruta1):
        QObject.__init__(self)
        self.id=id
        self.maxfichas=maxfichas
        self.color=color
        self.position=position
        self.rotate=rotate
        self.rotatepn=rotatepn #Rotar panel numerico
        self.rampallegada=rampallegada#booleano que indica si la casilla es de rampa de llegada
        
        ##Define a que jugador id pertenece la casilla si es la primera casilla de la ruta. Devuelve el id del jugador o -1, si no es ruta 1
        self.ruta1=ruta1
        self.tipo=tipo
        self.seguro=seguro# No se debe usar directamente ya que en ruta 1 solo es seguro si el jugador no tiene en casa
        self.buzon=[None]*self.maxfichas #Se crean los huecos y se juega con ellos para mantener la posicion
        self.oglname=self.id+34#Nombre usado para pick por opengl
        self.UltimaFichaEnLlegar=None#Puntero a un objeto ficha que es utilizado p.e. cuando se come la segunda ficha en la casilla de salida por un 5 obligado a salir
        
        ## Where to put pawns positions
        self.pawncoords=[]
        self.__setPawnCoordsInSquare()
    
    ## Sets Pawn positions in a square. Object ManagerPawnsSquare was created in Casilla constructor
    def __setPawnCoordsInSquare(self):
        if self.tipo==TSquareTypes.Normal:
            self.pawncoords.append(Coord3D(1.8, 1.5, 0.2))
            self.pawncoords.append(Coord3D(5.2, 1.5, 0.2))
        #Oblique Left
        elif self.tipo==TSquareTypes.ObliqueLeft4:
            self.pawncoords.append(Coord3D(3.5, 1.5, 0.2))
            self.pawncoords.append(Coord3D(5.6, 1.5, 0.2))
        elif self.tipo==TSquareTypes.ObliqueLeft6:
            self.pawncoords.append(Coord3D(2.6, 1.5, 0.2))
            self.pawncoords.append(Coord3D(5.4, 1.5, 0.2))
        elif self.tipo==TSquareTypes.ObliqueLeft8:
            self.pawncoords.append(Coord3D(2.3, 1.5, 0.2))
            self.pawncoords.append(Coord3D(5.2, 1.5, 0.2))
        #Oblique Right
        elif self.tipo==TSquareTypes.ObliqueRight4:
            self.pawncoords.append(Coord3D(3.5, 1.5, 0.2))
            self.pawncoords.append(Coord3D(1.4, 1.5, 0.2))
        elif self.tipo==TSquareTypes.ObliqueRight6:
            self.pawncoords.append(Coord3D(4.4, 1.5, 0.2))
            self.pawncoords.append(Coord3D(1.6, 1.5, 0.2))
        elif self.tipo==TSquareTypes.ObliqueRight8:
            self.pawncoords.append(Coord3D(4.7, 1.5, 0.2))
            self.pawncoords.append(Coord3D(1.8, 1.5, 0.2))
        #Initial
        elif self.tipo==TSquareTypes.Initial3:
            self.pawncoords.append(Coord3D(-1.8, 10.5, 0.2))
            self.pawncoords.append(Coord3D(-3.3, 7.5, 0.2))
            self.pawncoords.append(Coord3D(-4.7, 4.5, 0.2))
            self.pawncoords.append(Coord3D(-6.2, 1.5, 0.2))
        elif self.tipo==TSquareTypes.Initial4:
            self.pawncoords.append(Coord3D(7, 7, 0.2))
            self.pawncoords.append(Coord3D(14, 7, 0.2))
            self.pawncoords.append(Coord3D(14, 14, 0.2))
            self.pawncoords.append(Coord3D(7, 14, 0.2))
        elif self.tipo==TSquareTypes.Initial6:
            self.pawncoords.append(Coord3D(0, -8, 0.2))
            self.pawncoords.append(Coord3D(0, -11, 0.2))
            self.pawncoords.append(Coord3D(0, -14, 0.2))
            self.pawncoords.append(Coord3D(0, -17, 0.2))
        elif self.tipo==TSquareTypes.Initial8:
            self.pawncoords.append(Coord3D(8, 1, 0.2))
            self.pawncoords.append(Coord3D(8, 4, 0.2))
            self.pawncoords.append(Coord3D(8, 7, 0.2))
            self.pawncoords.append(Coord3D(8, 10, 0.2))
        elif self.tipo==TSquareTypes.Final3:
            self.pawncoords.append(Coord3D(6, 1.6, 0.2))
            self.pawncoords.append(Coord3D(9, 1.6, 0.2))
            self.pawncoords.append(Coord3D(12,  1.6, 0.2))
            self.pawncoords.append(Coord3D(15, 1.6, 0.2))
        elif self.tipo==TSquareTypes.Final4:
            self.pawncoords.append(Coord3D(10.5, 2, 0.2))
            self.pawncoords.append(Coord3D(4.5, 2, 0.2))
            self.pawncoords.append(Coord3D(7.5, 2, 0.2))
            self.pawncoords.append(Coord3D(7.5, 5, 0.2))
        elif self.tipo==TSquareTypes.Final6:
            self.pawncoords.append(Coord3D(3.6, 2.3, 0.2))
            self.pawncoords.append(Coord3D(7.2, 2.3, 0.2))
            self.pawncoords.append(Coord3D(10.8, 2.3, 0.2))
            self.pawncoords.append(Coord3D(14.4, 2.3, 0.2))
        elif self.tipo==TSquareTypes.Final8:
            self.pawncoords.append(Coord3D(3.3, 2.5, 0.2))
            self.pawncoords.append(Coord3D(6.8, 2.5, 0.2))
            self.pawncoords.append(Coord3D(10.3,  2.5, 0.2))
            self.pawncoords.append(Coord3D(13.8,  2.5, 0.2))

            
    def __repr__(self):
        return ("Casilla {0} con {1} fichas dentro".format(self.id, self.buzon_numfichas()))

    def esSegura(self, mem,  jugador, beforemove=True):
        """Devuelve si la casilla es segura para el jugador pasado como parametro ante un posible moviiento,
        esta funcion mezcla el concepto ruta y seguro dependiendo del numero de fichas
        
        Busca segun beforemove antes de mover ficha, es decir es seguro con 0 fichas, o aftermove seguro con 1 ficha"""
        if self.ruta1!=-1:
            propietario=mem.jugadores.arr[self.ruta1]
            if jugador==propietario:
                return True
            else:#color distinto
                if beforemove==True:
                    if propietario.tieneFichasEnCasa() and self.buzon_numfichas()==0:
                        return False
                    else:
                        return True
                else:#beforemove=False
                    if propietario.tieneFichasEnCasa() and self.buzon_numfichas()==1:
                        return False
                    else:
                        return True
        else:   
            if self.seguro==True:
                return True
            else:
                return False
            

    def draw(self, qglwidget):
        def panelnumerico():
            def cuadrito(x, texture, rotation):
                glBindTexture(GL_TEXTURE_2D, texture)                
                glPushMatrix()
                glTranslated(self.position[0],self.position[1],self.position[2]+0.12)#Sets position
                glRotated(self.rotate, 0, 0, 1 )            
                glBegin(GL_QUADS)
                qglwidget.qglColor(self.color.qcolor())
                if rotation==0:
                    glTexCoord2f(0.0,0.0)
                    glVertex3d(x, 1, 0.10)
                    glTexCoord2f(1.0,0.0)
                    glVertex3d(x+1, 1, 0.10)
                    glTexCoord2f(1.0,1.0)
                    glVertex3d(x+1, 2, 0.10)
                    glTexCoord2f(0.0,1.0)
                    glVertex3d(x, 2, 0.10)
                else:
                    glTexCoord2f(0.0,0.0)
                    glVertex3d(x+1, 2, 0.10)
                    glTexCoord2f(1.0,0.0)
                    glVertex3d(x, 2, 0.10)
                    glTexCoord2f(1.0,1.0)
                    glVertex3d(x, 1, 0.10)
                    glTexCoord2f(0.0,1.0)
                    glVertex3d(x+1, 1, 0.10)
                glEnd()
                glPopMatrix()
            ################################
            if self.seguro==True:
                return
            #Cada cuadrante estara a 3x7 estara a 1x1 de ancho
            if len(str(self.id))==1:
                primero=int(str(self.id)[0])
            if len(str(self.id))==2:
                primero=int(str(self.id)[0])
                segundo=int(str(self.id)[1])
            if len(str(self.id))==3:
                primero=int(str(self.id)[0])
                segundo=int(str(self.id)[1])
                tercero=int(str(self.id)[2])
            
            #dos cuadrantes
            if self.rotatepn==True and len(str(self.id))==2:
                rotation=180
                tmp=primero
                primero=segundo
                segundo=tmp
            elif self.rotatepn==True and len(str(self.id))==1:
                rotation=180
            elif self.rotatepn==True and len(str(self.id))==3:
                rotation=180
                tmp=primero
                primero=tercero
                tercero=tmp
            else:
                rotation=0
            
            glEnable(GL_TEXTURE_2D);
            #PRIMERO
            if len(str(self.id))==1:
                cuadrito(3, qglwidget.texNumeros[primero], rotation)
            elif len(str(self.id))==2:
                cuadrito(2.5, qglwidget.texNumeros[primero], rotation)
                cuadrito(3.5, qglwidget.texNumeros[segundo], rotation)
            elif len(str(self.id))==3:
                cuadrito(2, qglwidget.texNumeros[primero], rotation)
                cuadrito(3, qglwidget.texNumeros[segundo], rotation)
                cuadrito(4, qglwidget.texNumeros[tercero], rotation)
                
            glDisable(GL_TEXTURE_2D);
            
        def tipo_inicio3():        
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(-24*sin(pi/3), -24*cos(pi/3), 0),  Coord3D(0, 24, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName();
            draw_fichas()
            glPopMatrix()

        def tipo_inicio4():        
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 21, 0), Coord3D(21, 21, 0), Coord3D(21, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName()
            draw_fichas()
            glPopMatrix()
            
        def draw_fichas():
            #Draws pawns with  ManagerPawnsSquare(ManagerPawns) information
            for position_in_buzon, ficha in enumerate(self.buzon):
                if ficha!=None:
                    glPushName(ficha.id)
                    glTranslated(self.pawncoords[position_in_buzon].x,  self.pawncoords[position_in_buzon].y, self.pawncoords[position_in_buzon].z)
                    ficha.opengl(qglwidget, ficha.color.qcolor())
                    glTranslated(-self.pawncoords[position_in_buzon].x,  -self.pawncoords[position_in_buzon].y, -self.pawncoords[position_in_buzon].z)
                    glPopName()
            
        def tipo_inicio6():        
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            b=21*sin(pi/6)
            c=21*tan(pi/6)*sin(pi/6)
            d=21*cos(pi/6)
            verts=[ Coord3D(0, 0, 0), Coord3D(b, -d, 0), Coord3D(0, -c-d, 0), Coord3D (-b, -d, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)     
            glPopName();
            draw_fichas()
            glPopMatrix()

        def tipo_inicio8():        
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            a22c5=pi/8
            a=21*sin(a22c5)
            c=21*tan(a22c5)*sin(a22c5)
            h=21/cos(a22c5)
            verts=[ Coord3D(a, h-c, 0), Coord3D(2*a, 0, 0), Coord3D(a, -c, 0), Coord3D(0, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)# 0 It's prism upper face
            glPopName();
            draw_fichas()
            glPopMatrix()  
    
        def tipo_normal():
            """
                Puede haber varios pushmatrix y popmatrix, como este caso con el panelnumerico
                El Pushname abarca todo.
            """
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )            
            verts=[Coord3D(0, 0, 0), Coord3D(0, 3, 0), Coord3D(7, 3, 0), Coord3D(7, 0, 0)]
            texverts=[Coord2D(0, 0),Coord2D(0, 1), Coord2D(1, 1), Coord2D(1, 0) ]
            if self.seguro==True and self.rampallegada==False:
                glEnable(GL_TEXTURE_2D);
                p=Polygon().init__create(verts, self.color, TTextures.Sure, texverts)
            else:
                p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            if self.seguro==True and self.rampallegada==False:
                glDisable(GL_TEXTURE_2D)
            glPopName();
            draw_fichas()
            glPopMatrix()
            panelnumerico()
    
        def tipo_oblicuoi(lado):
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            verts=[Coord3D(0, 0, 0), Coord3D(lado, 3, 0), Coord3D(7, 3, 0), Coord3D(7, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)  
            glPopName();
            draw_fichas()
            glPopMatrix()
            panelnumerico()
    
        def tipo_oblicuod(lado):
            """Como parametro se recibe el lado recortado"""
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 3, 0), Coord3D(lado, 3, 0), Coord3D(7, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName();
            draw_fichas()
            glPopMatrix()
            panelnumerico()

        def tipo_oblicuoi4():
            tipo_oblicuoi(3)
        def tipo_oblicuoi6():
            tipo_oblicuoi(3.0/tan(pi/3))
        def tipo_oblicuoi8():
            tipo_oblicuoi(3.0*tan(pi/8))
        def tipo_oblicuod4():
            tipo_oblicuod(4)
        def tipo_oblicuod6():
            tipo_oblicuod(7-3.0/tan(pi/3))
        def tipo_oblicuod8():
            tipo_oblicuod(7-3.0*tan(pi/8))

        def tipo_final3():
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(10.50, 10.5*tan(pi/6), 0), Coord3D(21, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName();
            draw_fichas()
            glPopMatrix()
        def tipo_final4():
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(7.5, 7.5, 0), Coord3D(15, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName();
            draw_fichas()
            glPopMatrix()

        def tipo_final6():
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            x=2*tan(pi/6)*(21*cos(pi/6)-3)/15
            y=(21*cos(pi/6)-3)/7.5
            verts=[Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(x*7.5, y*7.5, 0), Coord3D(x*15, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            draw_fichas()
            glPopMatrix()
            glPopName()

        def tipo_final8():
            rad67_5=67.5*2*pi/360#67.5º =45+67.5+67.5
            sin_rad67_5=sin(rad67_5)
            cos_rad67_5=cos(rad67_5)
            tg_rad67_5=sin_rad67_5/cos_rad67_5
            sin_pi_4=sin(pi/4)
            glPushName(self.oglname);
            glPushMatrix()
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            verts=[Coord3D(0, 0, 0), Coord3D(0, 0, 0), Coord3D(21/2-3/tg_rad67_5,  -3+21*sin_pi_4 +10.5, 0), Coord3D(21-3/tg_rad67_5*2, 0, 0)]
            p=Polygon().init__create(verts, self.color, None, [])
            prism=Prism(p, 0.2)
            prism.opengl(qglwidget)
            prism.opengl_border(qglwidget, 1)    
            glPopName();
            draw_fichas()
            glPopMatrix()

        ##################################        
        if self.tipo==TSquareTypes.Initial4:
            tipo_inicio4()
        elif self.tipo==TSquareTypes.Initial3:
            tipo_inicio3()
        elif self.tipo==TSquareTypes.Initial6:
            tipo_inicio6()
        elif self.tipo==TSquareTypes.Initial8:
            tipo_inicio8()
        elif self.tipo==TSquareTypes.Final3:
            tipo_final3()
        elif self.tipo==TSquareTypes.Final4:
            tipo_final4()
        elif self.tipo==TSquareTypes.Final6:
            tipo_final6()
        elif self.tipo==TSquareTypes.Final8:
            tipo_final8()
        elif self.tipo==TSquareTypes.ObliqueLeft4:
            tipo_oblicuoi4()
        elif self.tipo==TSquareTypes.ObliqueLeft6:
            tipo_oblicuoi6()
        elif self.tipo==TSquareTypes.ObliqueLeft8:
            tipo_oblicuoi8()
        elif self.tipo==TSquareTypes.ObliqueRight4:
            tipo_oblicuod4()
        elif self.tipo==TSquareTypes.ObliqueRight6:
            tipo_oblicuod6()
        elif self.tipo==TSquareTypes.ObliqueRight8:
            tipo_oblicuod8()
        else:
            tipo_normal()

    def tieneBarrera(self):
        """Devuelve un booleano, las fichas de la barrera se pueden sacar del buzon"""
        if self.tipo not in (TSquareTypes.Initial3, TSquareTypes.Initial4, TSquareTypes.Initial6, TSquareTypes.Initial8, 
                        TSquareTypes.Final3, TSquareTypes.Final4, TSquareTypes.Final6, TSquareTypes.Final8):
            if self.maxfichas==2:
                if self.buzon_numfichas()==2:
                    if self.buzon[0].jugador==self.buzon[1].jugador:
                        return True
        return False

    def posicionLibreEnBuzon(self):
        """Funcion que devuelve la posicion de un sitio libre con un entero. En caso negativo devuelve -1"""
        for i, p in enumerate(self.buzon):
            if p==None:
                return i
        return -1

    def buzon_append(self,  ficha):
        """No chequea debe ser comprobado antes"""
        self.buzon[self.posicionLibreEnBuzon()]=ficha
        self.UltimaFichaEnLlegar=ficha
            
    def buzon_remove(self, ficha):
        """No chequea debe ser comprobado antes"""
        for i, f in enumerate(self.buzon):
            if f==ficha:
                self.buzon[i]=None
                if f==self.UltimaFichaEnLlegar:#Si la ficha a borrar era la ultima se pone a None
                    self.UltimaFichaEnLlegar=None
                return
        print ("No se ha podido hacer buzon_remove con {0}".format(ficha))
                
    def buzon_numfichas(self):
        """Funcion que devuelve el numero de fichas en el buzon"""
        resultado=0
        for f in self.buzon:
            if f!=None:
                resultado=resultado+1
        return resultado

    def buzon_fichas(self):
        """Como ahora puede haber una ficha y estar en buzon[1] se hace necesario esta funcion.
        Devuelve una lista de fichas con una tupla (posicion, ficha)"""
        resultado=[]
        for i, f in enumerate(self.buzon):
            if f!=None:
                resultado.append((i, f))
        return resultado


class SoundSystem:
    def __init__(self):
        self.sounds={}
        self.load_all()
        
    def load_all(self):
        for effect in ["comer", "click", "dice", "meter", "threesix", "win", "move"]:
            s=QSoundEffect()
            url=resource_filename("glparchis","sounds/{}.wav".format(effect))
            s.setSource(QUrl.fromLocalFile(url))
            s.setLoopCount(1)
            s.setVolume(0.99)
            self.sounds[effect]=s
            
    ## Plays a QSoundEffect
    ## @param effect 
    ## @param waittofinish. If False sound is played asyncronously
    def play(self, effect, waittofinish=True):
        self.sounds[effect].play()

## Abstract Mem objcet
## Must be initializated with Mem4, Mem6 or Mem 8
class Mem:
    ## Constructor
    ## @param maxplayers Number of game players
    def __init__(self, maxplayers):     
        self.maxplayers=maxplayers
        self.uuid=uuid4()
        self.pawnsgame=ManagerPawnsGame()

                
        self.colores=ColorManager()
        self.jugadores=SetJugadores(self)
        self.dic_rutas={}
        self.dado=Dado()
        self.selFicha=None
        self.playedtime=None#Tiempo inicio partida
        self.settings=None
        self.translator=None           
        self.mediaObject = None
        self.frmMain=None #Pointer to QMainWindow
        self.delay=300
        
        
        
        
    ##  Play sounds inside a game, You can play sound using self.frmMain.sound.play(sound) directly too
    ## @param sound
    ## @param waittofinish. If False sound is played asyncronously
    def play(self, sound, waittofinish=True):
        if str2bool(self.settings.value("frmSettings/sound"))==True:
            self.frmMain.sound.play(sound, waittofinish)
        else:
            delay(self.delay)
   
    ## Create Pawns 
    ## It must be generated after players constructors
    def generar_fichas(self):
        id=0
        for ic, c in enumerate(self.colores.arr):
            j=self.jugadores.find_by_colorname(c.name)
            j.ruta=self.rutas.ruta(ic)
            for i in range(4):
                ficha=Ficha(self, id, i, c, self.jugadores.find_by_colorname(c.name), j.ruta)
                self.pawnsgame.append(ficha)
                j.fichas.arr.append(ficha)#Rellena el SetFichas del jugador
                id=id+1

    def generar_jugadores(self):
        for c in self.colores.arr:
            j=Jugador(self, c)
            self.jugadores.arr.append(j)
            j.dado=self.dado

    def save(self, filename):
        """Version 1.1 INtroduce stadisticas
        Version 1.2 Introduce uuid
        Version 1.3 Changed iniitime by playedtime"""
        chdir(path.expanduser("~/.glparchis/"))
        config = ConfigParser()
        
        config.add_section("game")
        config.set("game", 'playerstarts',self.jugadores.actual.color.name)
        config.set("game",  "numplayers",  str(self.maxplayers))
        config.set("game", 'fakedice','')
        config.set("game", 'fileversion','1.3')
        config.set("game",  'playedtime', str(datetime.now()-self.playedtime))
        config.set("game",  'uuid', str(self.uuid))
        for i, j in enumerate(self.jugadores.arr):
            config.add_section("jugador{0}".format(i))
            config.set("jugador{0}".format(i),  'ia', str(j.ia))
            config.set("jugador{0}".format(i),  'name', j.name)
            config.set("jugador{0}".format(i),  'plays', str(j.plays))
            config.set("jugador{0}".format(i),  'eatbyme', str(j.comidaspormi))
            config.set("jugador{0}".format(i),  'eatbyothers', str(j.comidasporotro))
            config.set("jugador{0}".format(i),  'roll1', str(j.tiradahistorica.numTimesDiceGetNumber(1)))
            config.set("jugador{0}".format(i),  'roll2', str(j.tiradahistorica.numTimesDiceGetNumber(2)))
            config.set("jugador{0}".format(i),  'roll3', str(j.tiradahistorica.numTimesDiceGetNumber(3)))
            config.set("jugador{0}".format(i),  'roll4', str(j.tiradahistorica.numTimesDiceGetNumber(4)))
            config.set("jugador{0}".format(i),  'roll5', str(j.tiradahistorica.numTimesDiceGetNumber(5)))
            config.set("jugador{0}".format(i),  'roll6', str(j.tiradahistorica.numTimesDiceGetNumber(6)))
            config.set("jugador{0}".format(i),  'six3', str(j.tiradahistorica.numThreeSixes()))
            if j.plays==True:
                config.set("jugador{0}".format(i),  'rutaficha1', str(j.fichas.arr[0].posruta))
                config.set("jugador{0}".format(i),  'rutaficha2', str( j.fichas.arr[1].posruta))
                config.set("jugador{0}".format(i),  'rutaficha3',  str(j.fichas.arr[2].posruta))
                config.set("jugador{0}".format(i),  'rutaficha4',  str(j.fichas.arr[3].posruta))
        with open(filename, 'w') as configfile:
            config.write(configfile)           

    ##Function that allows to select current maxplayer object, Given the class root name
    ## @param cls is a Class string name
    ## @param args are the parameters of cls class constructor
    ## For example:  class_players(Tablero), selects Tablero8 if mem.maxplayers=8
    def class_players(self,  cls, *args ):
        return globals()["{}{}".format(cls, self.maxplayers)](args)
   
    def load(self, filename):       
        def error():           
            qmessagebox(QApplication.translate("glparchis", "Este fichero es de una version antigua o esta estropeado. No puede ser cargado."))
        ################################
        config = ConfigParser()
        config.read(filename)
        
        try:
            fileversion=config.get("game", "fileversion")
            self.maxplayers=config.getint("game",  "numplayers")
            self.uuid=config.get("game", "uuid")
        except:
            fileversion=None
            error()
            return False
            
        if fileversion!="1.3":#Ir cambiando segun necesidades
            error()
            return False

        try:
            init=config.get("game", "playedtime").split(".")[0]#Quita milissegundos
            arrinit=init.split(":")
            delta=timedelta(hours=int(arrinit[0]), minutes=int(arrinit[1]),  seconds=int(arrinit[2]))
            self.playedtime=datetime.now()-delta
        except:
            self.playedtime=datetime.now()
            print ("No se ha podido cargar el playedtime")
        
        for i, j in enumerate(self.jugadores.arr):
            j.name=config.get("jugador{0}".format(i), "name")
            j.ia=str2bool(config.get("jugador{0}".format(i), "ia"))
            j.plays=str2bool(config.get("jugador{0}".format(i), "plays"))
            try:
                j.comidaspormi=config.getint("jugador{0}".format(i), "eatbyme")
                j.comidasporotro=config.getint("jugador{0}".format(i), "eatbyothers")
            except:
                j.comidaspormi=0
                j.comidasporotro=0
                print("No se ha podido cargar comidas por mi u otros")
                
            if j.plays==True:
                j.fichas.arr[0].mover(config.getint("jugador{0}".format(i), "rutaficha1"), False,  True)
                j.fichas.arr[1].mover(config.getint("jugador{0}".format(i), "rutaficha2"), False,  True)
                j.fichas.arr[2].mover(config.getint("jugador{0}".format(i), "rutaficha3"), False,  True)
                j.fichas.arr[3].mover(config.getint("jugador{0}".format(i), "rutaficha4"), False,  True)
                
                #REGENERATE STATISTICS
                #Genera dos arrays, con seixes y no seises
                sixes=[]
                nosixes=[]
                for dice in range(1, 7):
                    for n in range(config.getint("jugador{0}".format(i), "roll{}".format(dice))):
                        if dice<6:
                            nosixes.append(dice)#Mete los no seises por jugador
                        else:
                            sixes.append(dice)#Mete los seises por jugador

                # Para generar las tiradas, hay que crear en jugador una TiradaTurno nuevo, usar la funcion jugador.tirarDAdo en ese turno, la funci´on hace el resto.
                #list.pop(0) borra el primero de la lista y lo devuleve
                #1 Los 3 seises
                for n in range(config.getint("jugador{0}".format(i), "six3")):
                    j.tiradaturno=TiradaTurno()
                    j.tirarDado(sixes.pop(0))
                    j.tirarDado(sixes.pop(0))
                    j.tirarDado(sixes.pop(0))
                    
                #2 Segundo los seixes, cogiendo uno de nosiexes tambien
                for n in range(len(sixes)):
                    j.tiradaturno=TiradaTurno()
                    j.tirarDado(6)
                    j.tirarDado(nosixes.pop(0))
                    
                #3 Resto de n´umeros
                for a in nosixes:
                    j.tiradaturno=TiradaTurno()
                    j.tirarDado(a)
                #FIN  DE ESTADISTICAS


        fake=config.get("game", 'fakedice')
        if fake!="":
            for i in  fake.split(";")  :
                self.dado.fake.append(int(i))

        self.jugadores.actual=self.jugadores.find_by_colorname(config.get("game", 'playerstarts'))    
        self.jugadores.actual.tiradaturno=TiradaTurno()
        self.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
        return True

class Mem8(Mem):    
    def __init__(self):
        Mem.__init__(self, 8)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=CasillaManager(8, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        self.tablero=self.class_players("Tablero")
        
        self.circulo=Circulo(self, 136)

class Mem6(Mem):    
    def __init__(self):
        Mem.__init__(self, 6)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=CasillaManager(6, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        self.tablero=self.class_players("Tablero")
        
        self.circulo=Circulo(self, 102)

class Mem3(Mem):    
    def __init__(self):
        Mem.__init__(self, 3)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=CasillaManager(self.maxplayers, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        self.tablero=self.class_players("Tablero")
        
        self.circulo=Circulo(self, 51)

class Mem4(Mem):
    def __init__(self):
        Mem.__init__(self, 4)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=CasillaManager(self.maxplayers, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        self.tablero=self.class_players("Tablero")
        
        self.circulo=Circulo(self, 68)
