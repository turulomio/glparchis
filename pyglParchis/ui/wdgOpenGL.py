## -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
import math
from OpenGL import GL,  GLU
import datos

class Casilla(QGLWidget):
    def __init__(self, id, parent=None):
        QGLWidget.__init__(self, parent)
        self.id=id
        self.color=self.defineColor(id)
        self.position=datos.posCasillas[id]
        self.rotate=self.defineRotate(id)

    def defineColor(self,  id):
        if id==5 or (id>=69 and id<=75):
           return QColor(255, 255, 0)        
        elif id==39 or (id>=85 and id<=91):
           return QColor(255, 0, 0)
        elif id==22 or (id>=76 and id<=84):
           return QColor(0, 0, 255)
        elif id==56 or (id>=92 and id<=99):
           return QColor(0, 255, 0)
        elif id==68 or  id==63 or  id==51 or id==46 or id==34 or  id==29 or  id==17 or   id==12:  
           return QColor(128, 128, 128)
        else:
            return QColor(255, 255, 255)
            
    def defineRotate(self,  id):
        if (id>=10 and id<=24) or (id>=76 and id<=84) or(id>=43 and id <=59) or (id>=92 and id<=99):
           return 90
        else:
            return 0
        
    def dibujar(self):       
        GL.glPushMatrix()
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

        self.quad(v1, v2, v3, v4, QColor(0, 0, 0))      
        self.quad(v8, v7, v6, v5, self.color)      
        self.quad(v1, v4, v8, v5, QColor(0, 0, 0))      
        self.quad(v2, v3, v7, v6, QColor(0, 0, 0))      
        self.quad(v1, v2, v6, v5, QColor(0, 0, 0))      
        self.quad(v4, v3, v7, v8, QColor(0, 0, 0))      

        GL.glEnd()
        self.border()
        GL.glPopMatrix()
            
    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])
        
    def border(self):        
        GL.glBegin(GL.GL_LINES)
        b5 = (0, 0, 0.21)
        b6 = (7, 0, 0.21)
        b7 = (7, 3, 0.21)
        b8 = (0, 3, 0.21)
        GL.glVertex3d(b5[0], b5[1], b5[2])
        GL.glVertex3d(b6[0], b6[1], b6[2])
        GL.glVertex3d(b7[0], b7[1], b7[2])
        GL.glVertex3d(b8[0], b8[1], b8[2])
        GL.glEnd()

class wdgOpenGL(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        
        self.lastPos = QPoint()
        self.casillas=[]
        for i in range(0, 104):
            self.casillas.append(Casilla(i+1))
        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)


    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
        self.tablero.makeObject()
#NO POR COLOR Y NUMEROS        self.casillas[0].makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
#        GL.glCullFace(GL_FRONT_AND_BACK)

    def paintGL(self):   
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(0, 0, -4)
#        GLU.gluLookAt(0,0,50,    0, 0,-100    ,0,1,0);
#        GLU.gluLookAt(10.5,12,   36,10.5,   12,0,0,1,0);

        GL.glCallList(self.tablero.object)
        for c in self.casillas:
            c.dibujar()

    def resizeGL(self, width, height):
        GL.glViewport(0, 0, width, height)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-1, +64, +64, -1, 2.0, 25.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)



    def keyPressEvent(self, event):
        print "hola"
        if (event.key() == Qt.Key_Escape) or (event.key() == Qt.Key_Q):
            self.close()

        if event.key() == Qt.Key_Q: # toggle mode
            self.updateGL()
                
    def mousePressEvent(self, event):
        self.lastPos = QPoint(event.pos())
        
        if event.buttons() & Qt.RightButton:
            return
        self.updateGL()


class Tablero(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1


            
    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])
    def border(self):        
        GL.glBegin(GL.GL_LINES)
        b5 = (0, 0, 0.021)
        b6 = (0.7, 0, 0.021)
        b7 = (0.7, 0.3, 0.021)
        b8 = (0, 0.3, 0.021)
        GL.glVertex3d(b5[0], b5[1], b5[2])
        GL.glVertex3d(b6[0], b6[1], b6[2])
        GL.glVertex3d(b7[0], b7[1], b7[2])
        GL.glVertex3d(b8[0], b8[1], b8[2])
        GL.glEnd()
        
    def makeObject(self):
        genList = GL.glGenLists(self.object)
        GL.glNewList(genList, GL.GL_COMPILE)
        GL.glPushMatrix()
        GL.glTranslated(0,0, -2)
        GL.glBegin(GL.GL_QUADS)
        v1 = (0, 0, 0)
        v2 = (63, 0, 0)
        v3 = (63, 63, 0)
        v4 = (0, 63, 0)
        v5 = (0, 0, 2)
        v6 = (63, 0, 2)
        v7 = (63, 63, 2)
        v8 = (0, 63, 2)

        self.quad(v1, v2, v3, v4, QColor(10, 10, 0))      
        self.quad(v8, v7, v6, v5, QColor(0, 64, 64))      
        self.quad(v1, v4, v8, v5, QColor(10, 10, 0))      
        self.quad(v2, v3, v7, v6, QColor(10, 10, 0))      
        self.quad(v1, v2, v6, v5, QColor(10, 10, 0))      
        self.quad(v4, v3, v7, v8, QColor(10, 10, 0))      

        GL.glEnd()
        self.border()
        GL.glPopMatrix()
            

        GL.glEndList()

        return genList
