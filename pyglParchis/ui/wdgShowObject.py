from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtGui import QPixmap, QColor

from OpenGL.GL import glClear, glEnable, glLoadIdentity, glMatrixMode, glOrtho, glRotated, glScaled, glShadeModel, glTranslated, glViewport, GL_COLOR_BUFFER_BIT, GL_CULL_FACE, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, GL_FLAT, GL_MODELVIEW, GL_PROJECTION
from libglparchis import Color, Casilla, Ficha, Jugador, Tablero, Coord3D, Dado

class wdgShowObject(QGLWidget):
    xRotationChanged=pyqtSignal(int)
    yRotationChanged=pyqtSignal(int)
    zRotationChanged=pyqtSignal(int)
    def __init__(self, parent=None):
        self.ortho=(-9, +9, +9, -9, -25.0, 25.0)
        QGLWidget.__init__(self, parent)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.objeto=0
        self.texNumeros=[]
        self.texDecor=[]

        self.lastPos = QPoint()
               
        #Carga el primer objeto    
        self.cas= Casilla(1, 2, Color(0, 0, 255) , (-3.5, -1.5, 0, 0), 0, False, False, 3,  False, (0, 0, 0), False)
        self.casinicio= Casilla(1, 2, Color(255, 0, 0) , (-3.5, -1.5, 0, 0), 0, False, False, 0,  False, (0, 0, 0), False)
        self.ficha=Ficha(None, 0, 1, Color(255, 0, 0), Jugador(None, Color(255, 0, 0)), None)
        self.tablero=Tablero(4)
        self.tablero.position=Coord3D(0, 0, 0)
        self.tablero6=Tablero(6)
        self.tablero6.position=Coord3D(0, 0, 0)
        self.tablero8=Tablero(8)
        self.tablero8.position=Coord3D(0, 0, 0)
        self.dado=Dado()
        self.dado.showing=True
        self.lasttirada=5

    
    def changeOrtho(self):
        side = min(self.width(), self.height())
        glViewport((self.width() - side) / 2, (self.height() - side) / 2, side, side)      
        self.updateOverlayGL()                          
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(self.ortho[0], self.ortho[1], self.ortho[2], self.ortho[3], self.ortho[4], self.ortho[5] )
        glMatrixMode(GL_MODELVIEW)
        self.updateGL()         


    def initializeGL(self): 
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/0.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/1.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/2.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/3.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/4.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/5.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/6.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/7.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/8.png')))
        self.texNumeros.append(self.bindTexture(QPixmap(':/glparchis/9.png')))
        
        self.texDecor.append(self.bindTexture(QPixmap(':/glparchis/casillainicial.png')))
        self.texDecor.append(self.bindTexture(QPixmap(':/glparchis/transwood.png')))
        self.texDecor.append(self.bindTexture(QPixmap(':/glparchis/seguro.png')))
        self.texDecor.append(self.bindTexture(QPixmap(':/glparchis/dado_desplegado.png')))
        self.qglClearColor(QColor.darker(QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)))
        glShadeModel(GL_FLAT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        
    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle

    def showObject(self, obj):
        self.objeto=obj
        print ("Visualizando el objeto: " + str(self.objeto))
        self.paintGL()
        self.updateGL()


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -10.0)
        glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
        if self.objeto==0:
            glScaled(0.1, 0.1,0.1)
            self.tablero.dibujar(self)
        elif self.objeto==1:
            glScaled(0.1, 0.1,0.1)
            self.tablero6.dibujar(self)
        elif self.objeto==2:
            glScaled(0.1, 0.1,0.1)
            self.tablero8.dibujar(self)
        elif self.objeto==3:
            glScaled(1.5, 1.5,1.5)
            self.dado.draw(self)
        elif self.objeto==4:
            self.cas.dibujar(self)
        elif self.objeto==5:
            glScaled(0.4, 0.4,0.4)
            self.casinicio.dibujar(self)
        elif self.objeto==6:
            glScaled(2, 2,2)
            self.ficha.dibujar(self, None)


    def resizeGL(self, width, height):
        side = min(width, height)
        glViewport(int((width - side) / 2.0), int((height - side) / 2.0), side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(self.ortho[0], self.ortho[1], self.ortho[2], self.ortho[3], self.ortho[4], self.ortho[5] )
        glMatrixMode(GL_MODELVIEW)


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
#            self.emit(SIGNAL("xRotationChanged(int)"), angle)
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
#            self.emit(SIGNAL("yRotationChanged(int)"), angle)
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
#            self.emit(SIGNAL("zRotationChanged(int)"), angle)
            self.zRotationChanged.emit(angle)
            self.updateGL()
            
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
