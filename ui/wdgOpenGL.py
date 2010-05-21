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
        self.tipo=self.defineTipo(id)

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
           return QColor(255, 255, 0)        
        elif id==39 or (id>=85 and id<=92) or id==103:
           return QColor(255, 0, 0)
        elif id==22 or (id>=77 and id<=84) or id==102:
           return QColor(0, 0, 255)
        elif id==56 or (id>=93 and id<=100) or id==104:
           return QColor(0, 255, 0)
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
        
    def tipo_inicio(self):
        GL.glPushMatrix()
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
        GL.glPopMatrix()

    def tipo_normal(self):
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

        self.quad(v1, v2, v3, v4, self.color)      
        self.quad(v8, v7, v6, v5,QColor(70, 70, 70) )      
        self.quad(v1, v4, v8, v5,QColor(170, 170, 170))      
        self.quad(v6, v7, v3, v2, QColor(170, 170, 170))      
        self.quad(v5, v6, v2, v1, QColor(170, 170, 170) )      
        self.quad(v4, v3, v7, v8, QColor(170, 170, 170))      

        GL.glEnd()
        self.border(v5, v6, v7, v8, QColor(0, 0, 0))
        GL.glPopMatrix()
        
    def tipo_oblicuoi(self):
        GL.glPushMatrix()
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
        GL.glPopMatrix() 

    def tipo_oblicuod(self):
        GL.glPushMatrix()
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
        GL.glPopMatrix() 
        
    def tipo_final(self):
        GL.glPushMatrix()
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
        GL.glPopMatrix()
        
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
class wdgOpenGL(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.tablero.position=(-1, -1, 0)
        self.rotX=0
        self.lastPos = QPoint()
        self.casillas=[]
        for i in range(0, 104):
            self.casillas.append(Casilla(i+1))
        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)


    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
#        self.tablero.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        
        
        GL.glFrontFace(GL.GL_CCW);

        light_ambient =  (1, 1, 1, 1);
        light_diffuse =  (0, 0, 1, 0);
        light_specular =  (0, 0, 0, 0);
        light_position =  (5.0, 5.0, 5.0, 0.0);


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

        
        GL.glTranslated(-31.5, -31.5,  -100)
        GL.glRotated(self.rotX, 1,0.3 , 0.3)
#        GL.glRotated(180,  1,0 , 0)
        self.tablero.makeObject()
#        GL.glCallList(self.tablero.object)
        for c in self.casillas:
            c.dibujar()

    def resizeGL(self, width, height):
        GL.glViewport(0, 0, width, height)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
#        GL.glOrtho(-1, +64, +64, -1, 2.0, 25.0)
        aspect=width/height
        GLU.gluPerspective(60.0, aspect, 1, 400)
        GL.glMatrixMode(GL.GL_MODELVIEW)



    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Escape) or (event.key() == Qt.Key_Q):
            self.close()

        if event.key() == Qt.Key_Q: # toggle mode
            self.updateGL()
                
    def mousePressEvent(self, event):
        self.lastPos = QPoint(event.pos())
        self.setFocus()
        if event.buttons() & Qt.RightButton:
            return
        self.updateGL()

    def wheelEvent(self, event):
        if event.delta() > 0:
           self.rotX=self.rotX-30;
        else:
           self.rotX=self.rotX+30;
        self.updateGL()

class Ficha(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.ficha=GLU.gluNewQuadric();
#
#            
#    def quad(self, p1, p2, p3, p4, color):
#        self.qglColor(color)
#        GL.glVertex3d(p1[0], p1[1], p1[2])
#        GL.glVertex3d(p2[0], p2[1], p2[2])
#        GL.glVertex3d(p3[0], p3[1], p3[2])
#        GL.glVertex3d(p4[0], p4[1], p4[2])
#    def border(self):        
#        GL.glBegin(GL.GL_LINES)
#        b5 = (0, 0, 0.021)
#        b6 = (0.7, 0, 0.021)
#        b7 = (0.7, 0.3, 0.021)
#        b8 = (0, 0.3, 0.021)
#        GL.glVertex3d(b5[0], b5[1], b5[2])
#        GL.glVertex3d(b6[0], b6[1], b6[2])
#        GL.glVertex3d(b7[0], b7[1], b7[2])
#        GL.glVertex3d(b8[0], b8[1], b8[2])
#        GL.glEnd()
#        
    def makeObject(self, color):
#        genList = GL.glGenLists(self.object)
#        GL.glNewList(genList, GL.GL_COMPILE)
        GL.glPushMatrix()
        self.qglColor(QColor(255, 255, 0))
        GLU.gluQuadricDrawStyle (self.ficha, GLU.GLU_FILL);
        GLU.gluQuadricNormals (self.ficha, GLU.GLU_SMOOTH);
        GLU.gluQuadricTexture (self.ficha, True);
#        glTranslated(.4,.4,0);
        self.qglColor(color)
        GLU.gluCylinder (self.ficha, 2.9, 2.9, 0.5, 16, 5)
        GL.glTranslated(0, 0, 0.5)
        self.qglColor(QColor(70, 70, 70))
        GLU.gluDisk(self.ficha, 0, 2.9, 16, 5)
        self.qglColor(color.dark())
        GL.glTranslated(0, 0, -0.5)
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        GLU.gluDisk(self.ficha, 0, 2.9, 16, 5)
        GL.glPopMatrix()
        
#        GL.glEndList()

#        return genList

class Tablero(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.position=(0, 0, 0)


            
    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])

        
    def makeObject(self):
#        genList = GL.glGenLists(self.object)
#        GL.glNewList(genList, GL.GL_COMPILE)
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
            

#        GL.glEndList()

#        return genList
