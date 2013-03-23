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
        self.mem=mem
        
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
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/transwood.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/seguro.png')))
        self.texDecor.append(self.bindTexture(QtGui.QPixmap(':/glparchis/dado_desplegado.png')))
        
        print ("initializeGL")
        glEnable(GL_TEXTURE_2D);
        glShadeModel (GL_SMOOTH);
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
        
        #Antialiasing
#        glEnable (GL_LINE_SMOOTH);
#        glEnable (GL_POINT_SMOOTH);
#        glEnable (GL_POLYGON_SMOOTH);
#        glHint (GL_LINE_SMOOTH_HINT, GL_NICEST);
#        glLineWidth (1.5)

    def paintGL(self):   
        glLoadIdentity()
        self.qglClearColor(QColor())

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.mem.maxplayers==8:
            glTranslated(-31.5, -17,  -85)
        elif self.mem.maxplayers==4:
            glTranslated(-31.5, -31.5,  -60)
        elif self.mem.maxplayers==6:
            glTranslated(-31.5, -24,  -80)
            
        glRotated(self.rotX, 1,0 , 0)
        if self.mem.maxplayers==4:
            self.tablero.dibujar(self)
        for c in self.mem.casillas.arr:
            c.dibujar(self)
            c.dibujar_fichas(self)
        self.mem.dado.dibujar(self)

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect=width/height
        gluPerspective(60.0, aspect, 1, 400)
        glMatrixMode(GL_MODELVIEW)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M: # toggle mode
            if self.visualizacion==0:
                self.rotX=0
            elif self.visualizacion==1:
                self.rotX=340
            elif self.visualizacion==2:
                self.rotX=275
            self.updateGL()
            
            if self.visualizacion==2:
                self.visualizacion=0
            else:
                self.visualizacion=self.visualizacion+1
    
    def mouseDoubleClickEvent(self, event):
        self.emit(SIGNAL("doubleClicked()"))
                
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
                return self.tablero
            elif id_name==17:#casillas de 17 a 121
                return mem.dado
            elif id_name>=18 and id_name<=18+self.mem.casillas.number:#casillas de 17 a 121
                return mem.casillas.casilla(id_name-18)
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
                fichas=self.mem.jugadores.actual.fichas.fichasAutorizadasAMover(self.mem)
                fichas=sorted(fichas, key=lambda f:f.numeroAmenazasMejora(self.mem),  reverse=True)     
                for f in fichas:
                    print (f, f.numeroAmenazasMejora(self.mem), f.numFichasPuedenComer(self.mem, f.posruta), f.numFichasPuedenComer(self.mem, f.posruta+f.estaAutorizadaAMover(self.mem)[1]))

                if isinstance(selCasilla, Casilla):
                    a=frmShowCasilla(self,  Qt.Popup,  selCasilla)
                    a. move(self.mapToGlobal(placePopUp() ))
                    a.show()
            elif len(objetos)==2:
                selFicha=object(self.mem, objetos[1])
                if isinstance(selFicha, Ficha):
                    a=frmShowFicha(self,  Qt.Popup,  selFicha, self.mem)
                    a. move(self.mapToGlobal(placePopUp()))
                    a.show()
                
        #########################################
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event, False)            
            if self.mem.selFicha!=None:
                self.mem.jugadores.actual.log(self.trUtf8("Se ha hecho click en la ficha %1").arg(self.mem.selFicha.id))
                self.emit(SIGNAL("fichaClicked()"))#No se pasa parámetro porque es self.mem.selFicha
        elif event.buttons() & Qt.RightButton:
            pickup(event, True)                    
        self.updateGL()

