#-*- coding: utf-8 -*- 

from OpenGL import GL,  GLU
import os,  random,   ConfigParser
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *

def colorid(color):
    if color=="yellow":
        return 0
    elif color=="blue":
        return 1
    elif color=="red":
        return 2
    elif color=="green":
        return 3

        
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





version="20120805"
cfgfile=os.environ['HOME']+ "/.glparchis/glparchis.cfg"
lastfile=os.environ['HOME']+ "/.glparchis/last.glparchis"



class Dado():    
    def __init__(self):
        self.fake=[]
        
    def tirar(self):
        if len(self.fake)>0:
            resultado=self.fake[0]
            self.fake.remove(self.fake[0])
        else:
            resultado= int(random.random()*6)+1
        return resultado
        
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
                    

class Jugadores:
    def __init__(self):
        self.actual=None
        self.arr=[]
    def cambiar_jugador_actual(self):
        return
        
class TiradaHistorica:
    """Estudio estadistico de tiradas. Lleva un array con todas los objetos TiradaTurno
    Se graba cuando se tira ya que es un objeto TiradaTurno que se vincula en el array de TiradaHistorica"""
    def __init__(self):
        self.arr=[]
        
class Tirada:
    """Lanzamiento individual de un dado"""
    def __init__(self, jugador, valor,  tipo=None):
        self.jugador=jugador
        self.valor=valor
        self.tipo=tipo#None desconocido 1 turno normal, dos por seis, tres por comer, cuatro por meter
        #EL TIPO SE PONE CUANDO SE PUEDA

class TiradaTurno:
    """Objeto que recoge todos las tiradas de un turno"""
    def __init__(self):
        self.jugador=None
        self.arr=[]
        
    def tresSeises(self):
        """Funci´on que devuelve un booleano seg´un haya o no salido 3 seises"""
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
        if len(self.arr)>0:
            return self.arr[len(self.arr)-1].valor
        else:
            return None

class Jugador:
    def __init__(self,  color):
        self.name=None
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

    def __repr__(self):
        return "Jugador {0}".format(self.color.name)

    def log(self, l):
#        self.inittime=datetime.timedelta(days=0)#inittime actualmente esta en mem y no quiero pasrlo como parametro
#        l=str(datetime.datetime.now()-self.inittime)[2:-7]+ " " + l
        self.logturno.append( l)
        self.loghistorico.append(l)
        
    def TirarDado(self):
        """Tira el dado lo almacena en tirada, tiradaturno e historico y devuelve el valor"""
        tirada=Tirada(self, self.dado.tirar())
        self.tiradaturno.arr.append(tirada)
        if self.tiradaturno not in self.tiradahistorica.arr:
            self.tiradahistorica.arr.append(self.tiradaturno)
        return tirada.valor

        
    def DeboAbrirBarrera(self):
        """Devuelve si el jugador est´a obligado a abrir barrera"""
        for f in self.fichas.arr:
            if f.casilla().tieneBarrera()==True:
                return True
        return False
#        if valordado==6:
#            barreras=self.Barreras(mem.jugadoractual)
#            if len(barreras)!=0 :
#                if self.id_casilla() not in barreras:
#                    self.log(self.trUtf8(pre+"No se puede mover, debes abrir barrera"))
#                    return (False, 0)

    def HaGanado(self):
        for f in self.fichas.arr:
            if f.estaEnMeta()==False:
                return False
        return True
        
            
    def qicon(self):
        ico = QIcon()
        ico.addPixmap(self.qpixmap(), QIcon.Normal, QIcon.Off) 
        return ico
    
    def qpixmap(self):
        """Devuelve un pixmap del color de la ficha"""
        if self.color.name=="yellow":
            return QPixmap(":/glparchis/fichaamarilla.png")
        elif self.color.name=="blue":
            return QPixmap(":/glparchis/fichaazul.png")
        elif self.color.name=="green":
            return QPixmap(":/glparchis/fichaverde.png")
        elif self.color.name=="red":
            return QPixmap(":/glparchis/ficharoja.png")
class Ruta:
    def __init__(self):
        self.arr=[] #Array ordenado
    

class SetFichas:
    """Agrupación de fichas"""
    def __init__(self):
        self.arr=[]

    def algunaPuedeMover(self, mem):
        for f in self.arr:
            if f.puedeMover(mem)[0]==True:
                return True
        return False
    
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
        
class Ficha(QGLWidget):
    def __init__(self, id, number,  color, jugador, ruta):
        """El identificador de la ficha viene dado por el nombre del color y el id (numero de creacion), se genera en la clase Mem"""
        QGLWidget.__init__(self)
        self.color=color
        self.id=id
        self.number=number#indice dentro de las fichas de mismo color.
        self.ruta=ruta
        self.posruta=0#pOSICION EN LA RUTA
        self.ficha=GLU.gluNewQuadric();
        self.jugador=jugador
#        self.casilla=casilla
#        self.id=fichas_name2id(name)
        
    def __repr__(self):
        return  "Ficha {0} del jugador {1}".format(self.id, self.jugador.color.name)
        
    def puedeMover(self, mem):
        #Es ficha del jugador actual
        if  self.jugador!=mem.jugadoractual:             
            mem.jugadoractual.logturno.append(self.trUtf8("No es del jugador actual"))
            return (False, 0)
        
        #Calcula el movimiento
        if mem.jugadoractual.movimientos_acumulados!=None:
            movimiento=mem.jugadoractual.movimientos_acumulados
        else:        
            movimiento=self.calculaValorAMover(self.jugador.tiradaturno.ultimoValor())
        
        if movimiento==0:
            return (False, 0)

        #Comprueba que no tenga obligación de abrir barrera
        if mem.jugadoractual.DeboAbrirBarrera()==True:
            mem.jugadoractual.logturno.append(self.trUtf8("No se puede mover, debes abrir barrera"))
            return (False, 0)          

        #Esta en casa y puede mover
        if self.estaEnCasa()==True:
            if movimiento!=5: #Saco un 5
                mem.jugadoractual.logturno.append(self.trUtf8("Necesita sacar un 5 para mover esta ficha"))
                return (False, 0)
                        
        #se ha pasado la meta
        if self.posruta+movimiento>72:
            mem.jugadoractual.logturno.append(self.trUtf8("Se ha pasado la meta"))
            return (False, 0)
                
                
        #Rastrea todas las casillas de paso en busca de barrera.
        for i in range(self.posruta, self.posruta+movimiento+1): 
            if self.ruta.arr[i].tieneBarrera()==True:
                mem.jugadoractual.logturno.append(self.trUtf8("Hay una barrera"))
                return (False, 0)

        #Comprueba si hay sitio libre
        if self.ruta.arr[self.posruta+movimiento].haySitioEnBuzon()==False:
            mem.jugadoractual.logturno.append(self.trUtf8("No hay espacio en la casilla"))
            return (False, 0)
            
        mem.jugadoractual.logturno.append(self.trUtf8("Puede mover %1").arg(str(movimiento)))
        return (True, movimiento)
        
    def mover(self, ruta, controllastficha=True,  startgame=False):
        casillaorigen=self.ruta.arr[self.posruta]
        casilladestino=self.ruta.arr[ruta]        
#        print ("antes mover ",  self,  len(casillaorigen.buzon),  len(casilladestino.buzon))
        self.posruta=ruta
        if controllastficha==True:
            self.jugador.LastFichaMovida=self
        if startgame==False:
            casillaorigen.buzon.remove(self)
        casilladestino.buzon.append(self)
#        print ("despu´es mover ",  self, len(casillaorigen.buzon),  len(casilladestino.buzon))


            
    def come(self,  ruta):
        """ruta, es la posición de ruta de ficha en la que come. Como ya se ha movido, come si puede y devuelve True, en caso contrario False"""
        if ruta>72:
            print ("en como se ha sobrepasado el 72")
            return False
        casilladestino=self.ruta.arr[ruta]
        
        if casilladestino.seguro==True:
            return False
        
        if len(casilladestino.buzon)==2:
            ficha1=casilladestino.buzon[0]
            ficha2=casilladestino.buzon[1]
            if ficha1.jugador!=self.mem.jugadoractual:
                fichaacomer=ficha1
            elif ficha2.jugador!=self.mem.jugadoractual:
                fichaacomer=ficha2
            else:
                return False
            fichaacomer.mover(0, False)
            self.mem.jugadoractual.movimientos_acumulados=20
            self.mem.jugadoractual.log(self.trUtf8("He comido la ficha %1").arg(fichaacomer.name))
            return True
                
            
            
    def mete(self):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""      
        if self.estaEnMeta():
            self.jugador.movimientos_acumulados=10
            self.jugador.log(self.trUtf8("He metido la ficha %1").arg(self.name))
            return True
        return False

    def casilla(self):
        """Devuelve el objeto casilla en el que se encuentra la ficha"""
        return self.ruta.arr[self.posruta]

        
    def estaEnCasa(self):
        if self.ruta==0:
            return True
        return False
        
    def calculaValorAMover(self, valordado):
        """Calcula el valor a mover la ficha teniendo en cuenta su posicion en la ruta, si han salido todas las fichas y el valor del dado"""
        if self.estaEnCasa() and valordado==5:
            return 1
        else:
            return 0
        if self.jugador.fichas.TodasFichasFueraDeCasa()==True and valordado==6:
            return 7
        return valordado

    def estaEnMeta(self):
        if self.posruta==72:
            return True
        return False

#    def fichas_name2id(self, name):
#        if name=="yellow1": return 0
#        if name=="yellow2": return 1
#        if name=="yellow3": return 2
#        if name=="yellow4": return 3
#        if name=="blue1": return 4
#        if name=="blue2": return 5
#        if name=="blue3": return 6
#        if name=="blue4": return 7
#        if name=="red1": return 8
#        if name=="red2": return 9
#        if name=="red3": return 10
#        if name=="red4": return 11
#        if name=="green1": return 12
#        if name=="green2": return 13
#        if name=="green3": return 14
#        if name=="green4": return 15
    
    def dibujar(self, posicionBuzon):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(self.id);
        print (self.id)
        if posicionBuzon==None:#Para frmAcercade
            p=(0, 0, 0)
        else:
#            print ("En dibujar ficha. posicion ruta {0}. posicion buzon. posiciones de fichas {2}".format(self.posruta,  posicionBuzon, self.ruta.arr[self.posruta].posfichas))
            p=self.ruta.arr[self.posruta].posfichas[posicionBuzon]
        GL.glTranslated(p[0], p[1], p[2])
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        self.qglColor(Color(255, 255, 0).qcolor().dark())
        GLU.gluQuadricDrawStyle (self.ficha, GLU.GLU_FILL);
        GLU.gluQuadricNormals (self.ficha, GLU.GLU_SMOOTH);
        GLU.gluQuadricTexture (self.ficha, True);
        self.qglColor(self.color.qcolor().dark())
        GLU.gluCylinder (self.ficha, 1.4, 1.4, 0.5, 16, 5)
        GL.glTranslated(0, 0, 0.5)
        self.qglColor(Color(70, 70, 70).qcolor())
        GLU.gluDisk(self.ficha, 0, 1.4, 16, 5)
        self.qglColor(self.color.qcolor().dark())
        GL.glTranslated(0, 0, -0.5)
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        GLU.gluDisk(self.ficha, 0, 1.40, 16, 5)
        GL.glPopName();
        GL.glPopMatrix()


class Tablero(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.position=(-1, -1, 0)


    def dibujar(self):
        def quad(p1, p2, p3, p4, color):
            self.qglColor(color.qcolor())
    
            GL.glVertex3d(p1[0], p1[1], p1[2])
            GL.glVertex3d(p2[0], p2[1], p2[2])
            GL.glVertex3d(p3[0], p3[1], p3[2])
            GL.glVertex3d(p4[0], p4[1], p4[2])        
        GL.glPushMatrix()
        GL.glTranslated(self.position[0],  self.position[1],  self.position[2])
        GL.glBegin(GL.GL_QUADS)
        v1 = (0, 0, 0)
        v2 = (65, 0, 0)
        v3 = (65, 65, 0)
        v4 = (0, 65, 0)
        v5 = (0, 0, 0.5)
        v6 = (65, 0, 0.5)
        v7 = (65, 65, 0.5)
        v8 = (0, 65, 0.5)
        color=Color(0, 64, 64)
        quad(v4, v3, v2, v1, color)      
        quad(v5, v6, v7, v8, color)      
        quad(v5, v8, v4, v1, color)      
        quad(v2, v3, v7, v6, color)      
        quad(v1, v2, v6, v5, color)      
        quad(v8, v7, v3, v4, color)      

        GL.glEnd()
        GL.glPopMatrix()
        
        
class Color:
    def __init__(self,   r,  g, b, name=None):
        self.name=name
        self.r=r
        self.g=g
        self.b=b
#    def Color(self):
#        return Color(self.r, self.g, self.b)      
    def glcolor(self):
        GL.glColor3d(self.r, self.g, self.b)
        
    def qcolor(self):
        return QColor(self.r, self.g, self.b, 125)
        
class Casilla(QGLWidget):
    def __init__(self, id, maxfichas, color,  position, rotate, rampallegada, tipo, seguro, posfichas):
        QGLWidget.__init__(self)
        self.id=id
        self.maxfichas=maxfichas
        self.posfichas=posfichas#es un array de vectores 3d de tamaño maxfichas
        self.color=color
        self.position=position
        self.rotate=rotate
        self.rampallegada=rampallegada
        self.tipo=tipo
        self.seguro=seguro
        self.buzon=[]

    def dibujar(self):                            
        def quad(p1, p2, p3, p4, color):
            self.qglColor(color.qcolor())
            GL.glVertex3d(p1[0], p1[1], p1[2])
            GL.glVertex3d(p2[0], p2[1], p2[2])
            GL.glVertex3d(p3[0], p3[1], p3[2])
            GL.glVertex3d(p4[0], p4[1], p4[2])
            
        def border(a, b, c, d, color):    
            GL.glBegin(GL.GL_LINE_LOOP)
            self.qglColor(color.qcolor())
            GL.glVertex3d(a[0], a[1], a[2]+0.0001)
            GL.glVertex3d(b[0], b[1], b[2]+0.0001)
            GL.glVertex3d(c[0], c[1], c[2]+0.0001)
            GL.glVertex3d(d[0], d[1], d[2]+0.0001)
            GL.glEnd()
        def tipo_inicio():        
            GL.glInitNames();
            GL.glPushMatrix()
            GL.glPushName(Name.casilla[self.id]);
            GL.glTranslated(self.position[0],self.position[1],self.position[2] )
            GL.glRotated(self.rotate, 0, 0, 1 )
            GL.glBegin(GL.GL_QUADS)
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
    
            GL.glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            GL.glPopName();
            GL.glPopMatrix()
    
        def tipo_normal():
            GL.glInitNames();
            GL.glPushMatrix()
            GL.glPushName(Name.casilla[self.id]);
            GL.glTranslated(self.position[0],self.position[1],self.position[2] )
            GL.glRotated(self.rotate, 0, 0, 1 )

            GL.glBegin(GL.GL_QUADS)
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
    
            GL.glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
            GL.glPopName();
            GL.glPopMatrix()
    
        def tipo_oblicuoi():
            GL.glInitNames();
            GL.glPushMatrix()
            GL.glPushName(Name.casilla[self.id]);
            GL.glTranslated(self.position[0],self.position[1],self.position[2] )
            GL.glRotated(self.rotate, 0, 0, 1 )

            GL.glBegin(GL.GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (7, 3, 0)
            v4 = (3, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (7, 3, 0.2)
            v8 = (3, 3, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            GL.glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            GL.glPopName();
            GL.glPopMatrix()
    
        def tipo_oblicuod():
            GL.glInitNames();
            GL.glPushMatrix()
            GL.glPushName(Name.casilla[self.id]);
            GL.glTranslated(self.position[0],self.position[1],self.position[2] )
            GL.glRotated(self.rotate, 0, 0, 1 )

            GL.glBegin(GL.GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (4, 3, 0)
            v4 = (0, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (4, 3, 0.2)
            v8 = (0, 3, 0.2)
    
            quad(v1, v2, v3, v4,self.color )      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      

            GL.glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            GL.glPopName();
            GL.glPopMatrix()
            
        def tipo_final():
            GL.glInitNames();
            GL.glPushMatrix()
            GL.glPushName(Name.casilla[self.id]);
            GL.glTranslated(self.position[0],self.position[1],self.position[2] )
            GL.glRotated(self.rotate, 0, 0, 1 )
            
            GL.glBegin(GL.GL_QUADS)
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
    
            GL.glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            GL.glPopName();
            GL.glPopMatrix()
        ##################################
        if self.tipo==0:
            tipo_inicio()
        elif self.tipo==1:
            tipo_final()
        elif self.tipo==2:
            tipo_oblicuoi()
        elif self.tipo==4:
            tipo_oblicuod()
        else:
            tipo_normal()
            
    def dibujar_fichas(self):
        if len(self.buzon)>0:
            for i, f in enumerate(self.buzon):       
                f.dibujar(i)
                print (i, f)


    def tieneBarrera(self):
        """Devuelve un booleano, las fichas de la barrera se pueden sacar del buz´on"""
        if self.tipo not in (0, 1):#Casilla inicio y final
            if self.maxfichas==2:
                if len(self.buzon)==2:
                    if self.buzon[0].jugador==self.buzon[1].jugador:
                        return True
        return False

    def haySitioEnBuzon(self):
        if len(self.buzon)<self.maxfichas:
            return True
        return False
#
#
#    def hayBarrera(self, jugador):
#        """Devuelve False si no y  una lista con las dos fichas si si"""
#        if self.buzon
#        resultado =[]
#        for f in jugador.fichas:
#            casilla=self.dic_casillas[jugador.fichas[f].id_casilla()]
#            if casilla.tieneBarrera()==True:
#                resultado.append(casilla.id)
#        return resultado

class Mem4:
    def __init__(self):
        self.dic_jugadores={}#Lista cuya posicion coincide con el id del objeto jugador que lleva dentro
        self.dic_casillas={}#Lista cuya posicion coincide con el id del objeto jugador que lleva dentro
        self.dic_fichas={}
        self.dic_colores={}
        self.dic_rutas={}
        self.dado=Dado()
        self.jugadoractual=None
        self.selFicha=None
        self.inittime=None#Tiempo inicio partida
        
        self.generar_colores()
        self.generar_jugadores()
        self.generar_casillas()
        self.generar_rutas()
        self.generar_fichas()
        
    def generar_colores(self):
        self.dic_colores["red"]=Color(255, 0, 0, "red")
        self.dic_colores["yellow"]=Color( 255, 255, 0, "yellow")
        self.dic_colores["blue"]=Color(0, 0, 255, "blue")
        self.dic_colores["green"]=Color(0, 255, 0, "green")

    def colores(self, name=None):
        if name==None:
            return dic2list(self.dic_colores)
        else:
            return self.dic_colores[str(name)]

    def generar_rutas(self):
        ruta=[None]*73
        ruta[0]=(101, 102, 103, 104)
        ruta[1]=(5, 22, 39, 56)
        ruta[2]=(6, 23, 40, 57)
        ruta[3]=(7, 24, 41, 58)
        ruta[4]=(8, 25, 42, 59)
        ruta[5]=(9, 26, 43, 60)
        ruta[6]=(10, 27, 44, 61)
        ruta[7]=(11, 28, 45, 62)
        ruta[8]=(12, 29, 46, 63)
        ruta[9]=(13, 30, 47, 64)
        ruta[10]=(14, 31, 48, 65)
        ruta[11]=(15, 32, 49, 66)
        ruta[12]=(16, 33, 50, 67)
        ruta[13]=(17, 34, 51, 68)
        ruta[14]=(18, 35, 52, 1)
        ruta[15]=(19, 36, 53, 2)
        ruta[16]=(20, 37, 54, 3)
        ruta[17]=(21, 38, 55, 4)
        ruta[18]=(22, 39, 56, 5)
        ruta[19]=(23, 40, 57, 6)
        ruta[20]=(24, 41, 58, 7)
        ruta[21]=(25, 42, 59, 8)
        ruta[22]=(26, 43, 60, 9)
        ruta[23]=(27, 44, 61, 10)
        ruta[24]=(28, 45, 62, 11)
        ruta[25]=(29, 46, 63, 12)
        ruta[26]=(30, 47, 64, 13)
        ruta[27]=(31, 48, 65, 14)
        ruta[28]=(32, 49, 66, 15)
        ruta[29]=(33, 50, 67, 16)
        ruta[30]=(34, 51, 68, 17)
        ruta[31]=(35, 52, 1, 18)
        ruta[32]=(36, 53, 2, 19)
        ruta[33]=(37, 54, 3, 20)
        ruta[34]=(38, 55, 4, 21)
        ruta[35]=(39, 56, 5, 22)
        ruta[36]=(40, 57, 6, 23)
        ruta[37]=(41, 58, 7, 24)
        ruta[38]=(42, 59, 8, 25)
        ruta[39]=(43, 60, 9, 26)
        ruta[40]=(44, 61, 10, 27)
        ruta[41]=(45, 62, 11, 28)
        ruta[42]=(46, 63, 12, 29)
        ruta[43]=(47, 64, 13, 30)
        ruta[44]=(48, 65, 14, 31)
        ruta[45]=(49, 66, 15,  32)
        ruta[46]=(50, 67, 16 , 33)
        ruta[47]=(51, 68, 17 , 34)
        ruta[48]=(52, 1, 18 , 35)
        ruta[49]=(53, 2, 19, 36)
        ruta[50]=(54, 3, 20, 37)
        ruta[51]=(55, 4, 21, 38)
        ruta[52]=(56, 5, 22, 39)
        ruta[53]=(57, 6, 23, 40)
        ruta[54]=(58, 7, 24, 41)
        ruta[55]=(59, 8, 25, 42)
        ruta[56]=(60, 9, 26, 43)
        ruta[57]=(61, 10, 27, 44)
        ruta[58]=(62, 11, 28, 45)
        ruta[59]=(63, 12, 29, 46)
        ruta[60]=(64, 13, 30, 47)
        ruta[61]=(65, 14, 31, 48)
        ruta[62]=(66, 15, 32, 49)
        ruta[63]=(67, 16, 33, 50)
        ruta[64]=(68, 17, 34, 51)
        ruta[65]=(69, 77, 85, 93)
        ruta[66]=(70, 78, 86, 94)
        ruta[67]=(71, 79, 87, 95)
        ruta[68]=(72, 80, 88, 96)
        ruta[69]=(73, 81, 89, 97)
        ruta[70]=(74, 82, 90, 98)
        ruta[71]=(75, 83, 91, 99)
        ruta[72]=(76, 84, 92, 100)
        
        self.dic_rutas["yellow"]=Ruta()
        self.dic_rutas["red"]=Ruta()
        self.dic_rutas['blue']=Ruta()
        self.dic_rutas['green']=Ruta()
        for r in ruta:
            self.dic_rutas["yellow"].arr.append(self.casillas(r[0]))
            self.dic_rutas["red"].arr.append(self.casillas(r[2]))
            self.dic_rutas['blue'].arr.append(self.casillas(r[1]))
            self.dic_rutas['green'].arr.append(self.casillas(r[3]))
            
    def rutas(self, name=None):
        if name==None:
            return dic2list(self.dic_rutas)
        else:
            return self.dic_rutas[str(name)]


    def generar_jugadores(self):
        for c in self.colores():
            self.dic_jugadores[str(c.name)]=Jugador(c)
            self.dic_jugadores[str(c.name)].dado=self.dado
            
    def jugadores(self, name=None):
        if name==None:
            return dic2list(self.dic_jugadores)
        else:
            return self.dic_jugadores[str(name)]
        
    def generar_fichas(self):
        """Debe generarse despuñes de jugadores"""

        id=0
        for c in self.colores():
            for i in range(4):
                self.dic_fichas[str(id)]=Ficha(id, i, c, self.jugadores(c.name), self.rutas(c.name))
                self.jugadores(c.name).fichas.arr.append(self.dic_fichas[str(id)])#Rellena el SetFichas del jugador
                id=id+1

    def fichas(self, name=None):
        if name==None:
            return dic2list(self.dic_fichas)
        else:
            return self.dic_fichas[str(name)]
            
            
    def save(self, filename):
        config = ConfigParser.ConfigParser()
        config.add_section("yellow")
        config.set("yellow",  'ia', int(self.jugadores('yellow').ia))
        config.set("yellow",  'name', self.jugadores('yellow').name)
        config.set("yellow",  'plays', int(self.jugadores('yellow').plays))
        if self.jugadores('yellow').plays==True:
            config.set("yellow",  'rutaficha1', self.jugadores('yellow').fichas.arr[0].posruta)
            config.set("yellow",  'rutaficha2',  self.jugadores('yellow').fichas.arr[1].posruta)
            config.set("yellow",  'rutaficha3',  self.jugadores('yellow').fichas.arr[2].posruta)
            config.set("yellow",  'rutaficha4',  self.jugadores('yellow').fichas.arr[3].posruta)
        config.add_section("blue")
        config.set("blue",  'ia', int(self.jugadores('blue').ia))
        config.set("blue",  'name', self.jugadores('blue').name)
        config.set("blue",  'plays', int(self.jugadores('blue').plays))
        if self.jugadores('blue').plays==True:        
            config.set("blue",  'rutaficha1', self.jugadores('blue').fichas.arr[0].posruta)
            config.set("blue",  'rutaficha2',  self.jugadores('blue').fichas.arr[1].posruta)
            config.set("blue",  'rutaficha3',  self.jugadores('blue').fichas.arr[2].posruta)
            config.set("blue",  'rutaficha4',  self.jugadores('blue').fichas.arr[3].posruta) 
        config.add_section("red")
        config.set("red",  'ia', int(self.jugadores('red').ia))
        config.set("red",  'name', self.jugadores('red').name)
        config.set("red",  'plays', int(self.jugadores('red').plays))
        if self.jugadores('red').plays==True:        
            config.set("red",  'rutaficha1', self.jugadores('red').fichas.arr[0].posruta)
            config.set("red",  'rutaficha2',  self.jugadores('red').fichas.arr[1].posruta)
            config.set("red",  'rutaficha3',  self.jugadores('red').fichas.arr[2].posruta)
            config.set("red",  'rutaficha4',  self.jugadores('red').fichas.arr[3].posruta)    
        config.add_section("green")
        config.set("green",  'ia', int(self.jugadores('green').ia))
        config.set("green",  'name', self.jugadores('green').name)
        config.set("green",  'plays', int(self.jugadores('green').plays))        
        if self.jugadores('green').plays==True:
            config.set("green",  'rutaficha1', self.jugadores('green').fichas.arr[0].posruta)
            config.set("green",  'rutaficha2',  self.jugadores('green').fichas.arr[1].posruta)
            config.set("green",  'rutaficha3',  self.jugadores('green').fichas.arr[2].posruta)
            config.set("green",  'rutaficha4',  self.jugadores('green').fichas.arr[3].posruta)    
        config.add_section("game")
        config.set("game", 'playerstarts',self.jugadoractual.color.name)
        config.set("game", 'fakedice','')
        with open(filename, 'w') as configfile:
            config.write(configfile)            

                    
    def generar_casillas(self):
        def defineSeguro( id):
            if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
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
               return Color(255, 255, 30)       #amarillo 
            elif id==39 or (id>=85 and id<=92) or id==103:
               return Color(255, 30, 30)#rojo
            elif id==22 or (id>=77 and id<=84) or id==102:
               return Color(30, 30, 255)#azul
            elif id==56 or (id>=93 and id<=100) or id==104:
               return Color(30, 255, 30) #verde
            elif id==68 or  id==63 or  id==51 or id==46 or id==34 or  id==29 or  id==17 or   id==12:  
               return Color(128, 128, 128)
            else:
                return Color(255, 255, 255)            
                
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
        posFichas=[None]*105
        posFichas[0]=((0, 0, 0), (0, 0, 0))
        posFichas[1]=((22.7, 61.5, 0.9), (26.3, 61.5, 0.9))
        posFichas[2]=((22.7, 58.5, 0.9), (26.3, 58.5, 0.9))
        posFichas[3]=((22.7, 55.5, 0.9), (26.3, 55.5, 0.9))
        posFichas[4]=((22.7, 52.5, 0.9), (26.3, 52.5, 0.9))
        posFichas[5]=((22.7, 49.5, 0.9), (26.3, 49.5, 0.9))
        posFichas[6]=((22.7, 46.5, 0.9), (26.3, 46.5, 0.9))
        posFichas[7]=((22.7, 43.5, 0.9), (26.3, 43.5, 0.9))
        posFichas[8]=((24.5, 40.5, 0.9), (26.5, 40.5, 0.9))
        posFichas[9]=((22.5, 38.5, 0.9), (22.5, 36.5, 0.9))
        posFichas[10]=((19.5, 40.3, 0.9), (19.5, 36.7, 0.9))
        posFichas[11]=((16.5, 40.3, 0.9), (16.5, 36.7, 0.9))
        posFichas[12]=((13.5, 40.3, 0.9), (13.5, 36.7, 0.9))
        posFichas[13]=((10.5, 40.3, 0.9), (10.5, 36.7, 0.9))
        posFichas[14]=((7.5, 40.3, 0.9), (7.5, 36.7, 0.9))
        posFichas[15]=((4.5, 40.3, 0.9), (4.5, 36.7, 0.9))
        posFichas[16]=((1.5, 40.3, 0.9), (1.5, 36.7, 0.9))
        posFichas[17]=((1.5, 33.3, 0.9), (1.5, 29.7, 0.9))
        posFichas[18]=((1.5, 26.3, 0.9), (1.5, 22.7, 0.9))
        posFichas[19]=((4.5, 26.3, 0.9), (4.5, 22.7, 0.9))
        posFichas[20]=((7.5, 26.3, 0.9), (7.5, 22.7, 0.9))
        posFichas[21]=((10.5, 26.3, 0.9), (10.5, 22.7, 0.9))
        posFichas[22]=((13.5, 26.3, 0.9), (13.5, 22.7, 0.9))
        posFichas[23]=((16.5, 26.3, 0.9), (16.5, 22.7, 0.9))
        posFichas[24]=((19.5, 26.3, 0.9), (19.5, 22.7, 0.9))
        posFichas[25]=((22.5, 26.5, 0.9), (22.5, 24.5, 0.9))
        posFichas[26]=((24.5, 22.5, 0.9), (26.5, 22.5, 0.9))
        posFichas[27]=((22.7, 19.5, 0.9), (26.3, 19.5, 0.9))
        posFichas[28]=((22.7, 16.5, 0.9), (26.3, 16.5, 0.9))
        posFichas[29]=((22.7, 13.5, 0.9), (26.3, 13.5, 0.9))
        posFichas[30]=((22.7, 10.5, 0.9), (26.3, 10.5, 0.9))
        posFichas[31]=((22.7, 7.5, 0.9), (26.3, 7.5, 0.9))
        posFichas[32]=((22.7, 4.5, 0.9), (26.3, 4.5, 0.9))
        posFichas[33]=((22.7, 1.5, 0.9), (26.3, 1.5, 0.9))
        posFichas[34]=((29.7, 1.5, 0.9), (33.3, 1.5, 0.9))
        posFichas[35]=((36.7, 1.5, 0.9), (40.3, 1.5, 0.9))
        posFichas[36]=((36.7, 4.5, 0.9), (40.3, 4.5, 0.9))
        posFichas[37]=((36.7, 7.5, 0.9), (40.3, 7.5, 0.9))
        posFichas[38]=((36.7, 10.5, 0.9), (40.3, 10.5, 0.9))
        posFichas[39]=((36.7, 13.5, 0.9), (40.3, 13.5, 0.9))
        posFichas[40]=((36.7, 16.5, 0.9), (40.3, 16.5, 0.9))
        posFichas[41]=((36.7, 19.5, 0.9), (40.3, 19.5, 0.9))
        posFichas[42]=((36.5, 22.5, 0.9), (38.5, 22.5, 0.9))
        posFichas[43]=((40.5, 26.5, 0.9), (40.5, 24.5, 0.9))
        posFichas[44]=((43.5, 26.3, 0.9), (43.5, 22.7, 0.9))
        posFichas[45]=((46.5, 26.3, 0.9), (46.5, 22.7, 0.9))
        posFichas[46]=((49.5, 26.3, 0.9), (49.5, 22.7, 0.9))
        posFichas[47]=((52.5, 26.3, 0.9), (52.5, 22.7, 0.9))
        posFichas[48]=((55.5, 26.3, 0.9), (55.5, 22.7, 0.9))
        posFichas[49]=((58.5, 26.3, 0.9), (58.5, 22.7, 0.9))
        posFichas[50]=((61.5, 26.3, 0.9), (61.5, 22.7, 0.9))
        posFichas[51]=((61.5, 33.3, 0.9), (61.5, 29.7, 0.9))
        posFichas[52]=((61.5, 40.3, 0.9), (61.5, 36.7, 0.9))
        posFichas[53]=((58.5, 40.3, 0.9), (58.5, 36.7, 0.9))
        posFichas[54]=((55.5, 40.3, 0.9), (55.5, 36.7, 0.9))
        posFichas[55]=((52.5, 40.3, 0.9), (52.5, 36.7, 0.9))
        posFichas[56]=((49.5, 40.3, 0.9), (49.5, 36.7, 0.9))
        posFichas[57]=((46.5, 40.3, 0.9), (46.5, 36.7, 0.9))
        posFichas[58]=((43.5, 40.3, 0.9), (43.5, 36.7, 0.9))
        posFichas[59]=((40.5, 38.5, 0.9), (40.5, 36.5, 0.9))
        posFichas[60]=((36.5, 40.5, 0.9), (38.5, 40.5, 0.9))
        posFichas[61]=((36.7, 43.5, 0.9), (40.3, 43.5, 0.9))
        posFichas[62]=((36.7, 46.5, 0.9), (40.3, 46.5, 0.9))
        posFichas[63]=((36.7, 49.5, 0.9), (40.3, 49.5, 0.9))
        posFichas[64]=((36.7, 52.5, 0.9), (40.3, 52.5, 0.9))
        posFichas[65]=((36.7, 55.5, 0.9), (40.3, 55.5, 0.9))
        posFichas[66]=((36.7, 58.5, 0.9), (40.3, 58.5, 0.9))
        posFichas[67]=((36.7, 61.5, 0.9), (40.3, 61.5, 0.9))
        posFichas[68]=((29.7, 61.5, 0.9), (33.3, 61.5, 0.9))
        posFichas[69]=((29.7, 58.5, 0.9), (33.3, 58.5, 0.9))
        posFichas[70]=((29.7, 55.5, 0.9), (33.3, 55.5, 0.9))
        posFichas[71]=((29.7, 52.5, 0.9), (33.3, 52.5, 0.9))
        posFichas[72]=((29.7, 49.5, 0.9), (33.3, 49.5, 0.9))
        posFichas[73]=((29.7, 46.5, 0.9), (33.3, 46.5, 0.9))
        posFichas[74]=((29.7, 43.5, 0.9), (33.3, 43.5, 0.9))
        posFichas[75]=((29.7, 40.5, 0.9), (33.3, 40.5, 0.9))
        posFichas[76]=((29.7, 37.5, 0.9), (33.3, 37.5, 0.9))
        posFichas[77]=((4.5, 33.3, 0.9), (4.5, 29.7, 0.9))
        posFichas[78]=((7.5, 33.3, 0.9), (7.5, 29.7, 0.9))
        posFichas[79]=((10.5, 33.3, 0.9), (10.5, 29.7, 0.9))
        posFichas[80]=((13.5, 33.3, 0.9), (13.5, 29.7, 0.9))
        posFichas[81]=((16.5, 33.3, 0.9), (16.5, 29.7, 0.9))
        posFichas[82]=((19.5, 33.3, 0.9), (19.5, 29.7, 0.9))
        posFichas[83]=((22.5, 33.3, 0.9), (22.5, 29.7, 0.9))
        posFichas[84]=((25.5, 33.3, 0.9), (25.5, 29.7, 0.9))
        posFichas[85]=((29.7, 4.5, 0.9), (33.3, 4.5, 0.9))
        posFichas[86]=((29.7, 7.5, 0.9), (33.3, 7.5, 0.9))
        posFichas[87]=((29.7, 10.5, 0.9), (33.3, 10.5, 0.9))
        posFichas[88]=((29.7, 13.5, 0.9), (33.3, 13.5, 0.9))
        posFichas[89]=((29.7, 16.5, 0.9), (33.3, 16.5, 0.9))
        posFichas[90]=((29.7, 19.5, 0.9), (33.3, 19.5, 0.9))
        posFichas[91]=((29.7, 22.5, 0.9), (33.3, 22.5, 0.9))
        posFichas[92]=((29.7, 25.5, 0.9), (33.3, 25.5, 0.9))
        posFichas[93]=((58.5, 33.3, 0.9), (58.5, 29.7, 0.9))
        posFichas[94]=((55.5, 33.3, 0.9), (55.5, 29.7, 0.9))
        posFichas[95]=((52.5, 33.3, 0.9), (52.5, 29.7, 0.9))
        posFichas[96]=((49.5, 33.3, 0.9), (49.5, 29.7, 0.9))
        posFichas[97]=((46.5, 33.3, 0.9), (46.5, 29.7, 0.9))
        posFichas[98]=((43.5, 33.3, 0.9), (43.5, 29.7, 0.9))
        posFichas[99]=((40.5, 33.3, 0.9), (40.5, 29.7, 0.9))
        posFichas[100]=((37.5, 33.3, 0.9), (37.5, 29.7, 0.9))
        posFichas[101]=((7, 49, 0.9), (14, 49, 0.9), (14, 56, 0.9), (7, 56, 0.9))
        posFichas[102]=((7, 7, 0.9), (14, 7, 0.9), (14, 14, 0.9), (7, 14, 0.9))
        posFichas[103]=((49, 7, 0.9), (56, 7, 0.9), (49, 14, 0.9), (56, 14, 0.9))
        posFichas[104]=((49, 49, 0.9), (56, 49, 0.9), (49, 56, 0.9), (56, 56, 0.9))        
        
        
        posCasillas=[None]*105
        posCasillas[0]=(0, 0, 0)
        posCasillas[1]=(21, 60, 0.7)
        posCasillas[2]=(21, 57, 0.7)
        posCasillas[3]=(21, 54, 0.7)
        posCasillas[4]=(21, 51, 0.7)
        posCasillas[5]=(21, 48, 0.7)
        posCasillas[6]=(21, 45, 0.7)
        posCasillas[7]=(21, 42, 0.7)
        posCasillas[8]=(28,  42, 0.7)
        posCasillas[9]=(21, 42, 0.7)
        posCasillas[10]=(21, 35, 0.7)
        posCasillas[11]=(18, 35, 0.7)
        posCasillas[12]=(15, 35, 0.7)
        posCasillas[13]=(12, 35, 0.7)
        posCasillas[14]=(9, 35, 0.7)
        posCasillas[15]=(6, 35, 0.7)
        posCasillas[16]=(3, 35, 0.7)
        posCasillas[17]=(3, 28, 0.7)
        posCasillas[18]=(3, 21, 0.7)
        posCasillas[19]=(6, 21, 0.7)
        posCasillas[20]=(9, 21, 0.7)
        posCasillas[21]=(12, 21, 0.7)
        posCasillas[22]=(15, 21, 0.7)
        posCasillas[23]=(18, 21, 0.7)
        posCasillas[24]=(21, 21, 0.7)
        posCasillas[25]=(21, 28, 0.7)
        posCasillas[26]=(21, 21, 0.7)
        posCasillas[27]=(21, 18, 0.7)
        posCasillas[28]=(21, 15, 0.7)
        posCasillas[29]=(21, 12, 0.7)
        posCasillas[30]=(21, 9, 0.7)
        posCasillas[31]=(21, 6, 0.7)
        posCasillas[32]=(21, 3, 0.7)
        posCasillas[33]=(21, 0, 0.7)
        posCasillas[34]=(28, 0, 0.7)
        posCasillas[35]=(35, 0, 0.7)
        posCasillas[36]=(35, 3, 0.7)
        posCasillas[37]=(35, 6, 0.7)
        posCasillas[38]=(35, 9, 0.7)
        posCasillas[39]=(35, 12, 0.7)
        posCasillas[40]=(35, 15, 0.7)
        posCasillas[41]=(35, 18, 0.7)
        posCasillas[42]=(35, 21, 0.7)
        posCasillas[43]=(42, 21, 0.7)
        posCasillas[44]=(45, 21, 0.7)
        posCasillas[45]=(48, 21, 0.7)
        posCasillas[46]=(51, 21, 0.7)
        posCasillas[47]=(54, 21, 0.7)
        posCasillas[48]=(57, 21, 0.7)
        posCasillas[49]=(60, 21, 0.7)
        posCasillas[50]=(63, 21, 0.7)
        posCasillas[51]=(63, 28, 0.7)
        posCasillas[52]=(63, 35, 0.7)
        posCasillas[53]=(60, 35, 0.7)
        posCasillas[54]=(57, 35, 0.7)
        posCasillas[55]=(54, 35, 0.7)
        posCasillas[56]=(51, 35, 0.7)
        posCasillas[57]=(48, 35, 0.7)
        posCasillas[58]=(45, 35, 0.7)
        posCasillas[59]=(42, 35, 0.7)
        posCasillas[60]=(42 ,42, 0.7)
        posCasillas[61]=(35, 42, 0.7)
        posCasillas[62]=(35, 45, 0.7)
        posCasillas[63]=(35, 48, 0.7)
        posCasillas[64]=(35, 51, 0.7)
        posCasillas[65]=(35, 54, 0.7)
        posCasillas[66]=(35, 57, 0.7)
        posCasillas[67]=(35, 60, 0.7)
        posCasillas[68]=(28, 60, 0.7)
        posCasillas[69]=(28, 57, 0.7)
        posCasillas[70]=(28, 54, 0.7)
        posCasillas[71]=(28, 51, 0.7)
        posCasillas[72]=(28, 48, 0.7)
        posCasillas[73]=(28, 45, 0.7)
        posCasillas[74]=(28, 42, 0.7)
        posCasillas[75]=(28, 39, 0.7)
        posCasillas[76]=(39, 39, 0.7)
        posCasillas[77]=(6, 28, 0.7)
        posCasillas[78]=(9, 28, 0.7)
        posCasillas[79]=(12, 28, 0.7)
        posCasillas[80]=(15, 28, 0.7)
        posCasillas[81]=(18, 28, 0.7)
        posCasillas[82]=(21, 28, 0.7)
        posCasillas[83]=(24, 28, 0.7)
        posCasillas[84]=(24, 39, 0.7)
        posCasillas[85]=(28, 3, 0.7)
        posCasillas[86]=(28, 6, 0.7)
        posCasillas[87]=(28, 9, 0.7)
        posCasillas[88]=(28, 12, 0.7)
        posCasillas[89]=(28, 15, 0.7)
        posCasillas[90]=(28, 18, 0.7)
        posCasillas[91]=(28, 21, 0.7)
        posCasillas[92]=(24, 24, 0.7)
        posCasillas[93]=(60, 28, 0.7)
        posCasillas[94]=(57, 28, 0.7)
        posCasillas[95]=(54, 28, 0.7)
        posCasillas[96]=(51, 28, 0.7)
        posCasillas[97]=(48, 28, 0.7)
        posCasillas[98]=(45, 28, 0.7)
        posCasillas[99]=(42, 28, 0.7)
        posCasillas[100]=(39, 24, 0.7)
        posCasillas[101]=(0, 42, 0.7)
        posCasillas[102]=(0, 0, 0.7)
        posCasillas[103]=(42, 0, 0.7)
        posCasillas[104]=(42,  42, 0.7)
        for i in range(0, 105):#Se debe inializar Antes que las fichas
            self.dic_casillas[str(i)]=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), posFichas[i])
            
            
    def casillas(self, name=None):
        if name==None:
            return dic2list(self.dic_casillas)
        else:
            return self.dic_casillas[str(name)]
            
    def load(self, filename):       
        config = ConfigParser.ConfigParser()
        config.read(filename)

        yellow=self.jugadores('yellow')
        yellow.name=config.get('yellow', 'name')
        yellow.ia=i2b(config.getint("yellow", "ia"))
        yellow.plays=(i2b(config.getint("yellow", "plays")))
        
        blue=self.jugadores('blue')
        blue.name=config.get("blue", "name")
        blue.ia=i2b(config.getint("blue", "ia"))
        blue.plays=(i2b(config.getint("blue", "plays")))
        
        red=self.jugadores('red')
        red.name=config.get("red", "name")
        red.ia=i2b(config.getint("red", "ia"))
        red.plays=(i2b(config.getint("red", "plays")))
        
        green=self.jugadores('green')
        green.name=config.get("green", "name")
        green.ia=i2b(config.getint("green", "ia"))
        green.plays=(i2b(config.getint("green", "plays")))  

        for j in self.jugadores():
            if j.plays==True:
                j.fichas.arr[0].mover(config.getint(j.color.name, "rutaficha1"), False,  True)
                j.fichas.arr[1].mover(config.getint(j.color.name, "rutaficha2"), False,  True)
                j.fichas.arr[2].mover(config.getint(j.color.name, "rutaficha3"), False,  True)
                j.fichas.arr[3].mover(config.getint(j.color.name, "rutaficha4"), False,  True)

        fake=config.get("game", 'fakedice')
        if fake!="":
            for i in  fake.split(";")  :
                self.dado.fake.append(int(i))
        self.jugadoractual=self.jugadores(config.get("game", 'playerstarts'))    
#        self.jugadoractual.historicodado=[]
        self.jugadoractual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadoractual.LastFichaMovida=None #Se utiliza cuando se va a casa

            
def dic2list(dic):
    """Función que convierte un diccionario pasado como parametro a una lista de objetos"""
    resultado=[]
    for k,  v in dic.items():
        resultado.append(v)
    return resultado

        

class Name:
    """Enumeración usada para los names de opengl"""
    ficha=[0]*16
    for i in range(0, 16):
        ficha[i]=i
    tablero=16
    casilla=[0]*105
    for i in range(17, 122):
        casilla[i-17]=i
#    print ficha,  tablero, casilla
    
    @staticmethod
    def object(mem, id_name):
        """Devuelve un objeto dependiendo del nombre.None si no corresponde"""
        if id_name>=0 and id_name<=15:
            return mem.fichas(id_name)
        elif id_name==16:
            return mem.tablero
        elif id_name>=17 and id_name<=121:
            return mem.casillas(id_name-17)
        else:
            return None
