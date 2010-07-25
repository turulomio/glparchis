## -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
import math
from OpenGL import GL
from wdgGame import *

class wdgShowObject(QGLWidget):
    def __init__(self, parent=None):
        self.ortho=(-4.5, +4.5, +4.5, -4.5, 4.0, 15.0)
        QGLWidget.__init__(self, parent)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.objeto=0

        self.lastPos = QPoint()
        
        self.trolltechGreen = QColor.fromCmykF(0.40, 0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)
        
        #Carga el primer objeto
        self.cas= Casilla(1)
        self.ficha=Ficha(1)
        self.tablero=Tablero()
        self.cas.position=(-3.5, -1.5, 0, 0)
        self.cas.tipo=3
        self.cas.color=QColor(255, 255, 255) 

    
    def changeOrtho(self):
        side = min(self.width(), self.height())
        GL.glViewport((self.width() - side) / 2, (self.height() - side) / 2, side, side)      
        self.updateOverlayGL()                          
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(self.ortho[0], self.ortho[1], self.ortho[2], self.ortho[3], self.ortho[4], self.ortho[5] )
        GL.glMatrixMode(GL.GL_MODELVIEW)
        self.updateGL()         

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(400, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.emit(SIGNAL("xRotationChanged(int)"), angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.emit(SIGNAL("yRotationChanged(int)"), angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.emit(SIGNAL("zRotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        
    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(0.0, 0.0, -10.0)
        GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        #Aquí no añadir calculos hacerlo en dobleclick
        if self.objeto==0:
            self.cas.dibujar()
        elif self.objeto==1:
            self.cas.dibujar()
        elif self.objeto==2:
            self.cas.dibujar()
        elif self.objeto==3:
            self.cas.dibujar()
        elif self.objeto==4:
            self.cas.dibujar()
        elif self.objeto==5:
            self.ficha.dibujar()
        elif self.objeto==6:
            self.tablero.dibujar()


    def resizeGL(self, width, height):
        side = min(width, height)
        GL.glViewport((width - side) / 2, (height - side) / 2, side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(self.ortho[0], self.ortho[1], self.ortho[2], self.ortho[3], self.ortho[4], self.ortho[5] )
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mouseDoubleClickEvent(self, event): 
        if event.buttons() & Qt.LeftButton:
            self.objeto=self.objeto+1
            if self.objeto>=7:
                self.objeto=0
            print "Visualizando el objeto: " + str(self.objeto)

        if self.objeto==0:#normal
            self.cas.position=(-3.5, -1.5, 0, 0)
            self.cas.tipo=3
            self.cas.color=QColor(255, 255, 255) 
            self.ortho=(-4.5, +4.5, +4.5, -4.5, 4.0, 15.0)
            self.changeOrtho()
        elif self.objeto==1:#inicio
            self.cas.position=(-10.5, -10.5, 0, 0)
            self.cas.tipo=0
            self.cas.color=QColor(0, 255, 0) 
            self.ortho=(-15, +15, +15, -15, -10, 50.0)
            self.changeOrtho()        
        elif self.objeto==2:#oblicuoi
            self.cas.position=(-3.5, -1.5, 0, 0)
            self.cas.tipo=2
            self.cas.color=QColor(255, 0, 0) 
            self.ortho=(-4.5, +4.5, +4.5, -4.5, 4.0, 15.0)
            self.changeOrtho()     
        elif self.objeto==3:#oblicuod
            self.cas.position=(-3.5, -1.5, 0, 0)
            self.cas.tipo=4
            self.cas.color=QColor(0, 0, 255) 
            self.ortho=(-4.5, +4.5, +4.5, -4.5, 4.0, 15.0)
            self.changeOrtho()
        elif self.objeto==4:#final
            self.cas.position=(-7.5, -3.75, 0, 0)
            self.cas.tipo=1
            self.cas.color=QColor(255, 255, 0) 
            self.ortho=(-8.5, +8.5, +8.5, -8.5, -10.0, 25.0)
            self.changeOrtho()
        elif self.objeto==5:#ficha
            self.ficha.position=(-1.45, -1.45, 0, 0)
            self.ortho=(-49, +49, +49, -49, -10.0, 25.0)
            self.changeOrtho()
        elif self.objeto==6:#tablero
            self.tablero.position=(-32.5, -32.5, 0, 0)
            self.ortho=(-53, +53, +53, -53, -60.0, 80.0)
            self.changeOrtho()


    def mousePressEvent(self, event):
        self.lastPos = QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = QPoint(event.pos())
