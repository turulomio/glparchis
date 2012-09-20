# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from OpenGL.GL import *
from OpenGL.GLU import *
from libglparchis import *
from frmShowCasilla import *
from frmShowFicha import *


class wdgOGL(QGLWidget):
    """Clase principal del Juego, aquí está fundamentalmente la representación.
   Emite click ficha cuando se realiza"""
    def __init__(self,  parent=None,  filename=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.texNumeros=[]
        self.texDecor=[]
        self.rotX=0
        self.visualizacion=0
        
    def assign_mem(self, mem):
        print ("assignmem")
        self.mem=mem
        self.dado=QLabel(self)
        self.dado.setScaledContents(True)
        self.dado.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        self.dado.hide()

    def initializeGL(self):
        #LAS TEXTURAS SE DEBEN CRAR AQUÍ ES LO PRIMERO QUE SE EJECUTA
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/0.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/1.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/2.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/3.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/4.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/5.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/6.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/7.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/8.png')))
        self.texNumeros.append(self.bindTexture(QtGui.QPixmap(':/glparchis/9.png')))
        
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/casillainicial.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/wood.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/seguro.png')))

        print ("initializeGL")
        glEnable(GL_TEXTURE_2D);
        glShadeModel (GL_SMOOTH);
#        self.qglClearColor(Color(0, 0, 0).qcolor())
#        glShadeModel(GL_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        
        glFrontFace(GL_CCW);

        light_ambient =  (0.3, 0.3, 0.3, 0.1);

        glEnable(GL_LIGHTING)
        lightpos=(0, 0, 50)
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)  
        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  
        glEnable(GL_LIGHT0);
        glEnable(GL_COLOR_MATERIAL);
        glColorMaterial(GL_FRONT,GL_AMBIENT_AND_DIFFUSE);

        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);

    def paintGL(self):   
        glLoadIdentity()
        self.qglClearColor(QColor())

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslated(-31.5, -31.5,  -60)
        glRotated(self.rotX, 1,0 , 0)

        self.tablero.dibujar(self)
        for c in self.mem.casillas():
            c.dibujar(self) 
            c.dibujar_fichas(self)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect=width/height
        gluPerspective(60.0, aspect, 1, 400)
        glMatrixMode(GL_MODELVIEW)

    def keyPressEvent(self, event):
#        if (event.key() == Qt.Key_Escape) or (event.key() == Qt.Key_Q):
#            self.close()

        if event.key() == Qt.Key_M: # toggle mode
            if self.visualizacion==0:
                self.rotX=0
            elif self.visualizacion==1:
                self.rotX=340
            self.updateGL()
            
            if self.visualizacion==1:
                self.visualizacion=0
            else:
                self.visualizacion=self.visualizacion+1
    def mousePressEvent(self, event):        
        def pickup(event, right):
            """right es si el botón pulsado en el derecho"""
            viewport=glGetIntegerv(GL_VIEWPORT);
            glMatrixMode(GL_PROJECTION);
            glPushMatrix();
            glSelectBuffer(512);
            glRenderMode(GL_SELECT);
            glLoadIdentity();
            gluPickMatrix(event.x(),viewport[3] -event.y(),1,1, viewport)
            aspect=viewport[2]/viewport[3]
            gluPerspective(60,aspect,1.0,400)
            glMatrixMode(GL_MODELVIEW)
            self.paintGL()
            glMatrixMode(GL_PROJECTION);
            if right==False:
                process(glRenderMode(GL_RENDER))
            else:
                processright(glRenderMode(GL_RENDER))
            glPopMatrix();
            glMatrixMode(GL_MODELVIEW);           
 
            
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
                objeto=object(self.mem, objetos[1])
                if isinstance(objeto, Ficha):
                    self.mem.selFicha=objeto
                else:
                    self.mem.selFicha=None
                
                
        def processright(nameStack):
            """nameStack tiene la estructura minDepth, maxDepth, names"""
            def placePopUp():
                resultado=QPoint(event.x(), event.y())
                if event.x()>self.width()-a.width():
                    resultado.setX(event.x()-a.width())
                if event.y()>self.height()-a.height():
                    resultado.setY(event.y()-a.height())
                return resultado
            ############################333
            objetos=[]
            for minDepth, maxDepth, names in nameStack:
                if len(names)==1:
                   objetos.append(names[0])
            if len(objetos)==1:
                selCasilla=object(self.mem, objetos[0])
                print ("Es segura para el jugadoractual", selCasilla.esUnSeguroParaJugador(self.mem, self.mem.jugadoractual))
                if isinstance(selCasilla, Casilla):
                    a=frmShowCasilla(self,  Qt.Popup,  selCasilla)
                    a. move(self.mapToGlobal(placePopUp() ))
                    a.show()
            elif len(objetos)==2:
                selFicha=object(self.mem, objetos[1])
                if isinstance(selFicha, Ficha):
                    a=frmShowFicha(self, Qt.Popup,  selFicha)
                    a. move(self.mapToGlobal(placePopUp()))
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
        if self.height()>700:
            dadowidth=40
        else:
            dadowidth=20
        xl=self.width()/6+6# xleft
        xr=self.width()*5/6-43
        yt=self.height()/6+3#ytop
        yb=self.height()*5/6-43
        if self.mem.jugadoractual.color.name=="yellow":
            self.dado.setGeometry( xl, yt, dadowidth, dadowidth )
        elif self.mem.jugadoractual.color.name=="blue":
            self.dado.setGeometry(xl, yb, dadowidth, dadowidth)
        elif self.mem.jugadoractual.color.name=="red":
            self.dado.setGeometry(xr, yb, dadowidth, dadowidth)
        elif self.mem.jugadoractual.color.name=="green":
            self.dado.setGeometry(xr, yt, dadowidth, dadowidth)
        self.dado.setPixmap(self.mem.dado.qpixmap(self.mem.jugadoractual.tiradaturno.ultimoValor()))
        self.dado.repaint()
        self.dado.update()
        self.updateGL()
        self.dado.show()


