## -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
import ConfigParser,  random
from OpenGL import GL,  GLU
import libglparchis

class Dado():    
    def __init__(self):
        self.lastthrow=None
        self.fake=[]
    def tirar(self):
        if len(self.fake)>0:
            self.lastthrow=self.fake[0]
            self.fake.remove(self.fake[0])
        else:
#        numero= int(random.random()*6)+1
            self.lastthrow= int(random.random()*2)+5
        return self.lastthrow
    

class Jugador():
    def __init__(self, color):
        self.name=None
        self.color=color
        self.ia=False
        self.plays=None
        self.fichas={}        
        self.historicodado=[]
        self.lastFichaMovida=None #Se utiliza cuando se va a casa NOne si ninguna
#        self.hamovidoficha=False #Util para ver si se va acasa tras 6 seises
        self.movimientos_acumulados=None#Comidas ymetidas, puede ser 10, 20 o None Cuando se cuenta se borra a None

        self.id=libglparchis.colorid(color)

    def CreaFichas(self, plays):
        self.plays=plays        
        if self.plays==True:
            for i in range(1, 5):
                self.fichas[self.color+str(i)]=Ficha(self.color+str(i))
        
    def TodasFichasEnCasa(self):
        for f in self.fichas:
            if self.fichas[f].ruta!=0:
                return False
        return True        
        
    def TodasFichasFueraDeCasa(self):
        for f in self.fichas:
            if self.fichas[f].ruta==0:
                return False
        return True
                
           
            
    def HaGanado(self):
        for f in self.fichas:
            if self.fichas[f].ruta!=72:
                return False
        return True
        
class Casilla(QGLWidget):
    def __init__(self, id, parent=None):
        QGLWidget.__init__(self, parent)
        self.id=id
        self.max_fichas=self.defineMaxFichas(id)
        self.color=self.defineColor(id)
        self.position=libglparchis.posCasillas[id]
        self.rotate=self.defineRotate(id)
        self.rampallegada=self.defineRampaLlegada(id)
        self.tipo=self.defineTipo(id)
#        self.busy=[False]*self.max_fichas
        self.seguro=self.defineSeguro(id)
        self.buzon=[]


    def defineSeguro(self,  id):
        if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
            return True
        else:
            return False

    def defineMaxFichas(self,  id):
        if id==101 or id==102 or id==103 or id==104 or id==76 or id==84 or id==92 or id==100:
            return 4
        else:
            return 2

    def defineRampaLlegada(self, id):
        if id>=69 and id<= 100:
           return True
        return False

    def defineTipo(self,  id):
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

    def defineColor(self,  id):
        if id==5 or (id>=69 and id<=76) or id==101:
           return QColor(255, 255, 30)       #amarillo 
        elif id==39 or (id>=85 and id<=92) or id==103:
           return QColor(255, 30, 30)#rojo
        elif id==22 or (id>=77 and id<=84) or id==102:
           return QColor(30, 30, 255)#azul
        elif id==56 or (id>=93 and id<=100) or id==104:
           return QColor(30, 255, 30) #verde
        elif id==68 or  id==63 or  id==51 or id==46 or id==34 or  id==29 or  id==17 or   id==12:  
           return QColor(128, 128, 128)
        else:
            return QColor(255, 255, 255)            
            
    def defineRotate(self,  id):
        if (id>=10 and id<=24) or (id>=77 and id<=83) or(id>=43 and id <=59) or (id>=93 and id<=100):
           return 90
        if id==60 or id==8 or id==76:
            return 180
        if id==9 or id==25 or id==84:
            return 270
        else:
            return 0
        
    def dibujar(self):
#        print("dibuajando casillaa")
        if self.tipo==0:
            self.tipo_inicio()
        elif self.tipo==1:
            self.tipo_final()
        elif self.tipo==2:
            self.tipo_oblicuoi()
        elif self.tipo==4:
            self.tipo_oblicuod()
        else:
            self.tipo_normal()
            
    def dibujar_fichas(self):
        posicionBuzon=0

        for f in self.buzon:
            if posicionBuzon+1>self.max_fichas:
                print "Hay m´as fichas en el buz´on que posiciones en casilla"
                return            
            f.dibujar(posicionBuzon)
            posicionBuzon=posicionBuzon+1
        
    def tipo_inicio(self):        
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.casilla[self.id]);
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

        self.quad(v1, v2, v3, v4,self.color)      
        self.quad(v8, v7, v6, v5,  QColor(70, 70, 70))      
        self.quad(v1, v4, v8, v5, QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170))      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))

        GL.glPopName();
        GL.glPopMatrix()

    def tipo_normal(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.casilla[self.id]);
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

        self.quad(v1, v2, v3, v4, self.color)      
        self.quad(v8, v7, v6, v5,QColor(70, 70, 70) )      
        self.quad(v1, v4, v8, v5,QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170) )      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))
        GL.glPopName();
        GL.glPopMatrix()

    def tipo_oblicuoi(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.casilla[self.id]);
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

        self.quad(v1, v2, v3, v4, self.color)      
        self.quad(v8, v7, v6, v5, QColor(70, 70, 70))      
        self.quad(v1, v4, v8, v5,QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170) )      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))

        GL.glPopName();
        GL.glPopMatrix()

    def tipo_oblicuod(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.casilla[self.id]);
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

        self.quad(v1, v2, v3, v4,self.color )      
        self.quad(v8, v7, v6, v5, QColor(70, 70, 70))      
        self.quad(v1, v4, v8, v5,QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170) )      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))

        GL.glPopName();
        GL.glPopMatrix()
        
    def tipo_final(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.casilla[self.id]);
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

        self.quad(v1, v2, v3, v4, self.color)      
        self.quad(v8, v7, v6, v5, QColor(70, 70, 70))      
        self.quad(v1, v4, v8, v5,QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170) )      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))

        GL.glPopName();
        GL.glPopMatrix()

    def TieneBarrera(self):
        if self.tipo not in (0, 1):#Casilla inicio y final
            if self.max_fichas==2:
                if len(self.buzon)==2:
                    if self.buzon[0].jugador==self.buzon[1].jugador:
                        return True
        return False

    def haySitioEnBuzon(self):
        if len(self.buzon)<self.max_fichas:
            return True
        return False

        
    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])
        
    def border(self, a, b, c, d, color):        
        GL.glBegin(GL.GL_LINE_LOOP)
        self.qglColor(color)
        GL.glVertex3d(a[0], a[1], a[2]+0.0001)
        GL.glVertex3d(b[0], b[1], b[2]+0.0001)
        GL.glVertex3d(c[0], c[1], c[2]+0.0001)
        GL.glVertex3d(d[0], d[1], d[2]+0.0001)
        GL.glEnd()


class wdgGame(QGLWidget):
    """Clase principal del Juego, aqu´i est´a toda la ciencia, cuando se deba pasar al UI se crear´an emits que captura qT para el UI"""
    def __init__(self, parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0
        self.lastPos = QPoint()
        self.jugadores={}
        self.casillas=[]
#        self.fichas=[]
        self.selFicha=None
        self.selCasilla=None
        self.jugadoractual=None
        self.dado=None
        for i in range(0, 105):#Se debe inializar Antes que las fichas
            self.casillas.append(Casilla(i)) #La casilla 0 no se usa pero se crea para que todo sea más intuitivo.

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def load_file(self, filename):
        self.rotX=0
        self.lastPos = QPoint()
        self.jugadores={}
#        self.fichas=[]
        self.selFicha=None
        self.selCasilla=None
        self.dado=Dado()
        
        
        config = ConfigParser.ConfigParser()
        config.read(filename)#ÐEBE SERLOCAL

        yellow=Jugador('yellow')
        yellow.name=config.get('yellow', 'name')
        yellow.ia=libglparchis.i2b(config.getint("yellow", "ia"))
        yellow.CreaFichas(libglparchis.i2b(config.getint("yellow", "plays")))
        
        blue=Jugador('blue')
        blue.name=config.get("blue", "name")
        blue.ia=libglparchis.i2b(config.getint("blue", "ia"))
        blue.CreaFichas(libglparchis.i2b(config.getint("blue", "plays")))
        
        red=Jugador('red')
        red.name=config.get("red", "name")
        red.ia=libglparchis.i2b(config.getint("red", "ia"))
        red.CreaFichas(libglparchis.i2b(config.getint("red", "plays")))
        
        green=Jugador('green')
        green.name=config.get("green", "name")
        green.ia=libglparchis.i2b(config.getint("green", "ia"))
        green.CreaFichas(libglparchis.i2b(config.getint("green", "plays")))
        
        self.jugadores['blue']=blue
        self.jugadores['yellow']=yellow
        self.jugadores['red']=red
        self.jugadores['green']=green        
        
#        #Crea la lista de fichas
#        for c in libglparchis.colores:
#            for f in self.jugadores[c].fichas:
#                self.fichas.append(self.jugadores[c].fichas[f])
      
        if yellow.plays==True:
            self.mover(yellow.fichas["yellow1"], config.getint("yellow", "rutaficha1"))
            self.mover(yellow.fichas["yellow2"], config.getint("yellow", "rutaficha2"))
            self.mover(yellow.fichas["yellow3"], config.getint("yellow", "rutaficha3"))
            self.mover(yellow.fichas["yellow4"], config.getint("yellow", "rutaficha4"))
        if blue.plays==True:
            self.mover(blue.fichas["blue1"], config.getint("blue", "rutaficha1"))
            self.mover(blue.fichas["blue2"], config.getint("blue", "rutaficha2"))
            self.mover(blue.fichas["blue3"], config.getint("blue", "rutaficha3"))
            self.mover(blue.fichas["blue4"], config.getint("blue", "rutaficha4"))
        if red.plays==True:
            self.mover(red.fichas["red1"], config.getint("red", "rutaficha1"))
            self.mover(red.fichas["red2"], config.getint("red", "rutaficha2"))
            self.mover(red.fichas["red3"], config.getint("red", "rutaficha3"))
            self.mover(red.fichas["red4"], config.getint("red", "rutaficha4"))
        if green.plays==True:
            self.mover(green.fichas["green1"], config.getint("green", "rutaficha1"))
            self.mover(green.fichas["green2"], config.getint("green", "rutaficha2"))
            self.mover(green.fichas["green3"], config.getint("green", "rutaficha3"))
            self.mover(green.fichas["green4"], config.getint("green", "rutaficha4"))
        
        self.jugadoractual=self.jugadores[config.get("game", 'playerstarts')]        
        self.jugadoractual.historicodado=[]
        self.jugadoractual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadoractual.lastFichaMovida=None #Se utiliza cuando se va a casa
        
    def initializeGL(self):
        print ("initializeGL")
        self.qglClearColor(self.trolltechPurple.dark())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        
        GL.glFrontFace(GL.GL_CCW);

        light_ambient =  (0.3, 0.3, 0.3, 0.1);
#        light_diffuse =  (0, 0, 1, 0);
#        light_specular =  (0, 0, 0, 0);
#        light_position =  (5.0, 5.0, 5.0, 0.0);


        GL.glEnable(GL.GL_LIGHTING)
        lightpos=(0, 0, 50)
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, light_ambient)  
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, lightpos)  
        GL.glEnable(GL.GL_LIGHT0);
        GL.glEnable(GL.GL_COLOR_MATERIAL);
        GL.glColorMaterial(GL.GL_FRONT,GL.GL_AMBIENT_AND_DIFFUSE);
        GL.glShadeModel (GL.GL_SMOOTH);

    def log(self, cadena):
            self.emit(SIGNAL("newLog(QString)"),str(cadena))

    def paintGL(self):   
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(-31.5, -31.5,  -60)
        GL.glRotated(self.rotX, 1,0 , 0)
        self.tablero.dibujar()
        for c in self.casillas:
            c.dibujar()
            c.dibujar_fichas()
#        for f in self.fichas:
##            print(f.name)
#            f.dibujar()

    def resizeGL(self, width, height):
        GL.glViewport(0, 0, width, height)
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        aspect=width/height
        GLU.gluPerspective(60.0, aspect, 1, 400)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Escape) or (event.key() == Qt.Key_Q):
            self.close()

        if event.key() == Qt.Key_Q: # toggle mode
            self.updateGL()
                
    def mousePressEvent(self, event):        
        def pickup(event):
            viewport=GL.glGetIntegerv(GL.GL_VIEWPORT);
            GL.glMatrixMode(GL.GL_PROJECTION);
            GL.glPushMatrix();
            GL.glSelectBuffer(512);
            GL.glRenderMode(GL.GL_SELECT);
            GL.glLoadIdentity();
            GLU.gluPickMatrix(event.x(),viewport[3] -event.y(),1,1, viewport)
            aspect=viewport[2]/viewport[3]
            GLU.gluPerspective(60,aspect,1.0,400)
            GL.glMatrixMode(GL.GL_MODELVIEW)
            self.paintGL()
            GL.glMatrixMode(GL.GL_PROJECTION);
            process(GL.glRenderMode(GL.GL_RENDER))
            GL.glPopMatrix();
            GL.glMatrixMode(GL.GL_MODELVIEW);           
        def pickupright(event):
            viewport=GL.glGetIntegerv(GL.GL_VIEWPORT);
            GL.glMatrixMode(GL.GL_PROJECTION);
            GL.glPushMatrix();
            GL.glSelectBuffer(512);
            GL.glRenderMode(GL.GL_SELECT);
            GL.glLoadIdentity();
            GLU.gluPickMatrix(event.x(),viewport[3] -event.y(),1,1, viewport)
            aspect=viewport[2]/viewport[3]
            GLU.gluPerspective(60,aspect,1.0,400)
            GL.glMatrixMode(GL.GL_MODELVIEW)
            self.paintGL()
            GL.glMatrixMode(GL.GL_PROJECTION);
            processright(GL.glRenderMode(GL.GL_RENDER))
            GL.glPopMatrix();
            GL.glMatrixMode(GL.GL_MODELVIEW);           
        def object(id_name):
            if id_name>=0 and id_name<=15:
                return id_name
            elif id_name==16:
                return self.tablero
            elif id_name>=17 and id_name<=121:
                return id_name-17
                
        def process(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
#                print minDepth,  maxDepth,  names
                if len(names)==1:
                   objetos.append(names[0])
            
            if len(objetos)==1:
                self.selCasilla=object(objetos[0])
#                self.emit(SIGNAL("newLog(QString)"),"selCasilla:" + str(self.selCasilla )+ ". Busy:" +  str(self.casillas[self.selCasilla].busy))
                self.selFicha=None
            elif len(objetos)==2:
#                self.selLastFicha=self.selFicha
                self.selCasilla=self.casillas[object(objetos[0])]
                self.selFicha=self.busca_ficha(object(objetos[1]))
                self.log("Clickeada " + self.selFicha.name)
                
        def processright(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
#                print minDepth,  maxDepth,  names
                if len(names)==1:
                   objetos.append(names[0])
#            print len(objetos)
            if len(objetos)==1:
                selCasilla=object(objetos[0])
                self.emit(SIGNAL("showCasillaFicha(int,int)"), selCasilla, -99)
            elif len(objetos)==2:
                selCasilla=object(objetos[0])
                selFicha=object(objetos[1])
                self.emit(SIGNAL("showCasillaFicha(int,int)"),selCasilla, selFicha)
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event)            
            if self.selFicha>=0:
                self.after_ficha_click()
        elif event.buttons() & Qt.RightButton:
            pickupright(event)                    
        self.updateGL()
                        
                
    def AlgunaPuedeMover(self):
        for f in self.jugadoractual.fichas:
            if self.PuedeMover(self.jugadoractual.fichas[f], self.dado.lastthrow)[0]==True:
                return True
        return False

    def Barreras(self, jugador):
        """Devuelve [] si no y [id_casillas,] si si"""
        resultado =[]
        for f in jugador.fichas:
            casilla=self.casillas[jugador.fichas[f].id_casilla()]
            if casilla.TieneBarrera()==True:
                resultado.append(casilla.id)
        return resultado
        
    def PuedeMover(self, ficha,  valordado):
        #Calcula el movimiento
        if self.jugadoractual.movimientos_acumulados!=None:
            movimiento=self.jugadoractual.movimientos_acumulados
        else:
            movimiento=valordado
            if ficha.EstaEnCasa() and valordado==5:
                movimiento=1
            if self.jugadoractual.TodasFichasFueraDeCasa()==True and valordado==6:
                movimiento=7

        #Es ficha del jugador actual
        if  ficha.jugador!=self.jugadoractual.id:             
            self.log("No es del jugador actual")
            return (False, 0)

        #Comprueba que no tenga obligaci´on de abrir barrera
        if valordado==6:
            barreras=self.Barreras(self.jugadoractual)
            if len(barreras)!=0 :
                if ficha.id_casilla() not in barreras:
                    self.log("No se puede mover, debes abrir barrera")
                    return (False, 0)
            
            

        #Esta en casa y puede mover
        if ficha.EstaEnCasa()==True:
            if valordado!=5: #Saco un 5
                self.log("Necesita sacar un 5 para mover esta ficha")
                return (False, 0)
                        
        #se ha pasado la meta
        if ficha.ruta+movimiento>72:
            self.log("Se ha pasado la meta")
            return (False, 0)
                
                
        #Rastrea todas las casillas de paso en busca de barrera.
        for i in range(0, movimiento): 
            id_casilla=libglparchis.ruta[ficha.ruta+i+1][ficha.jugador]
            if self.casillas[id_casilla].TieneBarrera()==True:
                self.log("Hay una barrera")
                return (False, 0)

           
        #Comprueba si hay sitio libre
        id_casilladestino=libglparchis.ruta[ficha.ruta+movimiento][ficha.jugador]
        if self.casillas[id_casilladestino].haySitioEnBuzon()==False:
            self.log("No hay espacio en la casilla")
            return (False, 0)
            
        self.log("Puede mover "+str(movimiento))
        return (True, movimiento)
            
    def habiaSalidoSeis(self):
        """Se usa despu´es de movimientos acumulados"""
        if self.dado.lastthrow==6:
            return True
        return False
            
    def come(self, ficha,  ruta):
        """ruta, es la posici´on de ruta de ficha en la que come. Como ya se ha movido, come si puede y devuelve True, en caso contrario False"""
#        def hay_ficha_otro_jugador(id_casilla):
#            for f in self.fichas:
#                if f.id_casilla()==id_casilla and f.jugador!=self.jugadoractual.id:
#                    return (True, f)
#            return (False, None)
        if ruta>72:
            print "en como se ha sobrepasado el 72"
            return False
        idcasilladestino=libglparchis.ruta[ruta][ficha.jugador]
        
        if self.casillas[idcasilladestino].seguro==True:
            return False
        
        if len(self.casillas[idcasilladestino].buzon)==1:
            fichaenbuzon=self.casillas[idcasilladestino].buzon[0]
            if fichaenbuzon.jugador!=self.jugadoractual:
                self.mover(fichaenbuzon, 0)
                self.jugadoractual.movimientos_acumulados=20
                self.log("He comido la ficha"+ fichaenbuzon.name)

                return True
                    
            
            
    def mete(self, ficha):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""
#        def hay_ficha_otro_jugador(id_casilla):
#            for f in self.fichas:
#                if f.id_casilla()==id_casilla and f.jugador!=self.jugadoractual.id:
#                    return (True, f)
#            return (False, None)
        
        if ficha.ruta==72:
            self.jugadoractual.movimientos_acumulados=10
            self.log("He metido la ficha "+ ficha.name)
            return True
        return False



    def after_dado_click(self,  numerodado):
        if numerodado==6 and len(self.jugadoractual.historicodado)==3:            
            self.emit(SIGNAL("TresSeisesSeguidos()"))      
            print "Ultima ficha movida",  self.jugadoractual.lastFichaMovida
            if self.jugadoractual.lastFichaMovida!=None:
                print self.jugadoractual.lastFichaMovida.name
                casilla=self.jugadoractual.lastFichaMovida.id_casilla()
                if self.casillas[casilla].rampallegada==True:
                    self.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    self.log(self.trUtf8("Han salido tres seises, la ´ultima ficha movida se va a casa"))
                    self.mover(self.jugadoractual.lastFichaMovida, 0)
            else:               
                self.log("Despu´es de tres seises, ya no puede volver a tirar")
            self.emit(SIGNAL("CambiarJugador()"))
        else: # si no han salido 3 seises
            if self.AlgunaPuedeMover()==True:
                print "sale"
                self.emit(SIGNAL("JugadorDebeMover()"))
            else:#alguna no puede mover.
                if self.jugadoractual.historicodado[0]==6:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:            
                    self.emit(SIGNAL("CambiarJugador()"))


    def busca_ficha(self, id):
        for c in libglparchis.colores:
            for f in self.jugadores[c].fichas:
                if self.jugadores[c].fichas[f].id==id:
                    return self.jugadores[c].fichas[f]
#                self.fichas.append(self.jugadores[c].fichas[f])

    def after_ficha_click(self):
        puede=self.PuedeMover(self.selFicha,  self.dado.lastthrow)
        if puede[0]==False:
            self.log("No puede mover esta ficha, seleccione otra")
            return
        
        self.mover(self.selFicha, self.selFicha.ruta + puede[1])
        
        #Comprueba si ha ganado
        if self.jugadoractual.HaGanado()==True:
            self.emit(SIGNAL("HaGanado()"))
        
        #Come
        if self.come(self.selFicha, self.selFicha.ruta+puede[1])==True:
            print ("come")
            if self.AlgunaPuedeMover()==False:
                if self.habiaSalidoSeis()==True:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:
                    self.emit(SIGNAL("CambiarJugador()"))                
            else:#si alguna puede mover
                self.emit(SIGNAL("JugadorDebeMover()"))
        print ("No come")
        
        #Mete
        if self.mete(self.selFicha)==True:
            print ("mete")
            if self.AlgunaPuedeMover()==False:
                if self.habiaSalidoSeis()==True:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:
                    self.emit(SIGNAL("CambiarJugador()"))                
            else:#si alguna puede mover
                self.emit(SIGNAL("JugadorDebeMover()"))
        print (" No mete")       
        
        if self.habiaSalidoSeis()==True:
            self.emit(SIGNAL("JugadorDebeTirar()"))
        else:
            self.emit(SIGNAL("CambiarJugador()"))      




    def mover(self, ficha, ruta):
        if ficha==None:
            print ("esta ficha es None y no se porque")
            return
        idcasillaorigen=ficha.id_casilla()
        idcasilladestino=libglparchis.ruta[ruta][ficha.jugador]        
        ficha.last_ruta=ficha.ruta
        try:
            self.casillas[idcasillaorigen].buzon.remove(ficha)
        except:
            print ("La ficha no estaba en el buz´on de la casilla "+str(idcasillaorigen),  ficha, self.casillas[idcasillaorigen].buzon )
        ficha.ruta=ruta#cambia la ruta
        self.casillas[idcasilladestino].buzon.append(ficha)
#        print self.casillas[idcasilladestino].buzon,  ficha
        self.LastFichaMovida=ficha
        return True


class Ficha(QGLWidget):
    def __init__(self, name,  parent=None):
        QGLWidget.__init__(self, parent)
        self.name=name
        self.ruta=0
        self.last_ruta=0
        self.color=libglparchis.qcolor(name[:-1])
        self.colorname=name[:-1]
        self.ficha=GLU.gluNewQuadric();
        self.jugador=libglparchis.colorid(name[:-1])#utilizado para array ruta
#        self.numposicion=None#Posicion dentro de la casilla
        self.id=libglparchis.fichas_name2id(name)

    def id_casilla(self):
        return libglparchis.ruta[self.ruta][self.jugador]
        
    def EstaEnCasa(self):
        if self.ruta==0:
            return True
        return False
        
                
    def EstaEnMeta(self):
        if self.ruta==72:
            return True
        return False

        
        
        
    def defineColor(self,  id):
        if id>=0 and id<=3:
           return QColor(255, 255, 0)        
        elif id>=4 and id<=7:
           return QColor(0, 0, 255)
        elif id>=8 and id<=11:
           return QColor(255, 0, 0 )
        elif id>=12 and id<=15:
           return QColor(0, 255, 0)


    def dibujar(self, posicionBuzon):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(libglparchis.Name.ficha[self.id]);
        if posicionBuzon==None:#Para frmAcercade
            p=(0, 0, 0)
        else:
            p=libglparchis.posFichas[self.id_casilla()][posicionBuzon]
        GL.glTranslated(p[0], p[1], p[2])
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        self.qglColor(QColor(255, 255, 0).dark())
        GLU.gluQuadricDrawStyle (self.ficha, GLU.GLU_FILL);
        GLU.gluQuadricNormals (self.ficha, GLU.GLU_SMOOTH);
        GLU.gluQuadricTexture (self.ficha, True);
        self.qglColor(self.color.dark())
        GLU.gluCylinder (self.ficha, 1.4, 1.4, 0.5, 16, 5)
        GL.glTranslated(0, 0, 0.5)
        self.qglColor(QColor(70, 70, 70))
        GLU.gluDisk(self.ficha, 0, 1.4, 16, 5)
        self.qglColor(self.color.dark())
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

    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])

    def dibujar(self):
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

        self.quad(v4, v3, v2, v1, QColor(0, 64, 64))      
        self.quad(v5, v6, v7, v8, QColor(0, 64, 64))      
        self.quad(v5, v8, v4, v1, QColor(0, 64, 64))      
        self.quad(v2, v3, v7, v6, QColor(0, 64, 64))      
        self.quad(v1, v2, v6, v5, QColor(0, 64, 64))      
        self.quad(v8, v7, v3, v4, QColor(0, 64, 64))      

        GL.glEnd()
        GL.glPopMatrix()
