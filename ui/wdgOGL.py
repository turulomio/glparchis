# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from OpenGL import GL,  GLU
from libglparchis import *


class wdgOGL(QGLWidget):
    """Clase principal del Juego, aquí está toda la ciencia, cuando se deba pasar al UI se crearán emits que captura qT para el UI"""
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0
        self.lastPos = QPoint()
        self.selFicha=None
        self.selCasilla=None

        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        
    def assign_mem(self, mem):
        self.mem=mem

        
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

#    def log(self, cadena):
#            self.emit(SIGNAL("newLog(QString)"),cadena)

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

                
        def process(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                   objetos.append(names[0])
            
            if len(objetos)==1:
                self.selCasilla=Name.object(self.mem, objetos[0])
                self.selFicha=None
            elif len(objetos)==2:
                self.selCasilla=Name.object(self.mem, objetos[0])
                self.selFicha=Name.object(self.mem, objetos[1])
                self.mem.jugadoractual.log(self.trUtf8("Se ha hecho click en la ficha %1").arg(self.selFicha.id))
                
        def processright(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
#                print minDepth,  maxDepth,  names
                if len(names)==1:
                   objetos.append(names[0])
#            print len(objetos)
            if len(objetos)==1:
                selCasilla=Name.object(self.mem, objetos[0])
                self.emit(SIGNAL("showCasillaFicha(int,int)"), selCasilla.id, -99)
            elif len(objetos)==2:
                selCasilla=Name.object(self.mem, objetos[0])
                selFicha=Name.object(self.mem, objetos[1])
                self.emit(SIGNAL("showCasillaFicha(int,int)"),selCasilla.id, selFicha.id)
                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event)            
            if self.selFicha!=None:
                self.after_ficha_click()
        elif event.buttons() & Qt.RightButton:
            pickupright(event)                    
        self.updateGL()



            
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
        
#        print len(self.dic_casillas[idcasilladestino].buzon)
        if len(self.dic_casillas[idcasilladestino].buzon)==2:
            ficha1=self.dic_casillas[idcasilladestino].buzon[0]
            ficha2=self.dic_casillas[idcasilladestino].buzon[1]
            if ficha1.jugador!=self.mem.jugadoractual.id:
                fichaacomer=ficha1
            elif ficha2.jugador!=self.mem.jugadoractual.id:
                fichaacomer=ficha2
            else:
                return False
            fichaacomer.mover(0, False)
            self.mem.jugadoractual.movimientos_acumulados=20
            self.mem.jugadoractual.log(self.trUtf8("He comido la ficha %1").arg(fichaacomer.name))
            return True
                
            
            
    def mete(self, ficha):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""      
        if ficha.ruta==72:
            self.mem.jugadoractual.movimientos_acumulados=10
            self.mem.jugadoractual.log(self.trUtf8("He metido la ficha %1").arg(ficha.name))
            return True
        return False


#
#    def busca_ficha(self, id):
#        for f in self.mem.fichas():
#            if f.id==id:
#                return f
#        for c in self.mem.colores():
#            for f in self.mem.juga[c].fichas:
#                if self.dic_jugadores[c].fichas[f].id==id:
#                    return self.dic_jugadores[c].fichas[f]

    def after_ficha_click(self):
        puede=self.selFicha.PuedeMover(self.mem,  self.dado.lastthrow)
        if puede[0]==False:
            self.mem.jugadoractual.log(self.trUtf8("No puede mover esta ficha, seleccione otra"))
            return
        
        self.mover(self.selFicha, self.selFicha.ruta + puede[1])
        #Quita el movimiento acumulados
        if self.mem.jugadoractual.movimientos_acumulados in (10, 20):
            self.mem.jugadoractual.movimientos_acumulados=None
            
            
        #Comprueba si ha ganado
        if self.mem.jugadoractual.HaGanado()==True:
            self.emit(SIGNAL("HaGanado()"))
        
        #Come
        if self.come(self.selFicha, self.selFicha.ruta)==True:
            if self.mem.jugadoractual.fichas.AlgunaPuedeMover(self.mem)==False:
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
            if self.mem.jugadoractual.fichas.AlgunaPuedeMover(self.mem)==False:
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
#            self.mem.jugadoractual.LastFichaMovida=ficha
#        return True

