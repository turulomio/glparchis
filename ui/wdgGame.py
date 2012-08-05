# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
import ConfigParser,  random
from OpenGL import GL,  GLU
from libglparchis import *


class wdgGame(QGLWidget):
    """Clase principal del Juego, aquí está toda la ciencia, cuando se deba pasar al UI se crearán emits que captura qT para el UI"""
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0
        self.lastPos = QPoint()
        self.selFicha=None
        self.selCasilla=None
        self.jugadoractual=None
        self.dado=None

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        
    def assign_mem(self, mem):
        self.mem=mem

    def load_file(self, filename):
        self.rotX=0
        self.lastPos = QPoint()
        self.selFicha=None
        self.selCasilla=None
        self.dado=Dado()
        
        
        config = ConfigParser.ConfigParser()
        config.read(filename)

        yellow=self.mem.jugadores('yellow')
        yellow.name=config.get('yellow', 'name')
        yellow.ia=i2b(config.getint("yellow", "ia"))
        yellow.plays=(i2b(config.getint("yellow", "plays")))
        
        blue=self.mem.jugadores('blue')
        blue.name=config.get("blue", "name")
        blue.ia=i2b(config.getint("blue", "ia"))
        blue.plays=(i2b(config.getint("blue", "plays")))
        
        red=self.mem.jugadores('red')
        red.name=config.get("red", "name")
        red.ia=i2b(config.getint("red", "ia"))
        red.plays=(i2b(config.getint("red", "plays")))
        
        green=self.mem.jugadores('green')
        green.name=config.get("green", "name")
        green.ia=i2b(config.getint("green", "ia"))
        green.plays=(i2b(config.getint("green", "plays")))  

        for j in self.mem.jugadores():
            if j.plays==True:
                j.fichas.arr[0].mover(  config.getint(j.id, "rutaficha1"), False,  True)
                j.fichas.arr[0].mover(config.getint(j.id, "rutaficha2"), False,  True)
                j.fichas.arr[0].mover(config.getint(j.id, "rutaficha3"), False,  True)
                j.fichas.arr[0].mover(config.getint(j.id, "rutaficha4"), False,  True)
#            self.mover(yellow.fichas["yellow2"], config.getint("yellow", "rutaficha2"), False)
#            self.mover(yellow.fichas["yellow3"], config.getint("yellow", "rutaficha3"), False)
#            self.mover(yellow.fichas["yellow4"], config.getint("yellow", "rutaficha4"), False)
#        if blue.plays==True:
#            self.mover(blue.fichas["blue1"], config.getint("blue", "rutaficha1"), False)
#            self.mover(blue.fichas["blue2"], config.getint("blue", "rutaficha2"), False)
#            self.mover(blue.fichas["blue3"], config.getint("blue", "rutaficha3"), False)
#            self.mover(blue.fichas["blue4"], config.getint("blue", "rutaficha4"), False)
#        if red.plays==True:
#            self.mover(red.fichas["red1"], config.getint("red", "rutaficha1"), False)
#            self.mover(red.fichas["red2"], config.getint("red", "rutaficha2"), False)
#            self.mover(red.fichas["red3"], config.getint("red", "rutaficha3"), False)
#            self.mover(red.fichas["red4"], config.getint("red", "rutaficha4"), False)
#        if green.plays==True:
#            self.mover(green.fichas["green1"], config.getint("green", "rutaficha1"), False)
#            self.mover(green.fichas["green2"], config.getint("green", "rutaficha2"), False)
#            self.mover(green.fichas["green3"], config.getint("green", "rutaficha3"), False)
#            self.mover(green.fichas["green4"], config.getint("green", "rutaficha4"), False)
#        
        fake=config.get("game", 'fakedice')
        if fake!="":
            for i in  fake.split(";")  :
                self.dado.fake.append(int(i))
        print (self.dado.fake)
        self.jugadoractual=self.mem.jugadores(config.get("game", 'playerstarts'))    
        self.jugadoractual.historicodado=[]
        self.jugadoractual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadoractual.LastFichaMovida=None #Se utiliza cuando se va a casa
        
    def initializeGL(self):
        print ("initializeGL")
        self.qglClearColor(self.trolltechPurple.dark())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        
        GL.glFrontFace(GL.GL_CCW);

        light_ambient =  (0.3, 0.3, 0.3, 0.1);

        GL.glEnable(GL.GL_LIGHTING)
        lightpos=(0, 0, 50)
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_AMBIENT, light_ambient)  
        GL.glLightfv(GL.GL_LIGHT0, GL.GL_POSITION, lightpos)  
        GL.glEnable(GL.GL_LIGHT0);
        GL.glEnable(GL.GL_COLOR_MATERIAL);
        GL.glColorMaterial(GL.GL_FRONT,GL.GL_AMBIENT_AND_DIFFUSE);
        GL.glShadeModel (GL.GL_SMOOTH);

    def log(self, cadena):
            self.emit(SIGNAL("newLog(QString)"),cadena)

    def paintGL(self):   
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(-31.5, -31.5,  -60)
        GL.glRotated(self.rotX, 1,0 , 0)
        self.tablero.dibujar()
        for c in self.mem.casillas():
            c.dibujar() 
            c.dibujar_fichas()

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
                if len(names)==1:
                   objetos.append(names[0])
            
            if len(objetos)==1:
                self.selCasilla=object(objetos[0])
                self.selFicha=None
            elif len(objetos)==2:
                self.selCasilla=self.dic_casillas[object(objetos[0])]
                self.selFicha=self.busca_ficha(object(objetos[1]))
                self.log(self.trUtf8("Se ha hecho click en la ficha %1").arg(self.selFicha.name))
                
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
            if self.PuedeMover(self.jugadoractual.fichas[f], self.dado.lastthrow, True)[0]==True:
                return True
        return False

    def Barreras(self, jugador):
        """Devuelve [] si no y [id_casillas,] si si"""
        resultado =[]
        for f in jugador.fichas:
            casilla=self.dic_casillas[jugador.fichas[f].id_casilla()]
            if casilla.TieneBarrera()==True:
                resultado.append(casilla.id)
        return resultado
        
    def PuedeMover(self, ficha,  valordado,  algunapuedemover=False):
        if algunapuedemover==True:
            pre="APM. "
        else:
            pre=""
        
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
            self.log(self.trUtf8(pre+"No es del jugador actual"))
            return (False, 0)

        #Comprueba que no tenga obligación de abrir barrera
        if valordado==6:
            barreras=self.Barreras(self.jugadoractual)
            if len(barreras)!=0 :
                if ficha.id_casilla() not in barreras:
                    self.log(self.trUtf8(pre+"No se puede mover, debes abrir barrera"))
                    return (False, 0)
            
            

        #Esta en casa y puede mover
        if ficha.EstaEnCasa()==True:
            if valordado!=5: #Saco un 5
                self.log(self.trUtf8(pre+"Necesita sacar un 5 para mover esta ficha"))
                return (False, 0)
                        
        #se ha pasado la meta
        if ficha.ruta+movimiento>72:
            self.log(self.trUtf8(pre+"Se ha pasado la meta"))
            return (False, 0)
                
                
        #Rastrea todas las casillas de paso en busca de barrera.
        for i in range(0, movimiento): 
            id_casilla=ruta[ficha.ruta+i+1][ficha.jugador]
            if self.dic_casillas[id_casilla].TieneBarrera()==True:
                self.log(self.trUtf8(pre+"Hay una barrera"))
                return (False, 0)

           
        #Comprueba si hay sitio libre
        id_casilladestino=ruta[ficha.ruta+movimiento][ficha.jugador]
        if self.dic_casillas[id_casilladestino].haySitioEnBuzon()==False:
            self.log(self.trUtf8(pre+"No hay espacio en la casilla"))
            return (False, 0)
            
        self.log(self.trUtf8(pre+"Puede mover %1").arg(str(movimiento)))
        return (True, movimiento)
            
    def habiaSalidoSeis(self):
        """Se usa después de movimientos acumulados"""
        if self.dado.lastthrow==6:
            return True
        return False
            
    def come(self, ficha,  ruta):
        """ruta, es la posición de ruta de ficha en la que come. Como ya se ha movido, come si puede y devuelve True, en caso contrario False"""
        if ruta>72:
            print ("en como se ha sobrepasado el 72")
            return False
        idcasilladestino=ruta[ruta][ficha.jugador]
        
        if self.dic_casillas[idcasilladestino].seguro==True:
            return False
        
        print len(self.dic_casillas[idcasilladestino].buzon)
        if len(self.dic_casillas[idcasilladestino].buzon)==2:
            ficha1=self.dic_casillas[idcasilladestino].buzon[0]
            ficha2=self.dic_casillas[idcasilladestino].buzon[1]
            if ficha1.jugador!=self.jugadoractual.id:
                fichaacomer=ficha1
            elif ficha2.jugador!=self.jugadoractual.id:
                fichaacomer=ficha2
            else:
                return False
            self.mover(fichaacomer, 0, False)
            self.jugadoractual.movimientos_acumulados=20
            self.log(self.trUtf8("He comido la ficha %1").arg(fichaacomer.name))
            return True
                
            
            
    def mete(self, ficha):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""      
        if ficha.ruta==72:
            self.jugadoractual.movimientos_acumulados=10
            self.log(self.trUtf8("He metido la ficha %1").arg(ficha.name))
            return True
        return False



    def after_dado_click(self,  numerodado):
        if numerodado==6 and len(self.jugadoractual.historicodado)==3:            
            self.emit(SIGNAL("TresSeisesSeguidos()"))      
#            print "Ultima ficha movida",  self.jugadoractual.LastFichaMovida
            if self.jugadoractual.LastFichaMovida!=None:
#                print self.jugadoractual.LastFichaMovida.name
                casilla=self.jugadoractual.LastFichaMovida.id_casilla()
                if self.dic_casillas[casilla].rampallegada==True:
                    self.log(self.trUtf8("Han salido tres seises, no se va a casa por haber llegado a rampa de llegada"))
                else:
                    self.log(self.trUtf8("Han salido tres seises, la última ficha movida se va a casa"))
                    self.mover(self.jugadoractual.LastFichaMovida, 0)
            else:               
                self.log(self.trUtf8("Después de tres seises, ya no puede volver a tirar"))
            self.emit(SIGNAL("CambiarJugador()"))
        else: # si no han salido 3 seises
            if self.AlgunaPuedeMover()==True:
                self.emit(SIGNAL("JugadorDebeMover()"))
            else:#alguna no puede mover.
                if self.jugadoractual.historicodado[0]==6:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:            
                    self.emit(SIGNAL("CambiarJugador()"))


    def busca_ficha(self, id):
        for c in colores:
            for f in self.dic_jugadores[c].fichas:
                if self.dic_jugadores[c].fichas[f].id==id:
                    return self.dic_jugadores[c].fichas[f]

    def after_ficha_click(self):
        puede=self.PuedeMover(self.selFicha,  self.dado.lastthrow)
        if puede[0]==False:
            self.log(self.trUtf8("No puede mover esta ficha, seleccione otra"))
            return
        
        self.mover(self.selFicha, self.selFicha.ruta + puede[1])
        #Quita el movimiento acumulados
        if self.jugadoractual.movimientos_acumulados in (10, 20):
            self.jugadoractual.movimientos_acumulados=None
            
            
        #Comprueba si ha ganado
        if self.jugadoractual.HaGanado()==True:
            self.emit(SIGNAL("HaGanado()"))
        
        #Come
        if self.come(self.selFicha, self.selFicha.ruta)==True:
            if self.AlgunaPuedeMover()==False:
                if self.habiaSalidoSeis()==True:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:
                    self.emit(SIGNAL("CambiarJugador()"))                
            else:#si alguna puede mover
                self.emit(SIGNAL("JugadorDebeMover()"))
#        print ("No come")
        
        #Mete
        if self.mete(self.selFicha)==True:
#            print ("mete")
            if self.AlgunaPuedeMover()==False:
                if self.habiaSalidoSeis()==True:
                    self.emit(SIGNAL("JugadorDebeTirar()"))
                else:
                    self.emit(SIGNAL("CambiarJugador()"))                
            else:#si alguna puede mover
                self.emit(SIGNAL("JugadorDebeMover()"))
#        print (" No mete")       
        
        if self.habiaSalidoSeis()==True:
            self.emit(SIGNAL("JugadorDebeTirar()"))
        else:
            self.emit(SIGNAL("CambiarJugador()"))      




#    def mover(self, ficha, ruta, controllastficha=True):
#        idcasillaorigen=ficha.id_casilla()
#        idcasilladestino=ruta[ruta][ficha.jugador]        
#        ficha.posruta=ficha.ruta
#        try:
#            self.dic_casillas[idcasillaorigen].buzon.remove(ficha)
#        except:
##            print ("La ficha no estaba en el buzón de la casilla "+str(idcasillaorigen),  ficha, self.dic_casillas[idcasillaorigen].buzon )
#            pass
#        ficha.ruta=ruta#cambia la ruta
#        self.dic_casillas[idcasilladestino].buzon.append(ficha)
##        print self.dic_casillas[idcasilladestino].buzon,  ficha
#        if controllastficha==True:
#            self.jugadoractual.LastFichaMovida=ficha
#        return True

