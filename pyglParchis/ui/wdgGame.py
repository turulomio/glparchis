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
        self.max_fichas=self.defineMaxFichas(id)
        self.color=self.defineColor(id)
        self.position=datos.posCasillas[id]
        self.rotate=self.defineRotate(id)
        self.tipo=self.defineTipo(id)
        self.busy=[False]*self.max_fichas
        self.seguro=self.defineSeguro(id)
#        print self.busy

    def defineSeguro(self,  id):
        if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
            return True
        else:
            return False

    def defineMaxFichas(self,  id):
        if id==101 or id==102 or id==103 or id==104 or id==76 or id==84 or id==92 or id==100:
            return 4
        else:
            return 2

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
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.casilla[self.id]);
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

        GL.glPopName();
        GL.glPopMatrix()

    def tipo_normal(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.casilla[self.id]);
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
        GL.glPopName();
        GL.glPopMatrix()

    def tipo_oblicuoi(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.casilla[self.id]);
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

        GL.glPopName();
        GL.glPopMatrix()

    def tipo_oblicuod(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.casilla[self.id]);
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

        GL.glPopName();
        GL.glPopMatrix()
        
    def tipo_final(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.casilla[self.id]);
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

        GL.glPopName();
        GL.glPopMatrix()

    def position_free(self):
        """Función que busca el libro pero no lo modifica"""
        for i in range(len(self.busy)):
            if self.busy[i]==False:
                return i
        return None
        
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


class wdgGame(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.tablero=Tablero()
        self.rotX=0
        self.lastPos = QPoint()
        self.casillas=[]
        self.fichas=[]
        #
        self.pendiente=2 #0 de nada,  2 de tirar dado, 6 por seis, 10 de mover ficha por metida, 20 de mover ficha por comida
#        self.newLog= pySignal(QString)  
    
        self.dado=0; # aquí debera llegar el movimiento del dado y las comidas y metidas
        self.historicodado=[]
        self.movimientos_acumulados=[]#Comidas ymetidas
        self.selLastFicha=None #Se utiliza cuando se va a casa
        self.selFicha=None
        self.selCasilla=None
        self.jugadoractual=3
        for i in range(0, 105):#Se debe inializar Antes que las fichas
            self.casillas.append(Casilla(i)) #La casilla 0 no se usa pero se crea para que todo sea más intuitivo.
        for i in range(0, 16):
            self.fichas.append(Ficha(i))
            self.mover(i, 0)# Paraz aque todo funcione debe iniciarse así.
        self.trolltechGreen = QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)


    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.dark())
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)
        
        GL.glFrontFace(GL.GL_CCW);

        light_ambient =  (0.3, 0.3, 0.3, 0.1);
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

    def log(self, cadena):
            self.emit(SIGNAL("newLog(QString)"),str(cadena))

    def paintGL(self):   
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(-31.5, -31.5,  -60)
        GL.glRotated(self.rotX, 1,0 , 0)
        self.tablero.dibujar()
        for c in self.casillas:
            c.dibujar()
        for f in self.fichas:
            f.dibujar()

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
                self.emit(SIGNAL("newLog(QString)"),"selCasilla:" + str(self.selCasilla )+ ". Busy:" +  str(self.casillas[self.selCasilla].busy))
                self.selFicha=None
            elif len(objetos)==2:
                self.selLastFicha=self.selFicha
                self.selCasilla=object(objetos[0])
                self.selFicha=object(objetos[1])
                self.emit(SIGNAL("newLog(QString)"),"selFicha:" +str(self.selFicha))
            
        self.setFocus()
        if event.buttons() & Qt.LeftButton:
            pickup(event)                
            if self.selFicha:
                self.after_ficha_click()
        self.updateGL()

    def puede_comer(self, id_ficha,  ruta):
        """No modifica nada"""
        def hay_ficha_otro_jugador(id_casilla):
            for f in self.fichas:
                if f.casilla()==id_casilla and f.jugador!=self.jugadoractual:
                    return (True, f.id)
            return (False, None)

        idcasilladestino=datos.ruta[ruta][self.fichas[id_ficha].jugador]
        r=hay_ficha_otro_jugador(idcasilladestino)
        if r==(False, None):
            return (False, None)
            
        if self.casillas[idcasilladestino].seguro==True:
            return (False, None)
            
        return r

    def puede_jugar(self, commit):
        """Lo relacionado con el movimiento del dado y movimientos especiales commit igual a -True lo gasta, con False solo busca"""
        def jugador_tiene_alguna_ficha_en_casa():
            for f in self.fichas:
                if f.jugador==self.jugadoractual:
                    if f.ruta==0:
                        return True
            return False
            
        salio=0
        if len(self.movimientos_acumulados)==0:
            if self.dado==0:
                return (False, 0)
            else:
                salio=self.dado
            
            if salio==6 and len(self.historicodado)==3:
                self.mover(self.selLastFicha, 0)
                self.log(tr("Han salido 3 seises te vas a casa"))
                self.emit(SIGNAL("cambiar_jugador()"))
                return (False, 0)

            if commit==True:
                if salio==6 and jugador_tiene_alguna_ficha_en_casa()==False:
                    salio=7
                    self.log("Salio un 6 pero mueves 7")
                    self.pendiente=2
                if self.fichas[self.selFicha].ruta==0:
                    if salio==5:
                        salio=1   
                        self.log("Sales de casa con un 5")
                    else:
                       return (False, 0)
                self.pendiente=0
                self.dado=0
                return (True, salio)
            else:               
                if salio==6 and jugador_tiene_alguna_ficha_en_casa()==False:
                    salio=7
                if self.fichas[self.selFicha].ruta==0:
                    if salio==5:
                        salio=1
                    else:
                       return (False, 0)
                return (True, salio)
        else:
            salio=movimientos_acumulados[0]
            if commit==True:
                del movimientos_acumulados[0]
            return (True, salio)

    def after_ficha_click(self):
        if  self.fichas[self.selFicha].jugador!=self.jugadoractual:             
            self.log("No es el jugador actual")
            return
            
        if self.pendiente==2:
            self.log("Debe tirar el dado")
            return
        pj=self.puede_jugar(False)
#        self.log(str(pj))

        if pj[0]==False:
            self.log("Ya no puede seguir jugando")
            self.emit(SIGNAL("cambiar_jugador()"))
            return
#        self.log("Puede usar " + str(pj[1]))
        
        if self.fichas[self.selFicha].ruta+ pj[1]>72:
            self.log("Se ha pasado")
            return 
            
        idcasilladestino=datos.ruta[self.fichas[self.selFicha].ruta+pj[1]][self.fichas[self.selFicha].jugador]
        posicioncasilladestino=self.casillas[idcasilladestino].position_free()
#        self.log(str(idcasilladestino) +" " + str( posicioncasilladestino))
        if posicioncasilladestino==None:
            self.log("No hay casilla destino libre")
            return             
            
        pc=self.puede_comer(self.selFicha, self.fichas[self.selFicha].ruta+pj[1])
        if pc[0]==True:
            pj=self.puede_jugar(True)
#            self.log("Va a comer y usar " + str(pj[1]))
            self.pendiente=20
            self.mover(pc[1], 0)

        pj=self.puede_jugar(True)
#        self.log(str(pj))
#        self.log(self.fichas[self.selFicha].ruta+  pj[1]+  self.fichas[self.selFicha].ruta+pj[1])
#        self.log("Va a usar " + str(pj[1]))
        self.mover(self.selFicha,self.fichas[self.selFicha].ruta+pj[1])            

        ##CHEQUEOS UNA VEZ MOVIDO
        if self.pendiente==0:
            self.emit(SIGNAL("cambiar_jugador()"))
        elif self.pendiente==2:#tirardado
                self.emit(SIGNAL("volver_a_tirar()"))
        elif self.pendiente==6:
            self.log("Debe tirar por haber salido un 6")
        elif self.pendiente==10:
            self.log("Debe mover 10")
        elif self.pendiente==20:
            self.log("Debe mover 20")
            


    def mover(self, id_ficha,  ruta):
        """Solo mueve, la logica en after_ficha_click"""
        idcasillaorigen=self.fichas[id_ficha].casilla()
        idcasilladestino=datos.ruta[ruta][self.fichas[id_ficha].jugador]
        if ruta==72:
            self.pendiente=10
        posicioncasillaorigen=self.fichas[id_ficha].numposicion
        posicioncasilladestino=self.casillas[idcasilladestino].position_free()
        self.fichas[id_ficha].last_ruta=self.fichas[id_ficha].ruta
        self.fichas[id_ficha].ruta=ruta#cambia la ruta
        self.fichas[id_ficha].numposicion=posicioncasilladestino
        if posicioncasillaorigen!=None: #Al iniciar no hay
            self.casillas[idcasillaorigen].busy[posicioncasillaorigen]=False#libera la posicion en la casilla
#        self.log("Ficha " +str (id_ficha)+" movido a casilla " + str(idcasilladestino) + " a la posicion " + str(posicioncasilladestino))
        self.casillas[idcasilladestino].busy[posicioncasilladestino]=True#okupa la posicion en la casilla
        return True
        
#    def wheelEvent(self, event):
#        if event.delta() > 0:
#            self.mover(self.selFicha, 1)
#        else:
#            self.mover(self.selFicha, 2)
#        self.updateGL()

class Ficha(QGLWidget):
    def __init__(self, id,  parent=None):
        QGLWidget.__init__(self, parent)
        self.id=id
        self.ruta=0
        self.last_ruta=0
        self.color=self.defineColor(id)
#        print "Aquí"
        self.ficha=GLU.gluNewQuadric();
#        print "Aquí"
        self.jugador=int(id/4)
        self.numposicion=None#Posicion dentro de la casilla
        print QCoreApplication.translate("wdgGame","Ejemplo de translacion")
#        self.numposicion=datos.numFichas[self.casilla()]-1#Posicion dentro de la casilla
#        datos.numFichas[self.casilla()]=datos.numFichas[self.casilla()]+1
#        print "Casilla",  self.casilla()
#        print "Jugador",  self.jugador
#        print "Numfichas", datos.numFichas[self.casilla()]
    def casilla(self):
        return datos.ruta[self.ruta][self.jugador]
        
    def posicion(self):
        return datos.posFichas[self.casilla()][self.numposicion]

    def defineColor(self,  id):
        if id>=0 and id<=3:
           return QColor(255, 255, 0)        
        elif id>=4 and id<=7:
           return QColor(0, 0, 255)
        elif id>=8 and id<=11:
           return QColor(255, 0, 0 )
        elif id>=12 and id<=15:
           return QColor(0, 255, 0)


    def dibujar(self):
        GL.glInitNames();
        GL.glPushMatrix()
        GL.glPushName(datos.Name.ficha[self.id]);
        p=self.posicion()
        GL.glTranslated(p[0], p[1], p[2])
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        self.qglColor(QColor(255, 255, 0).dark())
        GLU.gluQuadricDrawStyle (self.ficha, GLU.GLU_FILL);
        GLU.gluQuadricNormals (self.ficha, GLU.GLU_SMOOTH);
        GLU.gluQuadricTexture (self.ficha, True);
        self.qglColor(self.color.dark())
        GLU.gluCylinder (self.ficha, 1.4, 1.4, 0.5, 16, 5)
        GL.glTranslated(0, 0, 0.5)
        self.qglColor(QColor(70, 70, 70))
        GLU.gluDisk(self.ficha, 0, 1.4, 16, 5)
        self.qglColor(self.color.dark())
        GL.glTranslated(0, 0, -0.5)
        GL.glRotated(180, 1, 0, 0)# da la vuelta a la cara
        GLU.gluDisk(self.ficha, 0, 1.40, 16, 5)
        GL.glPopName();
        GL.glPopMatrix()


class Tablero(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.position=(-1, -1, 0)

    def quad(self, p1, p2, p3, p4, color):
        self.qglColor(color)
        GL.glVertex3d(p1[0], p1[1], p1[2])
        GL.glVertex3d(p2[0], p2[1], p2[2])
        GL.glVertex3d(p3[0], p3[1], p3[2])
        GL.glVertex3d(p4[0], p4[1], p4[2])

    def dibujar(self):
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
