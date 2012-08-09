# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from OpenGL import GL,  GLU
from libglparchis import *


class wdgOGL(QGLWidget):
    """Clase principal del Juego, aquí está fundamentalmente la representaci´on.
   Emite click ficha cuando se realiza"""
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0

    def assign_mem(self, mem):
        self.mem=mem

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
                self.mem.selFicha=None
            elif len(objetos)==2:
                self.mem.selFicha=Name.object(self.mem, objetos[1])
                print (self.mem.selFicha)
                
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
                self.showCasillaFicha (selCasilla, None)
            elif len(objetos)==2:
                selCasilla=Name.object(self.mem, objetos[0])
                selFicha=Name.object(self.mem, objetos[1])
                self.showCasillaFicha (selCasilla, selFicha)
                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event)            
            if self.mem.selFicha!=None:
                self.mem.jugadoractual.log(self.trUtf8("Se ha hecho click en la ficha %1").arg(self.mem.selFicha.id))
                self.emit(SIGNAL("fichaClicked()"))#No se pasa par´ametro porque es self.mem.selFicha
        elif event.buttons() & Qt.RightButton:
            pickupright(event)                    
        self.updateGL()
            
    def showCasillaFicha(self, selCasilla, selFicha):
        """selCasilla y selFicha son objetos"""
        a=frmShowCasilla(self,  Qt.Popup,  selCasilla)
        a. move(self.ogl.mapToGlobal(QPoint(10, 10))        )
        a.show()
        if selFicha!=None:
            a=frmShowFicha(self, Qt.Popup,  selFicha)
            a. move(self.ogl.mapToGlobal(QPoint(500, 10))        )
            a.show()

