#-*- coding: utf-8 -*- 
from OpenGL.GL import *
from OpenGL.GLU import *
from poscasillas8 import *
from posfichas8 import *
from poscasillas4 import *
from posfichas4 import *
from poscasillas6 import *
from posfichas6 import *
import os,  random,   ConfigParser,  datetime,  time,  sys,  codecs,  base64,  math,  glob
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.phonon import Phonon
#Cuando se modifique una version sacada se pondrá un + p.e. 20120921+
version="20130228+"
def q2s(q):
    """Qstring to python string en utf8"""
    return str(QString.toUtf8(q))
    
def s2q(st):
    """utf8 python string to qstring"""
    if st==None:
        return QString("")
    else:
        return QString(st.decode("UTF8"))

def i2b(integer):
    """Convierte 1 en Truue 0 en False"""
    if integer==1:
        return True
    elif integer==0:
        return False
        
def c2b(state):
    """QCheckstate to python bool"""
    if state==Qt.Checked:
        return True
    else:
        return False

def delay(miliseconds):
    dieTime= datetime.datetime.now()+datetime.timedelta(microseconds=miliseconds*1000)
    while datetime.datetime.now()< dieTime :
        QCoreApplication.processEvents(QEventLoop.AllEvents, 100);    


class Dado(QObject):    
    def __init__(self, parent=None ):
        QGLWidget.__init__(self, parent)
        self.fake=[]
        self.showing=False
        self.position=(65/2, 65/2, 1)
        self.oglname=17
        self.lasttirada=None
        
    def tirar(self):
        random.seed(datetime.datetime.now().microsecond)
        if len(self.fake)>0:
            resultado=self.fake[0]
            self.fake.remove(self.fake[0])
        else:
            resultado= int(random.random()*6)+1
        self.lasttirada=resultado
        return resultado
        
    def dibujar(self, ogl, alone=False):
        """Cuando se dibuja alone, no tiene en cuenta los jugadores es para showobject"""
        if self.showing==False:
            return
        glInitNames();
        glPushName(self.oglname);
        glPushMatrix();
        if alone==False:
            if ogl.mem.maxplayers==4:
                if ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("yellow"):
                    self.position=(10, 51, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("blue"):
                    self.position=(9, 10, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("red"):
                    self.position=(50, 10, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("green"):
                    self.position=(50, 51, 1)
            elif ogl.mem.maxplayers==6:
                if ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("yellow"):
                    self.position=(30, 31, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("blue"):
                    self.position=(23, 27, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("red"):
                    self.position=(23, 18, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("green"):
                    self.position=(30, 14, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("dimgray"):
                    self.position=(37, 18, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("fuchsia"):
                    self.position=(37, 27, 1)
            else:
                if ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("yellow"):
                    self.position=(30, 30, .9)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("blue"):
                    self.position=(19, 27, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("red"):
                    self.position=(15, 15, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("green"):
                    self.position=(19, 3, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("dimgray"):
                    self.position=(30, 0, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("fuchsia"):
                    self.position=(40, 3, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("darkorange"):
                    self.position=(44, 15, 1)
                elif ogl.mem.jugadores.actual==ogl.mem.jugadores.jugador("darkturquoise"):
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
        glScaled(3,3,3);
        glColor3d(255, 255, 255);

        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[3]);
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
        glPopName();
        glPopMatrix();

        glDisable(GL_TEXTURE_2D);
        
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
                    
class Amenaza:
    """Clase que controla las amenazas que se ciernen sobre una ficha"""
    def __init__(self,  objetivo, atacante, tipo):
        self.objetivo=objetivo
        self.atacante=atacante
        self.tipo=tipo #1-6 dados, 7 seis con todas fuera,10 meter una ficha, 20 comer una ficha, 51 saca un cinco y mueve 1
        
    def name(self, tipo=None):
        if tipo==None:
            tipo=self.tipo
        if tipo==1: return QApplication.translate("glparchis",u"Sacar un 1")
        if tipo==2: return QApplication.translate("glparchis",u"Sacar un 2")
        if tipo==3: return QApplication.translate("glparchis",u"Sacar un 3")
        if tipo==4: return QApplication.translate("glparchis",u"Sacar un 4")
        if tipo==5: return QApplication.translate("glparchis",u"Sacar un 5")
        if tipo==6: return QApplication.translate("glparchis",u"Sacar un 6")
        if tipo==7: return QApplication.translate("glparchis",u"Sacar un 7")
        if tipo==10: return QApplication.translate("glparchis",u"Contar 10")
        if tipo==20: return QApplication.translate("glparchis",u"Contar 20")
        if tipo==51: return QApplication.translate("glparchis",u"Sacar un 5")

class SetAmenazas:
    """Clase que genera las amenazas contra un objetivo en la casilla pasado como par´ametro"""
    def __init__(self,  mem,  objetivo, casilla):
        """Crea objeto"""
        self.arr=[]#Array de objetos amenaza
        self.objetivo=objetivo#Ficha objetivo de la amenaza. 
        self.casilla=casilla
        self.mem=mem
        self.detectar()
        
    def append(self, atacante, type):
        self.arr.append(Amenaza(self.objetivo, atacante, type))
            
    def detectar(self):
        del self.arr
        self.arr=[]
        print ("detectando en ",  self.casilla)
        
        
        if self.casilla.tipo==0 or self.casilla.tipo==1:#Casilla inicial y final
            return
        
        if self.casilla.rampallegada==True:
            return
        
        
        if self.casilla.seguro==True and self.casilla not in self.mem.casillas.rutas1():# Esta asegurada y no est´a en ruta 1
            return
            
        #Detecta salida con un 5 a ruta1
        if self.casilla in self.mem.casillas.rutas1():
            #Busca la casilla inicial del mismo color
            casillaataque=self.mem.rutas.ruta(self.mem.colores.index(self.casilla.color)).arr[0]#Casilla inicial
            if casillaataque.buzon_numfichas()>0:#Hay fichas que coman
                print (casillaataque)
                if self.casilla.buzon_numfichas()==2:
                    if  self.objetivo.posruta!=1: #Si no est´a en su propia ruta1, est´a llena
                        for posicion, ficha in casillaataque.buzon_fichas():
                            if  ficha.puedeComer(self.mem, ficha.posruta+1): #aquí chequea que sea mismo color o distinta, ultima en llegar...
                                self.append(ficha, 51)
                                break#Con que haya uno es suficiente
                            else:
                                return
                    else:#Esta en su propia ruta1
                        return
                else:
                    return
            else:
                return
        
        #Detecta si hay ficha en 1OJO LA CASILLA QUE SE BUSCA NO ES LA ACTUAL DEL OBJETIVO sino la de parametro de entrada self.casilla
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -1)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+1):
                self.append(ficha, 1)
        #Detecta si hay ficha en 2
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -2)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+2):
                self.append(ficha, 2)
        #Detecta si hay ficha en 3
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -3)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+3):
                self.append(ficha, 3)
        #Detecta si hay ficha en 4
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -4)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+4):
                self.append(ficha, 4)
        #Detecta si hay ficha en 5
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -5)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+5):
                self.append(ficha, 5 )
        #Detecta si hay ficha en 6 y chequea que no tiene todas fuera de casa
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -6)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador.tieneFichasEnCasa()==False:
                continue
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+6):
                self.append(ficha, 6 )
                
        #Detecta si hay ficha en 7 y chequea que tiene todas fuera de casa
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -7)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador.tieneFichasEnCasa()==True:
                continue
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+7):
                self.append(ficha, 7 )
        
        #Detecta si hay ficha en 10
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -10)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador.tieneFichasEnRampaLlegada()==False:
                continue
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+10):
                self.append(ficha, 10 )
                
        #Detecta si hay ficha en 20
        casillaataque=self.mem.circulo.casilla(self.casilla.id, -20)
        for posicion, ficha in casillaataque.buzon_fichas():
            if ficha.jugador!=self.objetivo.jugador and ficha.puedeComer(self.mem, ficha.posruta+20):
                self.append(ficha, 20 )


    def numero(self):
        return len(self.arr)

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
        """Función que devuelve un booleano según haya o no salido 3 seises"""
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
    """Clase que calcula gestiona todo lo relacionado con el highscore. Sólo debe usarse cuando haya acabado la partida
    y haya un winner"""
    def __init__(self, mem, players):
        self.players=players
        self.mem=mem
        self.arr=[]#Cada item tendrá la fecha en ordinal, nombre, tiempo de partida, color, el score
        self.load()

    def insert(self):
        """Solo se puede ejecutar, cuando haya un winner"""
        self.arr.append((datetime.date.today().toordinal(), self.mem.jugadores.winner.name, (datetime.datetime.now()-self.mem.inittime).seconds, self.mem.jugadores.winner.color.name,  str(self.mem.jugadores.score())))
        self.arr=sorted(self.arr, key=lambda a:a[4],  reverse=True)     

    def load(self):
        try:
            f=codecs.open(os.path.expanduser("~/.glparchis/")+ "highscores"+str(self.players), "r", "utf-8")
            for line in f.readlines():
                a=line[:-1].split(";")
                self.arr.append((a[0], a[1], a[2], self.mem.colores.arr[0].compatibilityName(a[3]),  a[4]))
            f.close()
        except:
            print("I couldn't load highscores")
            
            
        
    def save(self):        
        f=codecs.open(os.path.expanduser("~/.glparchis/")+ "highscores"+str(self.players), "w", "utf-8")
        s=""
        for a in self.arr[:10]:
            s=s+"{0};{1};{2};{3};{4}\n".format(a[0], a[1],  a[2], a[3], a[4])
        f.write(s)
        f.close()
                
class Jugador:
    def __init__(self,  color):
        self.name=None#Es el nombre de usuario no el de color
        self.color=color
        self.ia=False
        self.plays=True
        self.fichas=SetFichas()     
        self.tiradaturno=TiradaTurno()#TiradaJugador()
        self.tiradahistorica=TiradaHistorica()
        self.LastFichaMovida=None #Se utiliza cuando se va a casa NOne si ninguna
        self.movimientos_acumulados=None#Comidas ymetidas, puede ser 10, 20 o None Cuando se cuenta se borra a None
        self.dado=None #Enlace a objeto dado de mem
        self.logturno=[]#log de turno
        self.loghistorico=[]
        self.comidaspormi=0
        self.comidasporotro=0
        self.ruta=None#Se apunta

    def __repr__(self):
        return "Jugador {0}".format(self.color.name)

    def log(self, l):
        l=u"{0} {1}".format(str(datetime.datetime.now().time()).split(".")[0], l)
        self.logturno.append( l)
        self.loghistorico.append(l)
        
    def casillasPorMover(self):
        """Casillas que le queda al jugador hasta ganar la partida"""
        resultado =0
        for f in self.fichas.arr:
            resultado=resultado+f.casillasPorMover()
        return resultado
            
    def casillasMovidas(self):
        """Casillas que ha movido el jugador, puede considerarse la puntuación del jugador"""
        return 4*self.fichas.arr[0].ruta.length()-self.casillasPorMover()
            
        
    def hayDosJugadoresDistintosEnRuta1(self):
        ruta1=self.ruta.ruta1()
        if ruta1 not in self.ruta.mem.rutas.rutas1():#Casillas ruta1
            return False
        if ruta1.buzon_numfichas()!=2:
            return False
        if ruta1.buzon[0].jugador!=ruta1.buzon[1].jugador:
            return True
        return False
        
        
    def tirarDado(self):
        """Tira el dado lo almacena en tirada, tiradaturno e historico y devuelve el valor"""
        tirada=Tirada(self, self.dado.tirar())
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
        

    def HaGanado(self):
        for f in self.fichas.arr:
            if f.estaEnMeta()==False:
                return False
        return True
        
    def IASelectFicha(self, mem):
        """Función que devuelve la ficha seleccionada por la IA. Si devuelve None es que ninguna se puede mover"""
        def azar(tope):
            """Función que saca un numero al azar de entre 1 y 100. Si es mayor del tope devuelve true. Sino devuelve false. Es decir tope 85 es una probabilidad del 85%"""
            random.seed(datetime.datetime.now().microsecond)
            numero=int(random.random()*100)
            if numero<tope:
                return True
            return False
        ####################################
        fichas=self.fichas.fichasAutorizadasAMover(mem)
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)     
        if len(fichas)==0:
            return None
        
        # Hay porcentajes de acierto si falla pasa a la siguiente prioridad
        #1 prioridad. Puede comer IA 85%
        if azar(95):
            for f in fichas:#Recorre las que pueden mover
                movimiento=f.estaAutorizadaAMover(mem)[1]
                (puede, fichaacomer)=f.puedeComer(mem, f.posruta+movimiento)
                if puede:
                    print (f, "seleccionada por azar comer")
                    return f
        
        #2 prioridad. Mueve fichas que disminuyen en número de amenazas en la nueva posicion
        fichas=sorted(fichas, key=lambda f:f.numeroAmenazasMejora(mem),  reverse=True)     
#        for f in fichas:
#            print (f, f.numeroAmenazasMejora(mem), f.numFichasPuedenComer(mem, f.posruta), f.numFichasPuedenComer(mem, f.posruta+f.estaAutorizadaAMover(mem)[1]))
        if azar(95):
            for f in fichas:
                if f.numeroAmenazasMejora(mem)>=0 and  f.numFichasPuedenComer(mem, f.posruta+f.estaAutorizadaAMover(mem)[1])>0: #Debe estar amenazada
                    print (f, "seleccionada por azar al mejorar numero de fichas la pueden comer")
                    return f
        
        
        #3 prioridad Asegura IA  de ultima a primera 85%
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)     
        if azar(95):
            for f in fichas:
                movimiento=f.estaAutorizadaAMover(mem)[1]
                if f.casilla().esUnSeguroParaJugador(mem, self)==False  and  f.casilla(f.posruta+movimiento).seguro==True:
                    print (f,"seleccionado por azar asegurar")
                    return f
        
        #4 Alguna ficha no asegurada puede mover
        if azar(95):
            for f in fichas:
                if f.casilla().esUnSeguroParaJugador(mem, f.jugador)==False:
                    print(f,"seleccionado por azar ficha no asegurada")
                    return f
        
        #5 prioridad Mueve la ultima IA 100%
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)
        print (fichas[0], "Sin azar. Ultima ficha")
        return fichas[0]

            
class Ruta:
    def __init__(self, color, mem):
        self.arr=[] #Array ordenado
        self.color=color
        self.mem=mem
        
    def append_id(self,  arr):
        """Función que recibe un arr con los id de la ruta"""
        for id in arr:
            self.arr.append(self.mem.casillas.casilla(id))
            
    def length(self):
        """Saca el número de casillas """
        return len(self.arr)
        
    def ruta1(self):
        return self.arr[1]
    
    
class SetColores:
    """Agrupación de jugadores"""
    def __init__(self):
        self.arr=[]    
    
    def generar_colores(self, maxplayers):
        self.arr.append(Color( 255, 255, 50, "yellow"))
        self.arr.append(Color(50, 60, 180, "blue"))
        self.arr.append(Color(255, 50, 50, "red"))
        self.arr.append(Color(50, 255, 50, "green"))
        if maxplayers>4:#Para 6
            self.arr.append(Color(64, 64, 64, "dimgray"))
            self.arr.append(Color(255, 50, 255, "fuchsia"))
        if maxplayers>6:# Para 8
            self.arr.append(Color(255, 128, 50, "darkorange"))
            self.arr.append(Color(50, 255, 255, "darkturquoise"))
            
    def color(self, colo):
        for c in self.arr:
            if c==colo:
                return c
                            
    def colorbyname(self, name=None):
        for c in self.arr:
            if c.name==name:
                return c
        print ("No se ha encontrado el color de nombre {0}".format(name))
                
    def index(self, color):
        """Función que devuelve un orden de color según se ha insertado en el array"""
        for i, c in enumerate(self.arr):
            if c==color:
                return i
    
class SetJugadores:
    """Agrupación de jugadores"""
    def __init__(self, mem):
        self.arr=[]
        self.mem=mem
        self.actual=None
        self.winner=None
        
    def index(self, jugador):
        """Devuelve la posicion en self.arr del jugador"""
        for i, j in enumerate(self.arr):
            if j==jugador:
                return i
        
    def cambiarJugador(self):        
        index=self.index(self.actual)
        if index==len(self.arr)-1:
            self.actual=self.arr[0]
        else:
            self.actual=self.arr[index+1]
            
        if self.actual.plays==False:
            self.cambiarJugador()
            return
        else:
            self.actual.tiradaturno=TiradaTurno()#Se crea otro objeto porque así el anterior queda vinculada< a TiradaHistorica.
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
        
    def jugador(self, colorname):
        for j in self.arr:
            if j.color.name==colorname:
                return j
        return None
        
    def alguienHaGanado(self):
        for j in self.arr:
            if j.HaGanado()==True:
                return True
        return False
        
        
    def score(self, jugador=None):
        """Da la puntuación de un jugador, durante o al final de la partida 
        Saca la puntuación del jugador, se usa para el highscore y tiene en cuenta el tiempo 
        y lo lejos que han acabado los jugadores de la partida,
        Resta el número de casillas del propio jugador
       Además se sumará la diferencia de comidas y comidas por otro *30 
       
       Si no se pasa parámetro se usa para seleccionar el winner cuando haya acabado la partida"""
        if jugador==None:
            jugador=self.winner
        resultado=0
        jugadorcm=jugador.casillasPorMover()
        for j in  self.arr:
            if j != jugador:
                jcm=j.casillasPorMover()
                if jcm>jugadorcm:#Ya que si no salen valores negativos
                    resultado=resultado+jcm-jugadorcm
        resultado=resultado+(jugador.comidaspormi-jugador.comidasporotro)*40
        if resultado<0:#Ya que la direfencia de comidas puede dar negativo
            resultado=0
        return resultado
        
        
class SetRutas:        
    def __init__(self, numplayers,  mem):
        """Mem se necesita para identificar los colores"""
        self.arr=[]
        self.mem=mem
        self.numplayers=numplayers
        self.generar_rutas()
        
    def ruta(self, id):        
        """id es el mismo que el orden de los colores"""
        return self.arr[id]
        
    def rutas1(self):
        """Función que devuelve un arr con punteros a las casillas que están en ruta1
        Para poder saber de que color son, se puede usar casilla.color"""
        resultado=[]
        for r in self.arr:
            resultado.append(r.ruta1())
        return resultado

        
    def generar_rutas(self):
        if self.numplayers==4:
            self.generar_rutas4()
        elif self.numplayers==6:
            self.generar_rutas6()
        elif self.numplayers==8:
            self.generar_rutas8()

    def generar_rutas4(self):    
        r=Ruta(self.mem.colores.colorbyname("yellow"), self.mem)
        r.append_id( [101]+range(5, 76+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("blue"), self.mem)
        r.append_id([102]+ range(22, 68+1)+range(1, 17+1)+range(77, 84+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("red"), self.mem)
        r.append_id( [103]+range(39, 68+1)+range(1, 34+1)+range(85, 92+1))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.colorbyname("green"), self.mem)
        r.append_id([104]+range(56, 68+1)+range(1, 51+1)+range(93, 100+1))
        self.arr.append(r)        
            

    def generar_rutas6(self):    
        r=Ruta(self.mem.colores.colorbyname("yellow"), self.mem)
        r.append_id([151]+range(5, 110+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("blue"), self.mem)
        r.append_id([152]+range(22, 102+1)+range(1, 17+1)+range(111, 118+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("red"), self.mem)
        r.append_id( [153]+range(39, 102+1)+range(1, 34+1)+range(119, 126+1))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.colorbyname("green"), self.mem)
        r.append_id([154]+range(56, 102+1)+range(1, 51+1)+range(127, 134+1))
        self.arr.append(r)      
        r=Ruta(self.mem.colores.colorbyname("dimgray"), self.mem)
        r.append_id([155]+range(73, 102+1)+range(1, 68+1)+range(135, 142+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("fuchsia"), self.mem)
        r.append_id([156]+range(90, 102+1)+range(1, 85+1)+range(143, 150+1))
        self.arr.append(r)       

    def generar_rutas8(self):    
        r=Ruta(self.mem.colores.colorbyname("yellow"), self.mem)
        r.append_id([201]+range(5, 144+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("blue"), self.mem)
        r.append_id([202]+range(22, 136+1)+range(1, 17+1)+range(145, 152+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("red"), self.mem)
        r.append_id( [203]+range(39, 136+1)+range(1, 34+1)+range(153, 160+1))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.colorbyname("green"), self.mem)
        r.append_id([204]+range(56, 136+1)+range(1, 51+1)+range(161, 168+1))
        self.arr.append(r)            
        r=Ruta(self.mem.colores.colorbyname("dimgray"), self.mem)
        r.append_id([205]+range(73, 136+1)+range(1, 68+1)+range(169, 176+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("fuchsia"), self.mem)
        r.append_id([206]+range(90, 136+1)+range(1, 85+1)+range(177, 184+1))
        self.arr.append(r)
        r=Ruta(self.mem.colores.colorbyname("darkorange"), self.mem)
        r.append_id([207]+range(107, 136+1)+range(1, 102+1)+range(185, 192+1))
        self.arr.append(r) 
        r=Ruta(self.mem.colores.colorbyname("darkturquoise"), self.mem)
        r.append_id([208]+range(124, 136+1)+range(1, 119+1)+range(193, 200+1))
        self.arr.append(r)    

class SetCasillas:
    """Conjunto de casillas. Si es 209 es para 8 jugadores, Si es 105 es para 4 jugadores y 1 para 6 jugadores"""
    def __init__(self, numplayers, mem):
        """Mem se necesita para identificar los colores"""
        self.arr=[]
        self.mem=mem
        self.numplayers=numplayers
        if self.numplayers==4:
            self.number=105
        elif self.numplayers==6:
            self.number=157
        elif self.numplayers==8:
            self.number=209
        self.generar_casillas()
        
    def casilla(self, id):
        return self.arr[id]
        
    def rutas1(self):
        """Función que devuelve un arr con punteros a las casillas que están en ruta1
        Para poder saber de que color son, se puede usar casilla.color"""
        resultado=[]
        if self.numplayers==6:
            resultado.append(self.arr[5])
            resultado.append(self.arr[22])
            resultado.append(self.arr[39])
            resultado.append(self.arr[56])
            resultado.append(self.arr[73])
            resultado.append(self.arr[90])
        elif self.numplayers==8:
            resultado.append(self.arr[5])
            resultado.append(self.arr[22])
            resultado.append(self.arr[39])
            resultado.append(self.arr[56])
            resultado.append(self.arr[73])
            resultado.append(self.arr[90])
            resultado.append(self.arr[105])
            resultado.append(self.arr[122])
        elif self.numplayers==4:       
            resultado.append(self.arr[5])
            resultado.append(self.arr[22])
            resultado.append(self.arr[39])
            resultado.append(self.arr[56])
        return resultado
        
            
    def generar_casillas(self):
        if self.numplayers==6:
            self.generar_casillas6()
        elif self.numplayers==8:
            self.generar_casillas8()
        elif self.numplayers==4:
            self.generar_casillas4()
                                
    def generar_casillas4(self):
        def defineSeguro( id):
            if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
                return True
            elif id>=69 and id<=100:#Las de la rampa de llegada también son seguras
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
               return 0 #Casilla inicial
            elif id==76 or id==84 or id==92 or id==100:
               return 1 #Casilla final
            elif id==9 or  id==26 or  id==43 or  id==60:  
               return 2 #Casilla oblicuai
            elif id==8 or  id==25 or  id==42 or  id==59:  
               return 4 #Casilla oblicuad
            else:
                return 3 #Casilla Normal
    
        def defineColor( id):
            if id==5 or (id>=69 and id<=76) or id==101:
               return self.mem.colores.colorbyname("yellow")
            elif id==22 or (id>=77 and id<=84) or id==102:
               return self.mem.colores.colorbyname("blue")
            elif id==39 or (id>=85 and id<=92) or id==103:
               return self.mem.colores.colorbyname("red")
            elif id==56 or (id>=93 and id<=100) or id==104:
               return self.mem.colores.colorbyname("green")
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
                
        ##############################       
        posCasillas=poscasillas4(self.number)
        posFichas=posfichas4(self.number)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            self.arr.append(Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), posFichas[i]))
            
    def generar_casillas6(self):
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
               return 0 #Casilla inicial
            elif id in  (110, 118, 126, 134, 142, 150):
               return 1 #Casilla final
            elif id==9 or  id==26 or  id==43 or  id==60 or id==77 or id==94:  
               return 2 #Casilla oblicuai
            elif id==8 or  id==25 or  id==42 or  id==59 or id==76 or id==93:  
               return 4 #Casilla oblicuad
            else:
                return 3 #Casilla Normal
    
        def defineColor( id):
            if id==5 or (id>=103 and id<=110) or id==151:
               return self.mem.colores.colorbyname("yellow")
            elif id==22 or (id>=111 and id<=118) or id==152:
               return self.mem.colores.colorbyname("blue")
            elif id==39 or (id>=119 and id<=126) or id==153:
               return self.mem.colores.colorbyname("red")
            elif id==56 or (id>=127 and id<=134) or id==154:
               return self.mem.colores.colorbyname("green")
            elif id==73 or (id>=135 and id<=142) or id==155:
               return self.mem.colores.colorbyname("dimgray")
            elif id==90 or (id>=143 and id<=150) or id==156:
               return self.mem.colores.colorbyname("fuchsia")
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
            if (id>=10 and id<=24) or (id>=111 and id<=117)  or id in (60, 76, 126, 142):
               return 60
            if id==155:
                return 90
            if(id>=27 and id<=41) or (id>=119 and id<=125) or id in (77, 93):
                return 120
            if id==156:
                return 150
            if(id>=44 and id<=58) or (id>=127 and id<=133) or id in (8, 94):
                return 180
            if(id>=61 and id<=75) or (id>=135 and id<=141) or id in (9, 25, 118, 150):
                return 240
            if id==151:
                return 210
            if id==152:
                return 270
            if(id>=78 and id<=92) or (id>=143 and id<=149) or id in (26, 42, 110):
                return 300
            if id==153:
                return 330
            else:
                return 0        
                
        ##############################        
        posCasillas=poscasillas6(self.number)
        posFichas=posfichas6(self.number, posCasillas)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            self.arr.append(Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i) , defineRotatePN(i),  defineRampaLlegada(i), defineTipo(i), defineSeguro(i), posFichas[i]))
            
 
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
               return 0 #Casilla inicial
            elif id in (144, 152, 160, 168, 176, 184, 192, 200):
               return 1 #Casilla final
            elif id in (9, 26, 43, 60, 77, 94, 111, 128):  
               return 2 #Casilla oblicuai
            elif id in (8, 25, 42, 59, 76, 93, 110, 127):  
               return 4 #Casilla oblicuad
            else:
                return 3 #Casilla Normal
    
        def defineColor( id):
            if id in (5,  137, 138, 139, 140, 141, 142, 143, 144, 201) :
               return self.mem.colores.colorbyname("yellow")
            elif id in (22, 145, 146, 147, 148, 149, 150, 151, 152, 202):
               return self.mem.colores.colorbyname("blue")
            elif id in (39, 153, 154,  155, 156, 157, 158, 159, 160, 203) :
               return self.mem.colores.colorbyname("red")
            elif id in (56, 161, 162, 163, 164, 165, 166, 167, 168, 204):
               return self.mem.colores.colorbyname("green")
            elif id in (73, 169, 170, 171, 172, 173, 174, 175, 176, 205):
               return self.mem.colores.colorbyname("dimgray")
            elif id in (90, 177, 178, 179, 180, 181, 182, 183, 184, 206):
               return self.mem.colores.colorbyname("fuchsia")
            elif id in (107, 185, 186, 187, 188, 189, 190, 191, 192, 207) :
               return self.mem.colores.colorbyname("darkorange")
            elif id in (124, 193, 194, 195, 196, 197, 198, 199, 200, 208) :
               return self.mem.colores.colorbyname("darkturquoise")
            else:
                return Color(255, 255, 255)            
                
        def defineRotatePN(id):
            """EStablece si debe rotar el panel numerico"""
            if (id>=61 and id<=75) or id in(8, 9, 25, 26, 42, 43, 59, 60,  76, 77, 93, 94, 110, 111, 127, 128):
                return False
            return True
            
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
                
        ##############################        
        posCasillas=poscasillas8(self.number)
        posFichas=posfichas8(self.number, posCasillas)
        for i in range(0, self.number):#Se debe inializar Antes que las fichas
            self.arr.append(Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i), defineRotatePN(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), posFichas[i]))
            
class SetFichas:
    """Agrupación de fichas"""
    def __init__(self):
        self.arr=[]

    def algunaEstaObligada(self, mem):
        """Busca entre las fichas que pueden mover si alguna está obligada a mover"""
        for f in self.arr:
            if f.estaObligada(mem)==True:
                return True
        return False

    def algunaEstaAutorizadaAmover(self, mem):
        if len(self.fichasAutorizadasAMover(mem))>0:
            return True
        return False
        
    def fichasAutorizadasAMover(self, mem):
        """Devuelve un arr con las fichas que pueden mover"""
        resultado=[]
        for f in self.arr:
            if f.estaAutorizadaAMover(mem)[0]==True:
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
        
class Ficha(QObject):
    def __init__(self, id, number,  color, jugador, ruta):
        """El identificador de la ficha viene dado por el nombre del color y el id (numero de creacion), se genera en la clase Mem"""
        QGLWidget.__init__(self)
        self.color=color
        self.id=id
        self.number=number#indice dentro de las fichas de mismo color.
        self.ruta=ruta
        self.posruta=0#pOSICION EN LA RUTA
        self.ficha=gluNewQuadric();
        self.jugador=jugador
        self.oglname=self.id#Nombre usado para pick por opengl
        
    
        
    def amenazas(self, mem):
        return SetAmenazas(mem, self, self.casilla())
        
        
    def amenazasDestino(self,mem,  desplazamiento):
        if self.posruta+desplazamiento<self.ruta.length():
            return SetAmenazas(mem, self, self.ruta.arr[self.posruta+desplazamiento])
        else:
            print ("No se puede ver la amenaza destino de una ruta pasada")
        
    def __repr__(self):
        return  "Ficha {0} del jugador {1}".format(self.id, self.jugador.color.name)
        
    def estaObligada(self, mem):        
        """ESta pregunta se integra dentro de puede mover. NO DEBE HABER EN SETFICHAS ALGUNAS, YA QUE SE INTEGRARíA DENTRO DE ALGUNA PUEDEMOVER"""
        if self.puedeMover(mem)[0]==False:
            return False
            
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.ruta.arr[1].buzon_numfichas()<2:
            return True
        
        #dos jugadore distintos en inicio entonces come
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.jugador.hayDosJugadoresDistintosEnRuta1():
            return True
        
        #Comprueba que no tenga obligación de abrir barrera
        if self.jugador.tieneBarreras()==True  and self.jugador.tiradaturno.ultimoValor()==6:
            if self.casilla() in self.jugador.barreras():
                return True
        return False
        
    def estaAutorizadaAMover(self, mem, log=False):
        """PUEDE MOVER Y ESTA OBLIGADO SON DOS CONCEPTOS INDEPENDIENTES QUE NO DEBEN DE UNIRSE 
        PORQUE GENERA RECURSIVIDADPOR ESO SE HACE AQUí
        
        Autorizada significa que puede mover y no está obligada a hacer otras cosas"""
        
        (puede, movimiento)=self.puedeMover(mem, log)
        if puede:
            if mem.jugadores.actual.fichas.algunaEstaObligada(mem) :
                if self.estaObligada(mem)==False:
                    if log: mem.jugadores.actual.log(self.trUtf8("No puede mover, porque hay otra ficha obligada a mover"))
                    return (False, 0)                    
            return (puede, movimiento)
        return (puede, movimiento)
        
    def puedeMover(self, mem,  log=False):
        """Comprueba si la ficha puede mover. desde el punto de vista fisico
        Si log=True muestra los logs"""

        #Es ficha del jugador actual. #A PARTIR DE AQUI SE PUEDE USAR SELF.JUGADOR EN VEZ DE MEM.jugadores.actual
        if  self.jugador!=mem.jugadores.actual:             
            if log: mem.jugadores.actual.log(self.trUtf8("No es del jugador actual"))
            return (False, 0)
            
        #No se puede mover una ficha que está en casa con puntos acumulados
        if mem.jugadores.actual.movimientos_acumulados!=None and self.estaEnCasa():
            return (False, 0)

        #Calcula el movimiento
        if mem.jugadores.actual.movimientos_acumulados!=None:
            movimiento=mem.jugadores.actual.movimientos_acumulados
        elif self.estaEnCasa() and self.jugador.tiradaturno.ultimoValor()==5:
            movimiento= 1
        elif self.estaEnCasa()==True and self.jugador.tiradaturno.ultimoValor()!=5: #Saco un 5
            movimiento=0
        elif self.jugador.fichas.TodasFichasFueraDeCasa()==True and self.jugador.tiradaturno.ultimoValor()==6:
            movimiento=7
        else:
            movimiento=self.jugador.tiradaturno.ultimoValor()
                            
        if movimiento==0 or movimiento==None:
            if log: mem.jugadores.actual.log(self.trUtf8("No puede mover"))
            return (False, 0)    
           
        #se ha pasado la meta
        if self.posruta+movimiento>self.ruta.length()-1:
            if log: mem.jugadores.actual.log(self.trUtf8("Se ha pasado la meta"))
            return (False, 0) 
            
        #Rastrea todas las casillas de paso en busca de barrera. desde la siguiente
        for i in range(self.posruta+1, self.posruta+movimiento+1): 
            if self.ruta.arr[i].tieneBarrera()==True:
                if log: mem.jugadores.actual.log(self.trUtf8("Hay una barrera"))
                return (False, 0)

        #Comprueba si hay sitio libre
        casilladestino=self.ruta.arr[self.posruta+movimiento]
        if casilladestino.posicionLibreEnBuzon()==-1:
            if self.jugador.hayDosJugadoresDistintosEnRuta1():#COmprueeba si es primera casilla en ruta y hay otra de otro color.
                if log: mem.jugadores.actual.log(self.trUtf8("Obligado a sacar y a comer"))
            else:
                if log: mem.jugadores.actual.log(self.trUtf8("No hay espacio en la casilla"))
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

    def puedeComer(self, mem, destposruta):
        """Devuelve un (True, ficha a comer) or (False, None) si puede comer una ficha en la posición ruta"""
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
            else: #Las dos son distintas se escoge la última que entró
                print ("noigual0,noigual1")
                return (True, casilladestino.UltimaFichaEnLlegar)
                
        if casilladestino.seguro==True:
            return (False, None)
        
        if len(fichasdestino)==1:#Todavia no se ha movido
            if fichasdestino[0][1].jugador!=mem.jugadores.actual:
                return(True, fichasdestino[0][1])

        return (False, None)
                
                
    def come(self, mem,   ruta):
        """ruta, es la posición de ruta de ficha en la que come. No se ha movido antes, come si puede y devuelve True, en caso contrario False"""
        (puede, fichaacomer)=self.puedeComer(mem, ruta)
        if puede==True:
            fichaacomer.mover(0, False)
            if self.posruta==0:
                self.mover(1, True)
            else:
                self.mover(ruta, True)
            mem.jugadores.actual.movimientos_acumulados=20
            mem.jugadores.actual.log(self.trUtf8('He comido una ficha de %1 en la casilla %2').arg(fichaacomer.jugador.name).arg(self.casilla(ruta).id))
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
            self.jugador.log(self.trUtf8("Una ficha a llegado a la meta"))
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
        
    def numeroAmenazasMejora(self, mem):
        """Si devuelve un positivo es que ha disminuido en ese valor el numero de fichas que le amenzaban
        Si antes 0 y luego 1 tendra  -1
        Si antes 1 y luego 0 tendra 1
        Si antes 1 y luego 1 tendra 0
        Si antes 0 y luego o tendra 0"""
        movimiento=self.estaAutorizadaAMover(mem)[1]
        antes=self.numFichasPuedenComer(mem, self.posruta)
        despues=self.numFichasPuedenComer(mem, self.posruta+movimiento)
#        print ("Amenazas en casilla {0}: {1}. En casilla {2}: {3}".format(self.casilla(self.posruta).id, antes, self.casilla(self.posruta+movimiento).id, despues))
        return antes-despues

    def numFichasPuedenComer(self, mem, posruta=None):
        """Función que devuelve un array con las fichas que pueden comer a la ficha actual si la colocara en posruta"""
        resultado=0
        if posruta==None:
            posruta=self.posruta
            
        if posruta<0 or posruta>self.ruta.length()-1:
            return 0
            
        casilla=self.casilla(posruta)        #Datos casilla de posruta
        
        if casilla.esUnSeguroParaJugador(mem, self.jugador)==True or casilla.rampallegada==True:
            return 0
            
        if casilla.tieneBarrera():
            return 0
            
        if casilla not in mem.circulo.arr:#Si la casilla no esta en el circulo devuelve 0
            return 0
            
        #anota comer por cinco en ruta1    
        
        
        
        
        #fichas que se encuentran a una distancia en casillas
        for pos, f in mem.circulo.casilla(casilla.id, -1).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -2).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -3).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -4).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -5).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnCasa()==False:#no tiene que scar por lo que cuenta como un 5 normal
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -6).buzon_fichas():
            if f.jugador!=self.jugador: #Son fichas enemigas
                if f.jugador.tieneFichasEnCasa():
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -7).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnCasa()==False:
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -10).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnRampaLlegada():
                    resultado=resultado+1
        return resultado

    def estaEnCasa(self):
        if self.posruta==0:
            return True
        return False

    def estaEnMeta(self):
        if self.posruta==len(self.ruta.arr)-1:
            return True
        return False

    def dibujar(self, ogl,  posicionBuzon):
        glInitNames();
        glPushMatrix()
        glPushName(self.id);
        if posicionBuzon==None:#Para frmAcercade
            p=(0, 0, 0)
        else:
            p=self.ruta.arr[self.posruta].posfichas[posicionBuzon]
        glTranslated(p[0], p[1], p[2])
        glRotated(180, 1, 0, 0)# da la vuelta a la cara
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[1])
        ogl.qglColor(Color(255, 255, 0).qcolor())
        gluQuadricDrawStyle (self.ficha, GLU_FILL);
        gluQuadricNormals (self.ficha, GLU_SMOOTH);
        gluQuadricTexture (self.ficha, True);
        ogl.qglColor(self.color.qcolor())
        gluCylinder (self.ficha, 1.4, 1.4, 0.5, 16, 5)
        glTranslated(0, 0, 0.5)
        ogl.qglColor(Color(70, 70, 70).qcolor())
        gluDisk(self.ficha, 0, 1.4, 16, 5)
        ogl.qglColor(self.color.dark().qcolor())
        glTranslated(0, 0, -0.5)
        glRotated(180, 1, 0, 0)# da la vuelta a la cara
        gluDisk(self.ficha, 0, 1.40, 16, 5)
        glPopName();
        glPopMatrix()
        glDisable(GL_TEXTURE_2D);


class Tablero(QObject):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.position=(-1, -1, 0)
        self.oglname=16#Nombre usado para pick por opengl


    def dibujar(self, ogl):
        def quad(p1, p2, p3, p4, color):
            ogl.qglColor(color.qcolor())
            glTexCoord2f(0.0,0.0)
            glVertex3d(p1[0], p1[1], p1[2])
            glTexCoord2f(1.0,0.0)
            glVertex3d(p2[0], p2[1], p2[2])
            glTexCoord2f(1.0,1.0)
            glVertex3d(p3[0], p3[1], p3[2])
            glTexCoord2f(0.0,1.0)
            glVertex3d(p4[0], p4[1], p4[2])              
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[1])
        glTranslated(self.position[0],  self.position[1],  self.position[2])
        glBegin(GL_QUADS)
        v1 = (0, 0, 0)
        v2 = (65, 0, 0)
        v3 = (65, 65, 0)
        v4 = (0, 65, 0)
        v5 = (0, 0, 0.5)
        v6 = (65, 0, 0.5)
        v7 = (65, 65, 0.5)
        v8 = (0, 65, 0.5)
        color=Color(255, 255, 255)
        quad(v4, v3, v2, v1, color)      
        color=Color(70, 70, 70)
        quad(v5, v6, v7, v8, color)   
        color=Color(255, 255, 255)   
        quad(v5, v8, v4, v1, color)      
        quad(v2, v3, v7, v6, color)      
        quad(v1, v2, v6, v5, color)      
        quad(v8, v7, v3, v4, color)          

        glEnd()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
        
        
class Circulo:
    """Es el circulo publico por el que se mueven las fichas y pueden comerse entre ellas
    Es un array de casillas ordenado. que se repite ciclicamente
    numcasillas=68 para 4 jugadores"""
    def __init__(self, mem, numcasillas):
        self.arr=[]
        self.numcasillas=numcasillas
        for i in range(1, self.numcasillas+1):
            self.arr.append(mem.casillas.casilla(i))
    
    def casilla(self, posicion,  desplazamiento):
        """Calcula la casilla del circulo que tiene un desplazamiento positivo (hacia adelante) o negativo (hacia atrás) 
        de la casilla cuya posicion (id de la casilla) se ha dado como parametro"""
        if posicion<1 or posicion>self.numcasillas:   #Si no está en el circulo
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
                            
    def compatibilityName(self,  color):
        #Deberá desaparecer el tres versiones despues de 20130228
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

class ConfigFile:
    def __init__(self, file):
        self.file=file
        self.splitterstate=''
        self.language="en"
        self.names=[]#Es un array separado de ##=##=## y siempre habrá 8
        #NAMES ES UN STRING DE PYTHON USAR S2Q Y Q2S
        self.names.append("Yellowy")
        self.names.append("Bluey")
        self.names.append("Redy")
        self.names.append("Greeny")
        self.names.append("Graye")
        self.names.append("Pinky")
        self.names.append("Orangy")
        self.names.append("Cyanny")
        self.lastupdate=datetime.date.today().toordinal()
        self.autosaves=10
        
        self.config=ConfigParser.ConfigParser()
        self.load()
        
    def load(self):
        """Cuando se carga si falla deberá coger los valores por decto"""
        try:
            self.config.read(self.file)
            self.splitterstate=base64.b64decode(self.config.get("frmMain", "splitter_state"))
            self.language=self.config.get("frmSettings", "language")
            stringa=base64.b64decode(self.config.get("frmInitGame", "names"))
            self.names=base64.b64decode(self.config.get("frmInitGame", "names")).split("##=##=##")
            self.lastupdate=self.config.getint("frmMain", "lastupdate")
        except:
            print ("No hay fichero de configuración")    
            
        try:
            self.autosaves=self.config.getint("frmSettings", "autosaves")
        except:
            print ("Error cargando autosaves")
            
    def save(self):
        if self.config.has_section("frmMain")==False:
            self.config.add_section("frmMain")
        if self.config.has_section("frmSettings")==False:
            self.config.add_section("frmSettings")
        if self.config.has_section("frmInitGame")==False:
            self.config.add_section("frmInitGame")
        self.config.set("frmSettings",  'language', self.language)
        self.config.set("frmSettings",  'autosaves', self.autosaves)
        self.config.set("frmMain",  'splitter_state', base64.b64encode(self.splitterstate))
        self.config.set("frmMain",  'lastupdate', self.lastupdate)
        cadena=""
        for n in self.names:
            cadena=cadena+n+"##=##=##"
        self.config.set("frmInitGame",  'names', base64.b64encode(cadena[:-8]))
        with open(self.file, 'w') as configfile:
            self.config.write(configfile)
            
class Casilla(QObject):
    def __init__(self, id, maxfichas, color,  position, rotate, rotatepn,  rampallegada, tipo, seguro, posfichas):
        QObject.__init__(self)
        self.id=id
        self.maxfichas=maxfichas
        self.posfichas=posfichas#es un array de vectores 3d de tamaño maxfichas
        self.color=color
        self.position=position
        self.rotate=rotate
        self.rotatepn=rotatepn #Rotar panel numerico
        self.rampallegada=rampallegada#booleano que indica si la casilla es de rampa de llegada
        self.tipo=tipo
        self.seguro=seguro# No se debe usar directamente ya que en ruta 1 solo es seguro si el jugador no tiene en casa
        self.buzon=[None]*self.maxfichas #Se crean los huecos y se juega con ellos para mantener la posicion
        self.oglname=self.id+18#Nombre usado para pick por opengl
        self.UltimaFichaEnLlegar=None#Puntero a un objeto ficha que es utilizado p.e. cuando se come la segunda ficha en la casilla de salida por un 5 obligado a salir
        
    def __repr__(self):
        return ("Casilla {0} con {1} fichas dentro".format(self.id, self.buzon_numfichas()))


    def jugadorPropietario(self, mem):
        #Rutas 1
        if self.id==5:
            return mem.jugadores.jugador("yellow")
        elif self.id==22:
            return mem.jugadores.jugador("blue")
        elif self.id==39:
            return mem.jugadores.jugador("red")
        elif self.id==56:
            return mem.jugadores.jugador("green")
        else:
            return None

    def esUnSeguroParaJugador(self, mem,  jugador):
        """Devuelve si la casilla es segura para el jugador pasado como parámetro ante un posible moviiento"""
        if self.id in mem.rutas.rutas1():
            propietario=self.jugadorPropietario(mem)
            if jugador==propietario:
                return True
            else:#color distinto
                if propietario.tieneFichasEnCasa() and self.buzon_numfichas()>0:
                    return False
                else:
                    return True
        else:
            if self.seguro==True:
                return True
            else:
                return False
            

    def dibujar(self, ogl):             
        def quad(p1, p2, p3, p4, color):
            ogl.qglColor(color.qcolor())
#            glNormal3f(1, 1, 1)
#            glColor3d(color.r, color.g, color.b)
            glTexCoord2f(0.0,0.0)
            glVertex3d(p1[0], p1[1], p1[2])
            glTexCoord2f(1.0,0.0)
            glVertex3d(p2[0], p2[1], p2[2])
            glTexCoord2f(1.0,1.0)
            glVertex3d(p3[0], p3[1], p3[2])
            glTexCoord2f(0.0,1.0)
            glVertex3d(p4[0], p4[1], p4[2])          
            
        def panelnumerico():
            def cuadrito(x, texture, rotation):
                glBindTexture(GL_TEXTURE_2D, texture)                
                glPushMatrix()
                glTranslated(self.position[0],self.position[1],self.position[2] )
                glRotated(self.rotate, 0, 0, 1 )            
                glBegin(GL_QUADS)
                ogl.qglColor(self.color.qcolor())
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
            #Cada cuadrante estará a 3x7 estara a 1x1 de ancho
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
                cuadrito(3, ogl.texNumeros[primero], rotation)
            elif len(str(self.id))==2:
                cuadrito(2.5, ogl.texNumeros[primero], rotation)
                cuadrito(3.5, ogl.texNumeros[segundo], rotation)
            elif len(str(self.id))==3:
                cuadrito(2, ogl.texNumeros[primero], rotation)
                cuadrito(3, ogl.texNumeros[segundo], rotation)
                cuadrito(4, ogl.texNumeros[tercero], rotation)
                
            glDisable(GL_TEXTURE_2D);
            
        def border(a, b, c, d, color):    
            glBegin(GL_LINE_LOOP)
            glColor3d(color.r, color.g, color.b)
            glVertex3d(a[0], a[1], a[2])
            glVertex3d(b[0], b[1], b[2])
            glVertex3d(c[0], c[1], c[2])
            glVertex3d(d[0], d[1], d[2])
            glEnd()
        def tipo_inicio():        
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (21, 0, 0)
            v3 = (21, 21, 0)
            v4 = (0, 21, 0)
            v5 = (0, 0, 0.2)
            v6 = (21, 0, 0.2)
            v7 = (21, 21, 0.2)
            v8 = (0, 21, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5, Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170))      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
            
        def tipo_inicio6():        
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            glBegin(GL_QUADS)
            b=21*math.sin(math.pi/6)
            c=21*math.tan(math.pi/6)*math.sin(math.pi/6)
            d=21*math.cos(math.pi/6)
            v1 = (-b, -d, 0)
            v2 = (0, -c-d, 0)
            v3 = (b, -d, 0)
            v4 = (0, 0, 0)
            v5 = (-b, -d, 0.2)
            v6 = (0, -c-d, 0.2)
            v7 = (b, -d, 0.2)
            v8 = (0, 0, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5, Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170))      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()                 
        def tipo_inicio8():        
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            glBegin(GL_QUADS)
            a22c5=math.pi/8
            a=21*math.sin(a22c5)
            c=21*math.tan(a22c5)*math.sin(a22c5)
            h=21/math.cos(a22c5)
            v1 = (0, 0, 0)
            v2 = (a, -c, 0)
            v3 = (2*a, 0, 0)
            v4 = (a, h-c, 0)
            v5 = (0, 0, 0.2)
            v6 = (a, -c, 0.2)
            v7 = (2*a, 0, 0.2)
            v8 = (a, h-c, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5, Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170))      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()            
    
        def tipo_normal():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )            
            if self.seguro==True and self.rampallegada==False:
                glEnable(GL_TEXTURE_2D);
                glBindTexture(GL_TEXTURE_2D, ogl.texDecor[2])
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (7, 3, 0)
            v4 = (0, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (7, 3, 0.2)
            v8 = (0, 3, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5,Color(70, 70, 70) )      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
            glPopName();
            glPopMatrix()
            glDisable(GL_TEXTURE_2D)
            panelnumerico()
    
        def tipo_oblicuoi(lado):
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (7, 3, 0)
            v4 = (lado, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (7, 3, 0.2)
            v8 = (lado, 3, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
            panelnumerico()
    
        def tipo_oblicuod(lado):
            """Como parametro se recibe el lado recortado"""
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (lado, 3, 0)
            v4 = (0, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (lado, 3, 0.2)
            v8 = (0, 3, 0.2)
    
            quad(v1, v2, v3, v4,self.color )      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      

            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
            panelnumerico()
            
        def tipo_final():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            if ogl.__class__.__name__!="wdgShowObject":#En caso de que no sea wdgShowObject
                if ogl.mem.maxplayers==6:
                    glScaled(2*math.tan(math.pi/6)*(21*math.cos(math.pi/6)-3)/15, (21*math.cos(math.pi/6)-3)/7.5, 1)
                elif ogl.mem.maxplayers==8:
                    glScaled((21-2*3*math.tan(math.pi/8))/15.0, ((10.5/math.tan(math.pi/8))-3)/7.5, 1)
            
            
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (0,  0, 0)
            v3 = (15, 0, 0)
            v4 = (7.5, 7.5, 0)
            v5 = (0, 0, 0.2)
            v6 = (0, 0, 0.2)
            v7 = (15, 0, 0.2)
            v8 = (7.5, 7.5, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
        ##################################
        if ogl.__class__.__name__=="wdgShowObject":#En caso de wdgShowObject en la ayuda
            if self.tipo==0:
                tipo_inicio8()
            elif self.tipo==1:
                tipo_final()
            elif self.tipo==2:
                tipo_oblicuoi(3)
            elif self.tipo==4:
                tipo_oblicuod(4)
            else:
                tipo_normal()
            return
        
        
        if self.tipo==0:
            if ogl.mem.maxplayers==4:
                tipo_inicio()
            elif ogl.mem.maxplayers==6:
                tipo_inicio6()
            elif ogl.mem.maxplayers==8:
                tipo_inicio8()
        elif self.tipo==1:
            tipo_final()
        elif self.tipo==2:
            if ogl.mem.maxplayers==4:
                tipo_oblicuoi(3)
            elif ogl.mem.maxplayers==6:
                tipo_oblicuoi(3.0/math.tan(math.pi/3))
            elif ogl.mem.maxplayers==8:
                tipo_oblicuoi(3.0*math.tan(math.pi/8))
        elif self.tipo==4:
            if ogl.mem.maxplayers==4:
                tipo_oblicuod(4)
            elif ogl.mem.maxplayers==6:
                tipo_oblicuod(7-3.0*math.tan(math.pi/6))
            elif ogl.mem.maxplayers==8:
                tipo_oblicuod(7-3.0*math.tan(math.pi/8))
        else:
            tipo_normal()
            
    def dibujar_fichas(self, ogl):
        if self.buzon_numfichas()>0:
            for i, f in enumerate(self.buzon):       
                if f!=None:
                    f.dibujar(ogl, i)

    def tieneBarrera(self):
        """Devuelve un booleano, las fichas de la barrera se pueden sacar del buzón"""
        if self.tipo not in (0, 1):#Casilla inicio y final
            if self.maxfichas==2:
                if self.buzon_numfichas()==2:
                    if self.buzon[0].jugador==self.buzon[1].jugador:
                        return True
        return False

    def posicionLibreEnBuzon(self):
        """Función que devuelve la posición de un sitio libre con un entero. En caso negativo devuelve -1"""
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
        """Función que devuelve el número de fichas en el buzón"""
        resultado=0
        for f in self.buzon:
            if f!=None:
                resultado=resultado+1
        return resultado

    def buzon_fichas(self):
        """Como ahora puede haber una ficha y estar en buzon[1] se hace necesario esta función.
        Devuelve una lista de fichas con una tupla (posicion, ficha)"""
        resultado=[]
        for i, f in enumerate(self.buzon):
            if f!=None:
                resultado.append((i, f))
        return resultado

class Mem:
    def __init__(self, maxplayers):     
        self.maxplayers=maxplayers
#        self.casillas=None#Lista cuya posicion coincide con el id del objeto jugador que lleva dentro
        self.dic_fichas={}
        self.colores=SetColores()
        self.jugadores=SetJugadores(self)
        self.dic_rutas={}
        self.dado=Dado()
        self.selFicha=None
        self.inittime=None#Tiempo inicio partida
        self.cfgfile=None#fichero configuración que se crea en glparchis.py
           
        self.mediaObject = None
        self.sound=True#Enciende o apaga el sonido
        parent=QCoreApplication.instance()
        self.mediaObject = Phonon.MediaObject(parent)
        audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, parent)
        Phonon.createPath(self.mediaObject, audioOutput)
        

    def play(self, sound):
        if self.sound==True:
            so=os.environ['glparchisso']
            if so=="bin.windows" or so=="bin.linux":
                url= sound + ".wav"
            elif so=="src.windows":
                url="../share/glparchis/sounds/"+sound+".wav"
            elif so=="src.linux":
                url="/usr/share/glparchis/sounds/"+sound+".wav"
            self.mediaObject.setCurrentSource(Phonon.MediaSource(url))
            self.mediaObject.play()
            time.sleep(0.4)
            QCoreApplication.processEvents();    
   
    def generar_fichas(self):
        """Debe generarse despuñes de jugadores"""
        id=0
        for ic, c in enumerate(self.colores.arr):
            j=self.jugadores.jugador(c.name)
            j.ruta=self.rutas.ruta(ic)
            for i in range(4):
                self.dic_fichas[str(id)]=Ficha(id, i, c, self.jugadores.jugador(c.name), j.ruta)
                j.fichas.arr.append(self.dic_fichas[str(id)])#Rellena el SetFichas del jugador
                id=id+1

            
    def generar_jugadores(self):
        for c in self.colores.arr:
            j=Jugador(c)
            self.jugadores.arr.append(j)
            j.dado=self.dado

    def fichas(self, name=None):
        if name==None:
            return dic2list(self.dic_fichas)
        else:
            return self.dic_fichas[str(name)]
#
#    def casillas(self, name=None):
#        if name==None:
#            return dic2list(self.dic_casillas)
#        else:
#            return self.dic_casillas[str(name)]
#            
                        

            
    def save(self, filename):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = ConfigParser.ConfigParser()
        
        config.add_section("game")
        config.set("game", 'playerstarts',self.jugadores.actual.color.name)
        config.set("game",  "numplayers",  self.maxplayers)
        config.set("game", 'fakedice','')
        config.set("game", 'fileversion','1.0')
        for i, j in enumerate(self.jugadores.arr):
            config.add_section("jugador{0}".format(i))
            config.set("jugador{0}".format(i),  'ia', int(j.ia))
            config.set("jugador{0}".format(i),  'name', j.name)
            config.set("jugador{0}".format(i),  'plays', int(j.plays))
            if self.jugadores.jugador('yellow').plays==True:
                config.set("jugador{0}".format(i),  'rutaficha1', j.fichas.arr[0].posruta)
                config.set("jugador{0}".format(i),  'rutaficha2',  j.fichas.arr[1].posruta)
                config.set("jugador{0}".format(i),  'rutaficha3',  j.fichas.arr[2].posruta)
                config.set("jugador{0}".format(i),  'rutaficha4',  j.fichas.arr[3].posruta)
        with open(filename, 'w') as configfile:
            config.write(configfile)            
        os.chdir(cwd)


            
            
    def load(self, filename):       
        def error():           
            QMessageBox.information(None, "glParchis", QApplication.translate("glparchis", u"Este fichero es de una versión antigua o está estropeado. No puede ser cargado.", None, QApplication.UnicodeUTF8))
            print("Error loading file")
            os.chdir(cwd)

        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = ConfigParser.ConfigParser()
        config.read(filename)
        
        try:
            fileversion=config.get("game", "fileversion")
            self.maxplayers=config.getint("game",  "numplayers")
        except:
            fileversion=None
            error()
            return False
        if fileversion!="1.0":#Ir cambiando según necesidades
            error()
            return False
        
        for i, j in enumerate(self.jugadores.arr):
            j.name=config.get("jugador{0}".format(i), "name")
            j.ia=i2b(config.getint("jugador{0}".format(i), "ia"))
            j.plays=i2b(config.getint("jugador{0}".format(i), "plays"))
            
            if j.plays==True:
                j.fichas.arr[0].mover(config.getint("jugador{0}".format(i), "rutaficha1"), False,  True)
                j.fichas.arr[1].mover(config.getint("jugador{0}".format(i), "rutaficha2"), False,  True)
                j.fichas.arr[2].mover(config.getint("jugador{0}".format(i), "rutaficha3"), False,  True)
                j.fichas.arr[3].mover(config.getint("jugador{0}".format(i), "rutaficha4"), False,  True)

        fake=config.get("game", 'fakedice')
        if fake!="":
            for i in  fake.split(";")  :
                self.dado.fake.append(int(i))

        self.jugadores.actual=self.jugadores.jugador(config.get("game", 'playerstarts'))    
        self.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa

        

        os.chdir(cwd)
        return True

class Mem8(Mem):    
    def __init__(self):
        Mem.__init__(self, 8)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=SetCasillas(8, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        
        self.circulo=Circulo(self, 136)




                   

class Mem6(Mem):    
    def __init__(self):
        Mem.__init__(self, 6)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=SetCasillas(6, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        
        self.circulo=Circulo(self, 102)

class Mem4(Mem):
    def __init__(self):
        Mem.__init__(self, 4)
        self.colores.generar_colores(self.maxplayers)
        self.generar_jugadores()
        self.casillas=SetCasillas(4, self)
        self.rutas=SetRutas(self.maxplayers, self)
        self.generar_fichas()
        
        self.circulo=Circulo(self, 68)
            
def dic2list(dic):
    """Función que convierte un diccionario pasado como parametro a una lista de objetos"""
    resultado=[]
    for k,  v in dic.items():
        resultado.append(v)
    return resultado


def cargarQTranslator(cfgfile):  
    """language es un string"""
    so=os.environ['glparchisso']
    if so=="src.linux":
        cfgfile.qtranslator.load("/usr/share/glparchis/glparchis_" + cfgfile.language + ".qm")
    elif so=="src.windows":
        cfgfile.qtranslator.load("../share/glparchis/glparchis_" + cfgfile.language + ".qm")
    elif so=="bin.windows" or so=="bin.linux":
        cfgfile.qtranslator.load("glparchis_" + cfgfile.language + ".qm")
    qApp.installTranslator(cfgfile.qtranslator);
    
def developing():
    """Función que permite avanzar si hay un parametro y da un aviso e interrumpe si no, se debe poner un if en donde se use"""
    if len (sys.argv)==1:
        m=QMessageBox()
        m.setIcon(QMessageBox.Information)
        m.setText(QApplication.translate("frmMain", "Esta opción se está desarrollando", None, QApplication.UnicodeUTF8))
        m.exec_()            
        return False
    return True
