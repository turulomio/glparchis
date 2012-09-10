# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from OpenGL import GL,  GLU
from libglparchis import *
from frmShowCasilla import *
from frmShowFicha import *


class wdgOGL(QGLWidget):
    """Clase principal del Juego, aquí está fundamentalmente la representación.
   Emite click ficha cuando se realiza"""
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0
        
    def assign_mem(self, mem):
        self.mem=mem
        self.dado=QLabel(self)
        self.dado.setScaledContents(True)
        self.dado.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.dado.hide()

    def initializeGL(self):
        print ("initializeGL")
        self.qglClearColor(Color(0, 0, 0).qcolor())
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
        def pickup(event, right):
            """right es si el botón pulsado en el derecho"""
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
            if right==False:
                process(GL.glRenderMode(GL.GL_RENDER))
            else:
                processright(GL.glRenderMode(GL.GL_RENDER))
            GL.glPopMatrix();
            GL.glMatrixMode(GL.GL_MODELVIEW);           
 
            
        def object(mem, id_name):
            """Devuelve un objeto dependiendo del nombre.None si no corresponde"""
            if id_name>=0 and id_name<=15: #fichas van de 0 a 15
                return mem.fichas(id_name)
            elif id_name==16:#tablero 16
                return mem.tablero
            elif id_name>=17 and id_name<=121:#casillas de 17 a 121
                return mem.casillas(id_name-17)
            else:
                return None
                
        def process(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                    objetos.append(names[0])
            
            if len(objetos)==1:
                self.mem.selFicha=None
            elif len(objetos)==2:
                self.mem.selFicha=object(self.mem, objetos[1])
                
        def processright(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                   objetos.append(names[0])
            if len(objetos)==1:
                selCasilla=object(self.mem, objetos[0])
                a=frmShowCasilla(self,  Qt.Popup,  selCasilla)
                a. move(self.mapToGlobal(event.pos())        )
                a.show()
            elif len(objetos)==2:
                selFicha=object(self.mem, objetos[1])
                a=frmShowFicha(self, Qt.Popup,  selFicha)
                a. move(self.mapToGlobal(event.pos())        )
                a.show()
                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event, False)            
            if self.mem.selFicha!=None:
                self.mem.jugadoractual.log(self.trUtf8("Se ha hecho click en la ficha %1").arg(self.mem.selFicha.id))
                self.emit(SIGNAL("fichaClicked()"))#No se pasa parámetro porque es self.mem.selFicha
        elif event.buttons() & Qt.RightButton:
            pickup(event, True)                    
        self.updateGL()

    def showDado(self):
        xl=self.width()/6+6# xleft
        xr=self.width()*5/6-43
        yt=self.height()/6+3#ytop
        yb=self.height()*5/6-43
        if self.mem.jugadoractual.color.name=="yellow":
            self.dado.setGeometry( xl, yt, 40, 40 )
        elif self.mem.jugadoractual.color.name=="blue":
            self.dado.setGeometry(xl, yb, 40, 40)
        elif self.mem.jugadoractual.color.name=="red":
            self.dado.setGeometry(xr, yb, 40, 40)
        elif self.mem.jugadoractual.color.name=="green":
            self.dado.setGeometry(xr, yt, 40, 40)
        self.dado.setPixmap(self.mem.dado.qpixmap(self.mem.jugadoractual.tiradaturno.ultimoValor()))
        self.dado.show()
        self.updateGL()


