#-*- coding: utf-8 -*- 
from OpenGL.GL import *
from OpenGL.GLU import *
import os,  random,   ConfigParser,  datetime,  time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import *
from PyQt4.phonon import Phonon
version="20120921+"
def q2s(q):
    """Qstring to python string en utf8"""
    return str(QString.toUtf8(q))
    
def s2q(st):
    """utf8 python string to qstring"""
    if st==None:
        return QString("")
    else:
        return QString(st.decode("UTF8"))

def i2b(integer):
    """Convierte 1 en Truue 0 en False"""
    if integer==1:
        return True
    elif integer==0:
        return False
        
def c2b(state):
    """QCheckstate to python bool"""
    if state==Qt.Checked:
        return True
    else:
        return False

def delay(miliseconds):
    dieTime= datetime.datetime.now()+datetime.timedelta(microseconds=miliseconds*1000)
    while datetime.datetime.now()< dieTime :
        QCoreApplication.processEvents(QEventLoop.AllEvents, 100);    


class Dado(QObject):    
    def __init__(self, parent=None ):
        QGLWidget.__init__(self, parent)
        self.fake=[]
        self.showing=False
        self.position=(65/2, 65/2, 1)
        self.oglname=122
        self.lasttirada=None
        
    def tirar(self):
        random.seed(datetime.datetime.now().microsecond)
        if len(self.fake)>0:
            resultado=self.fake[0]
            self.fake.remove(self.fake[0])
        else:
            resultado= int(random.random()*6)+1
        self.lasttirada=resultado
        return resultado
        
    def dibujar(self, ogl, alone=False):
        """Cuando se dibuja alone, no tiene en cuenta los jugadores es para showobject"""
        if self.showing==False:
            return
        glInitNames();
        glPushName(self.oglname);
        glPushMatrix();
        if alone==False:
            if ogl.mem.jugadoractual==ogl.mem.jugadores.jugador("yellow"):
                self.position=(10, 51, 1)
            elif ogl.mem.jugadoractual==ogl.mem.jugadores.jugador("blue"):
                self.position=(9, 10, 1)
            elif ogl.mem.jugadoractual==ogl.mem.jugadores.jugador("red"):
                self.position=(50, 10, 1)
            elif ogl.mem.jugadoractual==ogl.mem.jugadores.jugador("green"):
                self.position=(50, 51, 1)
            glTranslatef(self.position[0],self.position[1],self.position[2]);
        if self.lasttirada==1:
            glTranslated(0, 0, 3)
            glRotated(-90.0,1.0,0.0,0.0);
        if (self.lasttirada==3):
            glTranslated(3, 0, 3)
            glRotated(180.0,0.0,1.0,0.0);
        if (self.lasttirada==4):
            glTranslated(0, 3, 0)
            glRotated(90.0,1.0,0.0,0.0);
       
        if (self.lasttirada==5):
            glTranslated(3, 3, 0)
            glRotated(90.0,1.0,0.0,0.0);
            glRotated(90.0,0.0,0.0,1.0);
        if (self.lasttirada==6):
            glTranslated(0, 0, 3)
            glRotated(90.0,0.0,1.0,0.0);
        glScaled(3,3,3);
        glColor3d(255, 255, 255);

        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[3]);
        unter=1.0/3.0;
        doster=2.0/3.0;
        glBegin(GL_QUADS);
        v0=  (0.0, 0.0, 0.0) 
        v1=( 1.0, 0.0, 0.0) 
        v2=( 1.0, 0.0, 1.0) 
        v3=  (0.0, 0.0, 1.0) 

        v4=(0.0, 0.0, 1.0)
        v5=( 1.0, 0.0, 1.0)
        v6=( 1.0, 1.0, 1.0)
        v7=(0.0, 1.0, 1.0)

        v8=(0.0, 0.0, 0.0)
        v9=(0.0, 1.0, 0.0)
        v10=( 1.0, 1.0, 0.0)
        v11=( 1.0, 0.0, 0.0) 

        v12=(0.0, 1.0, 0.0) 
        v13=(0.0, 1.0, 1.0) 
        v14=( 1.0, 1.0, 1.0) 
        v15=( 1.0, 1.0, 0.0) 

        v16=( 1.0, 0.0, 0.0) 
        v17=( 1.0, 1.0, 0.0) 
        v18=( 1.0, 1.0, 1.0) 
        v19=( 1.0, 0.0, 1.0) 

        v20=(0.0, 0.0, 1.0) 
        v21=(0.0, 1.0, 1.0) 
        v22=(0.0, 1.0, 0.0)
        v23=(0.0, 0.0, 0.0)
        glTexCoord2f(0.0, unter);glVertex3fv(v0)
        glTexCoord2f(0.25, unter);glVertex3fv(v1)
        glTexCoord2f(0.25, doster);glVertex3fv(v2)
        glTexCoord2f(0.0, doster);glVertex3fv(v3)  
        glTexCoord2f(0.25, doster);glVertex3fv(v4)
        glTexCoord2f(0.5, doster);glVertex3fv(v5)
        glTexCoord2f(0.5, 1.0);glVertex3fv(v6)
        glTexCoord2f(0.25, 1.0);glVertex3fv(v7)  
        glTexCoord2f(0.25, doster);glVertex3fv(v8)
        glTexCoord2f(0.5, doster);glVertex3fv(v9)
        glTexCoord2f(0.5, unter);glVertex3fv(v10)
        glTexCoord2f(0.25, unter);glVertex3fv(v11)  
        glTexCoord2f(0.25, 0.0);glVertex3fv(v12)
        glTexCoord2f(0.5, 0.0);glVertex3fv(v13)
        glTexCoord2f(0.5, unter);glVertex3fv(v14)
        glTexCoord2f(0.25, unter);glVertex3fv(v15)  
        glTexCoord2f(0.5, unter);glVertex3fv(v16)
        glTexCoord2f(0.75, unter);glVertex3fv(v17)
        glTexCoord2f(0.75, doster);glVertex3fv(v18)
        glTexCoord2f(0.5, doster);glVertex3fv(v19) 
        glTexCoord2f(0.75, unter);glVertex3fv(v20)
        glTexCoord2f(1.0, unter);glVertex3fv(v21)
        glTexCoord2f(1.0, doster);glVertex3fv(v22)
        glTexCoord2f(0.75, doster);glVertex3fv(v23)
        glEnd();
        glPopName();
        glPopMatrix();

        glDisable(GL_TEXTURE_2D);
        
    def qicon(self, numero):
            ico = QIcon()
            ico.addPixmap(self.qpixmap(numero), QIcon.Normal, QIcon.Off) 
            return ico
            
    def qpixmap(self, numero):
        """Devulve un QPixmap segun el valor del numero 0-6"""
        if numero==1:
            pix=QPixmap(":/glparchis/cube1.png")
        elif numero==2:
            pix=QPixmap(":/glparchis/cube2.png")
        elif numero==3:
            pix=QPixmap(":/glparchis/cube3.png")
        elif numero==4:
            pix=QPixmap(":/glparchis/cube4.png")
        elif numero==5:
            pix=QPixmap(":/glparchis/cube5.png")
        elif numero==6:
            pix=QPixmap(":/glparchis/cube6.png")
        elif numero==None:              
            pix=QPixmap(":/glparchis/cube.png")
        return pix
                    
        
class TiradaHistorica:
    """Estudio estadistico de tiradas. Lleva un array con todas los objetos TiradaTurno por cada jugador
    Se graba cuando se tira ya que es un objeto TiradaTurno que se vincula en el array de TiradaHistorica"""
    def __init__(self):
        self.arr=[]
    
    def numThrows(self):
        """Gets the number of total and historic player throws"""
        resultado=0
        for tt in self.arr:
            resultado=resultado+tt.numThrows()
        return resultado
        
    def numTimesDiceGetNumber(self, number):
        """Gets the number of times that the dice gets the number"""
        resultado=0
        for tt in self.arr:
            for t in tt.arr:
                if t.valor==number:
                    resultado=resultado+1
        return resultado
        
    def numThreeSixes(self):
        """Gets the number of times that the dice get three sixes"""
        resultado=0
        for tt in self.arr:
            if tt.tresSeises()==True:
                resultado=resultado+1
        return resultado
                
class TiradaJuego:
    """Estudio estadistico de tiradas globales del juego (une todos jugadores). Se usa para temas estadisticos y recorre las tiradas
    historicas de todos los jugadores."""
    def __init__(self, mem):
        self.mem=mem
    
    def numThrows(self):
        """Gets the number of total and historic player throws"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numThrows()
        return resultado
        
    def numTimesDiceGetNumber(self, number):
        """Gets the number of times that the dice gets the number"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numTimesDiceGetNumber(number)
        return resultado
        
    def numThreeSixes(self):
        """Gets the number of times that the dice get three sixes"""
        resultado=0
        for j in self.mem.jugadores.arr:
            resultado=resultado+j.tiradahistorica.numThreeSixes()
        return resultado
        
class Tirada:
    """Lanzamiento individual de un dado"""
    def __init__(self, jugador, valor,  tipo=None):
        self.jugador=jugador
        self.valor=valor
        self.tipo=tipo#None desconocido 1 turno normal, dos por seis, tres por comer, cuatro por meter

class TiradaTurno:
    """Objeto que recoge todos las tiradas de un turno"""
    def __init__(self):
        self.jugador=None
        self.arr=[]
        
    def tresSeises(self):
        """Función que devuelve un booleano según haya o no salido 3 seises"""
        if len(self.arr)==3:
            if self.arr[0].valor==6 and self.arr[1].valor==6 and self.arr[2].valor==6:
                return True
        return False
        
    def ultimoEsSeis(self):
        if len (self.arr)>0:
            if self.arr[len(self.arr)-1].valor==6:
                return True
        return False
        
    def ultimoValor(self):
        if len(self.arr)>0:
            return self.arr[len(self.arr)-1].valor
        else:
            return None
            
    def numThrows(self):
        """Gets the number of throws in the turn"""
        return len (self.arr)

class Jugador:
    def __init__(self,  color):
        self.name=None#Es el nombre de usuario no el de color
        self.color=color
        self.ia=False
        self.plays=True
        self.fichas=SetFichas()     
        self.tiradaturno=TiradaTurno()#TiradaJugador()
        self.tiradahistorica=TiradaHistorica()
        self.LastFichaMovida=None #Se utiliza cuando se va a casa NOne si ninguna
        self.movimientos_acumulados=None#Comidas ymetidas, puede ser 10, 20 o None Cuando se cuenta se borra a None
        self.dado=None #Enlace a objeto dado de mem
        self.logturno=[]#log de turno
        self.loghistorico=[]
        self.comidaspormi=0
        self.comidasporotro=0

    def __repr__(self):
        return "Jugador {0}".format(self.color.name)

    def log(self, l):
        l=u"{0} {1}".format(str(datetime.datetime.now().time()).split(".")[0], l)
        self.logturno.append( l)
        self.loghistorico.append(l)
        
    def casillasPorMover(self):
        """Casillas que le queda al jugador hasta ganar la partida"""
        resultado =0
        for f in self.fichas.arr:
            resultado=resultado+f.casillasPorMover()
        return resultado
            
    def casillasMovidas(self):
        """Casillas que ha movido el jugador, puede considerarse la puntuación del jugador"""
        return 4*72-self.casillasPorMover()
            
        
    def hayDosJugadoresDistintosEnRuta1(self):
        ruta1=self.fichas.arr[0].ruta.arr[1]
        if ruta1.id not in (5, 22, 39, 56):#Casillas ruta1
            return False
        if ruta1.buzon_numfichas()!=2:
            return False
        if ruta1.buzon[0].jugador!=ruta1.buzon[1].jugador:
            return True
        return False
        
        
    def tirarDado(self):
        """Tira el dado lo almacena en tirada, tiradaturno e historico y devuelve el valor"""
        tirada=Tirada(self, self.dado.tirar())
        self.tiradaturno.arr.append(tirada)
        if self.tiradaturno not in self.tiradahistorica.arr:
            self.tiradahistorica.arr.append(self.tiradaturno)
        return tirada.valor

        
    def barreras(self):
        """Devuelve una lista con las casillas en las que el jugador tiene barrera"""
        resultado=[]
        for f in self.fichas.arr:
            if f.casilla().tieneBarrera()==True:
                resultado.append(f.casilla())
        return resultado
        
    def tieneBarreras(self):
        if len(self.barreras())>0:
            return True
        return False

    def tieneFichasEnCasa(self):
        for f in self.fichas.arr:
            if f.estaEnCasa()==True:
                return True
        return False
        
    def tieneFichasEnRampaLlegada(self):
        """Devuelve un booleano si el jugador tiene fichas en la rampa de llegada"""
        for f in self.fichas.arr:
            if f.casilla().rampallegada==True:
                return True
        return False
        

    def HaGanado(self):
        for f in self.fichas.arr:
            if f.estaEnMeta()==False:
                return False
        return True
        
    def IASelectFicha(self, mem):
        """Función que devuelve la ficha seleccionada por la IA. Si devuelve None es que ninguna se puede mover"""
        def azar(tope):
            """Función que saca un numero al azar de entre 1 y 100. Si es mayor del tope devuelve true. Sino devuelve false. Es decir tope 85 es una probabilidad del 85%"""
            random.seed(datetime.datetime.now().microsecond)
            numero=int(random.random()*100)
            if numero<tope:
                return True
            return False
        ####################################
        fichas=self.fichas.fichasAutorizadasAMover(mem)
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)     
        if len(fichas)==0:
            return None
        
        # Hay porcentajes de acierto si falla pasa a la siguiente prioridad
        #1 prioridad. Puede comer IA 85%
        if azar(90):
            for f in fichas:#Recorre las que pueden mover
                movimiento=f.estaAutorizadaAMover(mem)[1]
                (puede, fichaacomer)=f.puedeComer(mem, f.posruta+movimiento)
                if puede:
                    print (f, "seleccionada por azar comer")
                    return f
        
        #2 prioridad. Mueve fichas que disminuyen en número de amenazas en la nueva posicion
        fichas=sorted(fichas, key=lambda f:f.numeroAmenazasMejora(mem),  reverse=True)     
        if azar(95):
            for f in fichas:
                if f.numeroAmenazasMejora(mem)>0 and  f.numFichasPuedenComer(mem, f.posruta)>0: #Debe estar amenazada
                    print (f, "seleccionada por azar al mejorar numero de fichas la pueden comer")
                    return f
        
        
        #3 prioridad Asegura IA  de ultima a primera 85%
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)     
        if azar(80):
            for f in fichas:
                movimiento=f.estaAutorizadaAMover(mem)[1]
                if f.casilla().esUnSeguroParaJugador(mem, self)==False  and  f.casilla(f.posruta+movimiento).seguro==True:
                    print (f,"seleccionado por azar asegurar")
                    return f
        
        #4 Alguna ficha no asegurada puede mover
        if azar(95):
            for f in fichas:
                if f.casilla().esUnSeguroParaJugador(mem, f.jugador)==False:
                    print(f,"seleccionado por azar ficha no asegurada")
                    return f
        
        #5 prioridad Mueve la ultima IA 100%
        fichas=sorted(fichas, key=lambda f:f.posruta,  reverse=True)
        print (fichas[0], "Sin azar. Ultima ficha")
        return fichas[0]
            
    def qicon(self):
        ico = QIcon()
        ico.addPixmap(self.qpixmap(), QIcon.Normal, QIcon.Off) 
        return ico
    
    def qpixmap(self):
        """Devuelve un pixmap del color de la ficha"""
        if self.color.name=="yellow":
            return QPixmap(":/glparchis/fichaamarilla.png")
        elif self.color.name=="blue":
            return QPixmap(":/glparchis/fichaazul.png")
        elif self.color.name=="green":
            return QPixmap(":/glparchis/fichaverde.png")
        elif self.color.name=="red":
            return QPixmap(":/glparchis/ficharoja.png")
class Ruta:
    def __init__(self):
        self.arr=[] #Array ordenado
    
    
class SetJugadores:
    """Agrupación de jugadores"""
    def __init__(self):
        self.arr=[]
        
    def vaGanando(self):
        """Devuelve el objeto del jugador que va ganando"""
        resultado=self.arr[0]#Selecciona primer jugador
        maxpunt=resultado.casillasMovidas()
        for j in self.arr:
            if j.casillasMovidas()>maxpunt:
                maxpunt=j.casillasMovidas()
                resultado=j
        return resultado
        
    def jugador(self, colorname):
        for j in self.arr:
            if j.color.name==colorname:
                return j
        return None
        
class SetCasillas:
    """Conjunto de casillas"""
    def __init__(self):
        pass
        
    def rutas1(self):
        pass
        
class SetFichas:
    """Agrupación de fichas"""
    def __init__(self):
        self.arr=[]

    def algunaEstaObligada(self, mem):
        """Busca entre las fichas que pueden mover si alguna está obligada a mover"""
        for f in self.arr:
            if f.estaObligada(mem)==True:
                return True
        return False

    def algunaEstaAutorizadaAmover(self, mem):
        if len(self.fichasAutorizadasAMover(mem))>0:
            return True
        return False
        
    def fichasAutorizadasAMover(self, mem):
        """Devuelve un arr con las fichas que pueden mover"""
        resultado=[]
        for f in self.arr:
            if f.estaAutorizadaAMover(mem)[0]==True:
                resultado.append(f)
        return resultado        
    
    def TodasFichasEnCasa(self):
        for f in self.arr:
            if f.posruta!=0:
                return False
        return True        
        
    def TodasFichasFueraDeCasa(self):
        for f in self.arr:
            if f.posruta==0:
                return False
        return True
        
class Ficha(QObject):
    def __init__(self, id, number,  color, jugador, ruta):
        """El identificador de la ficha viene dado por el nombre del color y el id (numero de creacion), se genera en la clase Mem"""
        QGLWidget.__init__(self)
        self.color=color
        self.id=id
        self.number=number#indice dentro de las fichas de mismo color.
        self.ruta=ruta
        self.posruta=0#pOSICION EN LA RUTA
        self.ficha=gluNewQuadric();
        self.jugador=jugador
        self.oglname=self.id#Nombre usado para pick por opengl
        
    def __repr__(self):
        return  "Ficha {0} del jugador {1}".format(self.id, self.jugador.color.name)
        
    def estaObligada(self, mem):        
        """ESta pregunta se integra dentro de puede mover. NO DEBE HABER EN SETFICHAS ALGUNAS, YA QUE SE INTEGRARíA DENTRO DE ALGUNA PUEDEMOVER"""
        if self.puedeMover(mem)[0]==False:
            return False
            
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.ruta.arr[1].buzon_numfichas()<2:
            return True
        
        #dos jugadore distintos en inicio entonces come
        if self.jugador.tiradaturno.ultimoValor()==5 and self.estaEnCasa() and self.jugador.hayDosJugadoresDistintosEnRuta1():
            return True
        
        #Comprueba que no tenga obligación de abrir barrera
        if self.jugador.tieneBarreras()==True  and self.jugador.tiradaturno.ultimoValor()==6:
            if self.casilla() in self.jugador.barreras():
                return True
        return False
        
    def estaAutorizadaAMover(self, mem, log=False):
        """PUEDE MOVER Y ESTA OBLIGADO SON DOS CONCEPTOS INDEPENDIENTES QUE NO DEBEN DE UNIRSE 
        PORQUE GENERA RECURSIVIDADPOR ESO SE HACE AQUí
        
        Autorizada significa que puede mover y no está obligada a hacer otras cosas"""
        
        (puede, movimiento)=self.puedeMover(mem, log)
        if puede:
            if mem.jugadoractual.fichas.algunaEstaObligada(mem) :
                if self.estaObligada(mem)==False:
                    if log: mem.jugadoractual.log(self.trUtf8("No puede mover, porque hay otra ficha obligada a mover"))
                    return (False, 0)                    
            return (puede, movimiento)
        return (puede, movimiento)
        
    def puedeMover(self, mem,  log=False):
        """Comprueba si la ficha puede mover. desde el punto de vista fisico
        Si log=True muestra los logs"""

        #Es ficha del jugador actual. #A PARTIR DE AQUI SE PUEDE USAR SELF.JUGADOR EN VEZ DE MEM.JUGADORACTUAL
        if  self.jugador!=mem.jugadoractual:             
            if log: mem.jugadoractual.log(self.trUtf8("No es del jugador actual"))
            return (False, 0)
            
        #No se puede mover una ficha que está en casa con puntos acumulados
        if mem.jugadoractual.movimientos_acumulados!=None and self.estaEnCasa():
            return (False, 0)

        #Calcula el movimiento
        if mem.jugadoractual.movimientos_acumulados!=None:
            movimiento=mem.jugadoractual.movimientos_acumulados
        elif self.estaEnCasa() and self.jugador.tiradaturno.ultimoValor()==5:
            movimiento= 1
        elif self.estaEnCasa()==True and self.jugador.tiradaturno.ultimoValor()!=5: #Saco un 5
            movimiento=0
        elif self.jugador.fichas.TodasFichasFueraDeCasa()==True and self.jugador.tiradaturno.ultimoValor()==6:
            movimiento=7
        else:
            movimiento=self.jugador.tiradaturno.ultimoValor()
                            
        if movimiento==0 or movimiento==None:
            if log: mem.jugadoractual.log(self.trUtf8("No puede mover"))
            return (False, 0)    
           
        #se ha pasado la meta
        if self.posruta+movimiento>72:
            if log: mem.jugadoractual.log(self.trUtf8("Se ha pasado la meta"))
            return (False, 0) 
            
        #Rastrea todas las casillas de paso en busca de barrera. desde la siguiente
        for i in range(self.posruta+1, self.posruta+movimiento+1): 
            if self.ruta.arr[i].tieneBarrera()==True:
                if log: mem.jugadoractual.log(self.trUtf8("Hay una barrera"))
                return (False, 0)

        #Comprueba si hay sitio libre
        casilladestino=self.ruta.arr[self.posruta+movimiento]
        if casilladestino.posicionLibreEnBuzon()==-1:
            if self.jugador.hayDosJugadoresDistintosEnRuta1():#COmprueeba si es primera casilla en ruta y hay otra de otro color.
                if log: mem.jugadoractual.log(self.trUtf8("Obligado a sacar y a comer"))
            else:
                if log: mem.jugadoractual.log(self.trUtf8("No hay espacio en la casilla"))
                return (False, 0)
                

        return (True, movimiento)
        
    def mover(self, ruta, controllastficha=True,  startgame=False):
        casillaorigen=self.ruta.arr[self.posruta]
        casilladestino=self.ruta.arr[ruta]        
        self.posruta=ruta
        if controllastficha==True:
            self.jugador.LastFichaMovida=self
        if startgame==False:
            casillaorigen.buzon_remove(self)
        casilladestino.buzon_append(self)

    def puedeComer(self, mem, ruta):
        """Devuelve un (True, ficha a comer) or (False, None) si puede comer una ficha en la posición ruta"""
        casilladestino=self.casilla(ruta)
        fichasdestino=casilladestino.buzon_fichas()
        #debe estar primero porque es una casilla segura
        if self.posruta==0 and self.jugador.tiradaturno.ultimoValor()==5 and self.jugador.hayDosJugadoresDistintosEnRuta1():                
            if fichasdestino[0][1].jugador!=mem.jugadoractual:
                return(True, fichasdestino[0][1])
            else:# fichasdestino[1][1].jugador!=mem.jugadoractual:
                return(True, fichasdestino[1][1])
                
        if casilladestino.seguro==True:
            return (False, None)
        
        if len(fichasdestino)==1:#Todavia no se ha movido
            if fichasdestino[0][1].jugador!=mem.jugadoractual:
                return(True, fichasdestino[0][1])

        return (False, None)
                
                
    def come(self, mem,   ruta):
        """ruta, es la posición de ruta de ficha en la que come. No se ha movido antes, come si puede y devuelve True, en caso contrario False"""
        (puede, fichaacomer)=self.puedeComer(mem, ruta)
        if puede==True:
            fichaacomer.mover(0, False)
            if self.posruta==0:
                self.mover(1, True)
            else:
                self.mover(ruta, True)
            mem.jugadoractual.movimientos_acumulados=20
            mem.jugadoractual.log(self.trUtf8('He comido una ficha de %1 en la casilla %2').arg(fichaacomer.jugador.name).arg(self.casilla(ruta).id))
            self.jugador.comidaspormi=self.jugador.comidaspormi+1
            fichaacomer.jugador.comidasporotro=fichaacomer.jugador.comidasporotro+1
            return True
        return False

    def puedeMeter(self, posruta):
        """Devuelve un booleano si puede meter la ficha en las casilla final"""
        if posruta==72:
            return True
        return False
        
    def mete(self, posruta):
        """r Como ya se ha movido, mete si puede y devuelve True, en caso contrario False"""      
        if self.puedeMeter(posruta):
            self.mover(posruta, True)
            self.jugador.movimientos_acumulados=10
            self.jugador.log(self.trUtf8("He metido una ficha en casa"))
            return True
        return False

    def casilla(self,  posruta=None):
        """Devuelve el objeto casilla en el que se encuentra la ficha
        Si se le pasa el parametro devuelve la casilla de la ruta de la ficha, en la posicion posruta"""
        if posruta==None:
            posruta=self.posruta
        return self.ruta.arr[posruta]
            

    def casillasPorMover(self):
        return 72-self.posruta
        
    def numeroAmenazasMejora(self, mem):
        """Si devuelve un positivo es que ha disminuido en ese valor el numero de fichas que le amenzaban"""
        movimiento=self.estaAutorizadaAMover(mem)[1]
        antes=self.numFichasPuedenComer(mem, self.posruta)
        despues=self.numFichasPuedenComer(mem, self.posruta+movimiento)
#        print ("Amenazas en casilla {0}: {1}. En casilla {2}: {3}".format(self.casilla(self.posruta).id, antes, self.casilla(self.posruta+movimiento).id, despues))
        return antes-despues

    def numFichasPuedenComer(self, mem, posruta=None):
        """Función que devuelve un array con las fichas que pueden comer a la ficha actual si la colocara en posruta"""
        resultado=0
        if posruta==None:
            posruta=self.posruta
            
        if posruta<0 or posruta>72:
            return 0
            
        casilla=self.casilla(posruta)        #Datos casilla de posruta
        
        if casilla.esUnSeguroParaJugador(mem, self.jugador)==True or casilla.rampallegada==True:
            return 0
            
        if casilla.tieneBarrera():
            return 0
            
        if casilla not in mem.circulo.arr:#Si la casilla no esta en el circulo devuelve 0
            return 0
            
        #anota comer por cinco en ruta1    
        

        for pos, f in mem.circulo.casilla(casilla.id, -1).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -2).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -3).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -4).buzon_fichas():
            if f.jugador!=self.jugador:
                resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -5).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnCasa()==False:#debe sacar
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -6).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnCasa():
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -7).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnCasa()==False:
                    resultado=resultado+1
        for pos, f in mem.circulo.casilla(casilla.id, -10).buzon_fichas():
            if f.jugador!=self.jugador:
                if f.jugador.tieneFichasEnRampaLlegada():
                    resultado=resultado+1
        return resultado

    def estaEnCasa(self):
        if self.posruta==0:
            return True
        return False

    def estaEnMeta(self):
        if self.posruta==72:
            return True
        return False

    def dibujar(self, ogl,  posicionBuzon):
        glInitNames();
        glPushMatrix()
        glPushName(self.id);
        if posicionBuzon==None:#Para frmAcercade
            p=(0, 0, 0)
        else:
            p=self.ruta.arr[self.posruta].posfichas[posicionBuzon]
        glTranslated(p[0], p[1], p[2])
        glRotated(180, 1, 0, 0)# da la vuelta a la cara
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[1])
        ogl.qglColor(Color(255, 255, 0).qcolor())
        gluQuadricDrawStyle (self.ficha, GLU_FILL);
        gluQuadricNormals (self.ficha, GLU_SMOOTH);
        gluQuadricTexture (self.ficha, True);
        ogl.qglColor(self.color.qcolor())
        gluCylinder (self.ficha, 1.4, 1.4, 0.5, 16, 5)
        glTranslated(0, 0, 0.5)
        ogl.qglColor(Color(70, 70, 70).qcolor())
        gluDisk(self.ficha, 0, 1.4, 16, 5)
        ogl.qglColor(self.color.qcolor())
        glTranslated(0, 0, -0.5)
        glRotated(180, 1, 0, 0)# da la vuelta a la cara
        gluDisk(self.ficha, 0, 1.40, 16, 5)
        glPopName();
        glPopMatrix()
        glDisable(GL_TEXTURE_2D);


class Tablero(QObject):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.object = 1
        self.position=(-1, -1, 0)
        self.oglname=16#Nombre usado para pick por opengl


    def dibujar(self, ogl):
        def quad(p1, p2, p3, p4, color):
            ogl.qglColor(color.qcolor())
            glTexCoord2f(0.0,0.0)
            glVertex3d(p1[0], p1[1], p1[2])
            glTexCoord2f(1.0,0.0)
            glVertex3d(p2[0], p2[1], p2[2])
            glTexCoord2f(1.0,1.0)
            glVertex3d(p3[0], p3[1], p3[2])
            glTexCoord2f(0.0,1.0)
            glVertex3d(p4[0], p4[1], p4[2])              
        glPushMatrix()
        glEnable(GL_TEXTURE_2D);
        glBindTexture(GL_TEXTURE_2D, ogl.texDecor[1])
        glTranslated(self.position[0],  self.position[1],  self.position[2])
        glBegin(GL_QUADS)
        v1 = (0, 0, 0)
        v2 = (65, 0, 0)
        v3 = (65, 65, 0)
        v4 = (0, 65, 0)
        v5 = (0, 0, 0.5)
        v6 = (65, 0, 0.5)
        v7 = (65, 65, 0.5)
        v8 = (0, 65, 0.5)
        color=Color(255, 255, 255)
        quad(v4, v3, v2, v1, color)      
        color=Color(70, 70, 70)
        quad(v5, v6, v7, v8, color)   
        color=Color(255, 255, 255)   
        quad(v5, v8, v4, v1, color)      
        quad(v2, v3, v7, v6, color)      
        quad(v1, v2, v6, v5, color)      
        quad(v8, v7, v3, v4, color)          

        glEnd()
        glPopMatrix()
        glDisable(GL_TEXTURE_2D)
        
        
class Circulo:
    """Es el circulo publico por el que se mueven las fichas y pueden comerse entre ellas
    Es un array de casillas ordenado. que se repite ciclicamente
    numcasillas=68 para 4 jugadores"""
    def __init__(self, mem, numcasillas):
        self.arr=[]
        self.numcasillas=numcasillas
        for i in range(1, self.numcasillas+1):
            self.arr.append(mem.casillas(i))
    
    def casilla(self, posicion,  desplazamiento):
        """Calcula la casilla del circulo que tiene un desplazamiento positivo (hacia adelante) o negativo (hacia atrás) 
        de la casilla cuya posicion (id de la casilla) se ha dado como parametro"""
        if posicion<1 or posicion>self.numcasillas:   #Si no está en el circulo
            return None
            
        destino=posicion-1+desplazamiento
        if destino<0:
            destino=self.numcasillas+destino
        if destino>self.numcasillas-1:
            destino=destino-self.numcasillas
        return self.arr[destino]
        
class Color:
    def __init__(self,   r,  g, b, name=None):
        self.name=name
        self.r=r
        self.g=g
        self.b=b
    def glcolor(self):
        glColor3d(self.r, self.g, self.b)
        
    def qcolor(self):
        return QColor(self.r, self.g, self.b, 125)
        
class ConfigFile:
    def __init__(self, file):
        self.file=file
        self.splitterstate=None
        self.language="en"
        self.yellowname=None
        self.redname=None
        self.bluename=None
        self.greenname=None
        self.lastupdate=datetime.date.today().toordinal()
        self.config=ConfigParser.ConfigParser()
        self.load()
        
    def load(self):
        self.config.read(self.file)
        try:
            self.splitterstate=self.config.get("frmMain", "splitter_state")
            self.language=self.config.get("frmSettings", "language")
            self.yellowname=self.config.get("frmInitGame", "yellowname")
            self.redname=self.config.get("frmInitGame", "redname")
            self.bluename=self.config.get("frmInitGame", "bluename")
            self.greenname=self.config.get("frmInitGame", "greenname")
            self.lastupdate=self.config.getint("frmMain", "lastupdate")
        except:
            print ("No hay fichero de configuración")    
        
    def save(self):
        if self.config.has_section("frmMain")==False:
            self.config.add_section("frmMain")
        if self.config.has_section("frmSettings")==False:
            self.config.add_section("frmSettings")
        if self.config.has_section("frmInitGame")==False:
            self.config.add_section("frmInitGame")
        self.config.set("frmSettings",  'language', self.language)
        self.config.set("frmMain",  'splitter_state', self.splitterstate)
        self.config.set("frmMain",  'lastupdate', self.lastupdate)
        self.config.set("frmInitGame",  'yellowname', self.yellowname)
        self.config.set("frmInitGame",  'redname', self.redname)
        self.config.set("frmInitGame",  'bluename', self.bluename)
        self.config.set("frmInitGame",  'greenname', self.greenname)
        with open(self.file, 'w') as configfile:
            self.config.write(configfile)
            
class Casilla(QObject):
    def __init__(self, id, maxfichas, color,  position, rotate, rampallegada, tipo, seguro, posfichas):
        QObject.__init__(self)
        self.id=id
        self.maxfichas=maxfichas
        self.posfichas=posfichas#es un array de vectores 3d de tamaño maxfichas
        self.color=color
        self.position=position
        self.rotate=rotate
        self.rampallegada=rampallegada#booleano que indica si la casilla es de rampa de llegada
        self.tipo=tipo
        self.seguro=seguro# No se debe usar directamente ya que en ruta 1 solo es seguro si el jugador no tiene en casa
        self.buzon=[None]*self.maxfichas #Se crean los huecos y se juega con ellos para mantener la posicion
        self.oglname=self.id+17#Nombre usado para pick por opengl
#        self.texturas=[]
#        self.texturas.append(self.bindTexture(QPixmap(':/glparchis/keke.png')))
        
    def __repr__(self):
        return ("Casilla {0} con {1} fichas dentro".format(self.id, self.buzon_numfichas()))


    def jugadorPropietario(self, mem):
        #Rutas 1
        if self.id==5:
            return mem.jugadores.jugador("yellow")
        elif self.id==22:
            return mem.jugadores.jugador("blue")
        elif self.id==39:
            return mem.jugadores.jugador("red")
        elif self.id==56:
            return mem.jugadores.jugador("green")
        else:
            return None

    def esUnSeguroParaJugador(self, mem,  jugador):
        """Devuelve si la casilla es segura para el jugador pasado como parámetro ante un posible moviiento"""
        if self.id in (5, 22, 39, 56):#Ruta1
            propietario=self.jugadorPropietario(mem)
            if jugador==propietario:
                return True
            else:#color distinto
                if propietario.tieneFichasEnCasa() and self.buzon_numfichas()>0:
                    return False
                else:
                    return True
        else:
            if self.seguro==True:
                return True
            else:
                return False
            

    def dibujar(self, ogl):             
        def quad(p1, p2, p3, p4, color):
            ogl.qglColor(color.qcolor())
#            glNormal3f(1, 1, 1)
#            glColor3d(color.r, color.g, color.b)
            glTexCoord2f(0.0,0.0)
            glVertex3d(p1[0], p1[1], p1[2])
            glTexCoord2f(1.0,0.0)
            glVertex3d(p2[0], p2[1], p2[2])
            glTexCoord2f(1.0,1.0)
            glVertex3d(p3[0], p3[1], p3[2])
            glTexCoord2f(0.0,1.0)
            glVertex3d(p4[0], p4[1], p4[2])          
            
        def panelnumerico():
            def cuadrito(x, texture, rotation):
                glBindTexture(GL_TEXTURE_2D, texture)                
                glPushMatrix()
                glTranslated(self.position[0],self.position[1],self.position[2] )
                glRotated(self.rotate, 0, 0, 1 )            
                glBegin(GL_QUADS)
                ogl.qglColor(self.color.qcolor())
                if rotation==0:
                    glTexCoord2f(0.0,0.0)
                    glVertex3d(x, 1, 0.10)
                    glTexCoord2f(1.0,0.0)
                    glVertex3d(x+1, 1, 0.10)
                    glTexCoord2f(1.0,1.0)
                    glVertex3d(x+1, 2, 0.10)
                    glTexCoord2f(0.0,1.0)
                    glVertex3d(x, 2, 0.10)
                else:
                    glTexCoord2f(0.0,0.0)
                    glVertex3d(x+1, 2, 0.10)
                    glTexCoord2f(1.0,0.0)
                    glVertex3d(x, 2, 0.10)
                    glTexCoord2f(1.0,1.0)
                    glVertex3d(x, 1, 0.10)
                    glTexCoord2f(0.0,1.0)
                    glVertex3d(x+1, 1, 0.10)
                    
                glEnd()
                glPopMatrix()
            ################################
            if self.seguro==True:
                return
            #Cada cuadrante estará a 3x7 estara a 1x1 de ancho
            if len(str(self.id))==1:
                primero=None
                segundo=int(str(self.id)[0])
            if len(str(self.id))==2:
                primero=int(str(self.id)[0])
                segundo=int(str(self.id)[1])
            
            #dos cuadrantes
            if self.id in (60,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 ):
                rotation=180
                tmp=primero
                primero=segundo
                segundo=tmp
            else:
                #un cuadrantes
                if self.id in (8,):
                    rotation=180
                else:
                    rotation=0
            
            glEnable(GL_TEXTURE_2D);
            #PRIMERO
            if primero==None:
                cuadrito(3, ogl.texNumeros[segundo], rotation)
            else:
                cuadrito(2.5, ogl.texNumeros[primero], rotation)
                cuadrito(3.5, ogl.texNumeros[segundo], rotation)
            glDisable(GL_TEXTURE_2D);
            
        def border(a, b, c, d, color):    
            glBegin(GL_LINE_LOOP)
#            self.qglColor(color.qcolor())
            glColor3d(color.r, color.g, color.b)
            glVertex3d(a[0], a[1], a[2]+0.0001)
            glVertex3d(b[0], b[1], b[2]+0.0001)
            glVertex3d(c[0], c[1], c[2]+0.0001)
            glVertex3d(d[0], d[1], d[2]+0.0001)
            glEnd()
        def tipo_inicio():        
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
#            glEnable(GL_TEXTURE_2D);
#            glBindTexture(GL_TEXTURE_2D, ogl.texDecor[0])
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (21, 0, 0)
            v3 = (21, 21, 0)
            v4 = (0, 21, 0)
            v5 = (0, 0, 0.2)
            v6 = (21, 0, 0.2)
            v7 = (21, 21, 0.2)
            v8 = (0, 21, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5, Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170))      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
#            glDisable(GL_TEXTURE_2D);
    
        def tipo_normal():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )            
            if self.id in (5, 12, 17,  22, 29, 34, 39, 46, 51, 56, 63, 68):
                glEnable(GL_TEXTURE_2D);
                glBindTexture(GL_TEXTURE_2D, ogl.texDecor[2])
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (7, 3, 0)
            v4 = (0, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (7, 3, 0.2)
            v8 = (0, 3, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5,Color(70, 70, 70) )      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
            glPopName();
            glPopMatrix()
            glDisable(GL_TEXTURE_2D)
            panelnumerico()
    
        def tipo_oblicuoi():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (7, 3, 0)
            v4 = (3, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (7, 3, 0.2)
            v8 = (3, 3, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
            panelnumerico()
    
        def tipo_oblicuod():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )

            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (7, 0, 0)
            v3 = (4, 3, 0)
            v4 = (0, 3, 0)
            v5 = (0, 0, 0.2)
            v6 = (7, 0, 0.2)
            v7 = (4, 3, 0.2)
            v8 = (0, 3, 0.2)
    
            quad(v1, v2, v3, v4,self.color )      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      

            glEnd()
            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
            panelnumerico()
            
        def tipo_final():
            glInitNames();
            glPushMatrix()
            glPushName(self.oglname);
            glTranslated(self.position[0],self.position[1],self.position[2] )
            glRotated(self.rotate, 0, 0, 1 )
            
            glBegin(GL_QUADS)
            v1 = (0, 0, 0)
            v2 = (0,  0, 0)
            v3 = (15, 0, 0)
            v4 = (7.5, 7.5, 0)
            v5 = (0, 0, 0.2)
            v6 = (0, 0, 0.2)
            v7 = (15, 0, 0.2)
            v8 = (7.5, 7.5, 0.2)
    
            quad(v1, v2, v3, v4, self.color)      
            quad(v8, v7, v6, v5, Color(70, 70, 70))      
            quad(v1, v4, v8, v5,Color(170, 170, 170))      
            quad(v6, v7, v3, v2, Color(170, 170, 170))      
            quad(v5, v6, v2, v1, Color(170, 170, 170) )      
            quad(v4, v3, v7, v8, Color(170, 170, 170))      
    
            glEnd()

            border(v5, v6, v7, v8, Color(0, 0, 0))
    
            glPopName();
            glPopMatrix()
        ##################################
        if self.tipo==0:
            tipo_inicio()
        elif self.tipo==1:
            tipo_final()
        elif self.tipo==2:
            tipo_oblicuoi()
        elif self.tipo==4:
            tipo_oblicuod()
        else:
            tipo_normal()
            
    def dibujar_fichas(self, ogl):
        if self.buzon_numfichas()>0:
            for i, f in enumerate(self.buzon):       
                if f!=None:
                    f.dibujar(ogl, i)

    def tieneBarrera(self):
        """Devuelve un booleano, las fichas de la barrera se pueden sacar del buzón"""
        if self.tipo not in (0, 1):#Casilla inicio y final
            if self.maxfichas==2:
                if self.buzon_numfichas()==2:
                    if self.buzon[0].jugador==self.buzon[1].jugador:
                        return True
        return False

    def posicionLibreEnBuzon(self):
        """Función que devuelve la posición de un sitio libre con un entero. En caso negativo devuelve -1"""
        for i, p in enumerate(self.buzon):
            if p==None:
                return i
        return -1
        
    def buzon_append(self,  ficha):
        """No chequea debe ser comprobado antes"""
        self.buzon[self.posicionLibreEnBuzon()]=ficha
            
    def buzon_remove(self, ficha):
        """No chequea debe ser comprobado antes"""
        for i, f in enumerate(self.buzon):
            if f==ficha:
                self.buzon[i]=None
                return
        print ("No se ha podido hacer buzon_remove con {0}".format(ficha))
                
    def buzon_numfichas(self):
        """Función que devuelve el número de fichas en el buzón"""
        resultado=0
        for f in self.buzon:
            if f!=None:
                resultado=resultado+1
        return resultado

    def buzon_fichas(self):
        """Como ahora puede haber una ficha y estar en buzon[1] se hace necesario esta función.
        Devuelve una lista de fichas con una tupla (posicion, ficha)"""
        resultado=[]
        for i, f in enumerate(self.buzon):
            if f!=None:
                resultado.append((i, f))
        return resultado

class Mem:
    def __init__(self):     
        self.dic_casillas={}#Lista cuya posicion coincide con el id del objeto jugador que lleva dentro
        self.dic_fichas={}
        self.dic_colores={}
        self.jugadores=SetJugadores()
        self.dic_rutas={}
        self.dado=Dado()
        self.jugadoractual=None
        self.selFicha=None
        self.inittime=None#Tiempo inicio partida
        self.cfgfile=None#fichero configuración que se crea en glparchis.py
           
        self.mediaObject = None
        self.sound=True#Enciende o apaga el sonido
        parent=QCoreApplication.instance()
        self.mediaObject = Phonon.MediaObject(parent)
        audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, parent)
        Phonon.createPath(self.mediaObject, audioOutput)

    def play(self, sound):
        if self.sound==True:
            so=os.environ['glparchisso']
            if so=="bin.windows" or so=="bin.linux":
                url= sound + ".wav"
            elif so=="src.windows":
                url="../share/glparchis/sounds/"+sound+".wav"
            elif so=="src.linux":
                url="/usr/share/glparchis/sounds/"+sound+".wav"
            self.mediaObject.setCurrentSource(Phonon.MediaSource(url))
            self.mediaObject.play()
            time.sleep(0.4)
            QCoreApplication.processEvents();    

    def colores(self, name=None):
        if name==None:
            return dic2list(self.dic_colores)
        else:
            return self.dic_colores[str(name)]
            
    def rutas(self, name=None):
        if name==None:
            return dic2list(self.dic_rutas)
        else:
            return self.dic_rutas[str(name)]

        
    def generar_fichas(self):
        """Debe generarse despuñes de jugadores"""
        id=0
        for c in self.colores():
            for i in range(4):
                self.dic_fichas[str(id)]=Ficha(id, i, c, self.jugadores.jugador(c.name), self.rutas(c.name))
                self.jugadores.jugador(c.name).fichas.arr.append(self.dic_fichas[str(id)])#Rellena el SetFichas del jugador
                id=id+1

            
    def generar_jugadores(self):
        for c in self.colores():
            j=Jugador(c)
            self.jugadores.arr.append(j)
            j.dado=self.dado

    def fichas(self, name=None):
        if name==None:
            return dic2list(self.dic_fichas)
        else:
            return self.dic_fichas[str(name)]

    def casillas(self, name=None):
        if name==None:
            return dic2list(self.dic_casillas)
        else:
            return self.dic_casillas[str(name)]
            
            

class Mem6(Mem):    
    def __init__(self):
        Mem.__init__(self)
        self.generar_colores()
        self.generar_jugadores()
        self.generar_casillas()
        self.generar_rutas()
        self.generar_fichas()
        
        self.circulo=Circulo(self, 68)



    def generar_colores(self):
        self.dic_colores["red"]=Color(255, 0, 0, "red")
        self.dic_colores["yellow"]=Color( 255, 255, 0, "yellow")
        self.dic_colores["blue"]=Color(0, 0, 255, "blue")
        self.dic_colores["green"]=Color(0, 255, 0, "green")

    def generar_rutas(self):
        return

    def generar_casillas(self):
        return

class Mem4(Mem):
    def __init__(self):
        Mem.__init__(self)
        
        self.generar_colores()
        self.generar_jugadores()
        self.generar_casillas()
        self.generar_rutas()
        self.generar_fichas()
        
        self.circulo=Circulo(self, 68)



    def generar_colores(self):
        self.dic_colores["red"]=Color(255, 0, 0, "red")
        self.dic_colores["yellow"]=Color( 255, 255, 0, "yellow")
        self.dic_colores["blue"]=Color(0, 0, 255, "blue")
        self.dic_colores["green"]=Color(0, 255, 0, "green")

    def generar_rutas(self):
        ruta=[None]*73
        ruta[0]=(101, 102, 103, 104)
        ruta[1]=(5, 22, 39, 56)
        ruta[2]=(6, 23, 40, 57)
        ruta[3]=(7, 24, 41, 58)
        ruta[4]=(8, 25, 42, 59)
        ruta[5]=(9, 26, 43, 60)
        ruta[6]=(10, 27, 44, 61)
        ruta[7]=(11, 28, 45, 62)
        ruta[8]=(12, 29, 46, 63)
        ruta[9]=(13, 30, 47, 64)
        ruta[10]=(14, 31, 48, 65)
        ruta[11]=(15, 32, 49, 66)
        ruta[12]=(16, 33, 50, 67)
        ruta[13]=(17, 34, 51, 68)
        ruta[14]=(18, 35, 52, 1)
        ruta[15]=(19, 36, 53, 2)
        ruta[16]=(20, 37, 54, 3)
        ruta[17]=(21, 38, 55, 4)
        ruta[18]=(22, 39, 56, 5)
        ruta[19]=(23, 40, 57, 6)
        ruta[20]=(24, 41, 58, 7)
        ruta[21]=(25, 42, 59, 8)
        ruta[22]=(26, 43, 60, 9)
        ruta[23]=(27, 44, 61, 10)
        ruta[24]=(28, 45, 62, 11)
        ruta[25]=(29, 46, 63, 12)
        ruta[26]=(30, 47, 64, 13)
        ruta[27]=(31, 48, 65, 14)
        ruta[28]=(32, 49, 66, 15)
        ruta[29]=(33, 50, 67, 16)
        ruta[30]=(34, 51, 68, 17)
        ruta[31]=(35, 52, 1, 18)
        ruta[32]=(36, 53, 2, 19)
        ruta[33]=(37, 54, 3, 20)
        ruta[34]=(38, 55, 4, 21)
        ruta[35]=(39, 56, 5, 22)
        ruta[36]=(40, 57, 6, 23)
        ruta[37]=(41, 58, 7, 24)
        ruta[38]=(42, 59, 8, 25)
        ruta[39]=(43, 60, 9, 26)
        ruta[40]=(44, 61, 10, 27)
        ruta[41]=(45, 62, 11, 28)
        ruta[42]=(46, 63, 12, 29)
        ruta[43]=(47, 64, 13, 30)
        ruta[44]=(48, 65, 14, 31)
        ruta[45]=(49, 66, 15,  32)
        ruta[46]=(50, 67, 16 , 33)
        ruta[47]=(51, 68, 17 , 34)
        ruta[48]=(52, 1, 18 , 35)
        ruta[49]=(53, 2, 19, 36)
        ruta[50]=(54, 3, 20, 37)
        ruta[51]=(55, 4, 21, 38)
        ruta[52]=(56, 5, 22, 39)
        ruta[53]=(57, 6, 23, 40)
        ruta[54]=(58, 7, 24, 41)
        ruta[55]=(59, 8, 25, 42)
        ruta[56]=(60, 9, 26, 43)
        ruta[57]=(61, 10, 27, 44)
        ruta[58]=(62, 11, 28, 45)
        ruta[59]=(63, 12, 29, 46)
        ruta[60]=(64, 13, 30, 47)
        ruta[61]=(65, 14, 31, 48)
        ruta[62]=(66, 15, 32, 49)
        ruta[63]=(67, 16, 33, 50)
        ruta[64]=(68, 17, 34, 51)
        ruta[65]=(69, 77, 85, 93)
        ruta[66]=(70, 78, 86, 94)
        ruta[67]=(71, 79, 87, 95)
        ruta[68]=(72, 80, 88, 96)
        ruta[69]=(73, 81, 89, 97)
        ruta[70]=(74, 82, 90, 98)
        ruta[71]=(75, 83, 91, 99)
        ruta[72]=(76, 84, 92, 100)
        
        self.dic_rutas["yellow"]=Ruta()
        self.dic_rutas["red"]=Ruta()
        self.dic_rutas['blue']=Ruta()
        self.dic_rutas['green']=Ruta()
        for r in ruta:
            self.dic_rutas["yellow"].arr.append(self.casillas(r[0]))
            self.dic_rutas["red"].arr.append(self.casillas(r[2]))
            self.dic_rutas['blue'].arr.append(self.casillas(r[1]))
            self.dic_rutas['green'].arr.append(self.casillas(r[3]))


            
    def save(self, filename):
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = ConfigParser.ConfigParser()
        config.add_section("yellow")
        config.set("yellow",  'ia', int(self.jugadores.jugador('yellow').ia))
        config.set("yellow",  'name', self.jugadores.jugador('yellow').name)
        config.set("yellow",  'plays', int(self.jugadores.jugador('yellow').plays))
        if self.jugadores.jugador('yellow').plays==True:
            config.set("yellow",  'rutaficha1', self.jugadores.jugador('yellow').fichas.arr[0].posruta)
            config.set("yellow",  'rutaficha2',  self.jugadores.jugador('yellow').fichas.arr[1].posruta)
            config.set("yellow",  'rutaficha3',  self.jugadores.jugador('yellow').fichas.arr[2].posruta)
            config.set("yellow",  'rutaficha4',  self.jugadores.jugador('yellow').fichas.arr[3].posruta)
        config.add_section("blue")
        config.set("blue",  'ia', int(self.jugadores.jugador('blue').ia))
        config.set("blue",  'name', self.jugadores.jugador('blue').name)
        config.set("blue",  'plays', int(self.jugadores.jugador('blue').plays))
        if self.jugadores.jugador('blue').plays==True:        
            config.set("blue",  'rutaficha1', self.jugadores.jugador('blue').fichas.arr[0].posruta)
            config.set("blue",  'rutaficha2',  self.jugadores.jugador('blue').fichas.arr[1].posruta)
            config.set("blue",  'rutaficha3',  self.jugadores.jugador('blue').fichas.arr[2].posruta)
            config.set("blue",  'rutaficha4',  self.jugadores.jugador('blue').fichas.arr[3].posruta) 
        config.add_section("red")
        config.set("red",  'ia', int(self.jugadores.jugador('red').ia))
        config.set("red",  'name', self.jugadores.jugador('red').name)
        config.set("red",  'plays', int(self.jugadores.jugador('red').plays))
        if self.jugadores.jugador('red').plays==True:        
            config.set("red",  'rutaficha1', self.jugadores.jugador('red').fichas.arr[0].posruta)
            config.set("red",  'rutaficha2',  self.jugadores.jugador('red').fichas.arr[1].posruta)
            config.set("red",  'rutaficha3',  self.jugadores.jugador('red').fichas.arr[2].posruta)
            config.set("red",  'rutaficha4',  self.jugadores.jugador('red').fichas.arr[3].posruta)    
        config.add_section("green")
        config.set("green",  'ia', int(self.jugadores.jugador('green').ia))
        config.set("green",  'name', self.jugadores.jugador('green').name)
        config.set("green",  'plays', int(self.jugadores.jugador('green').plays))        
        if self.jugadores.jugador('green').plays==True:
            config.set("green",  'rutaficha1', self.jugadores.jugador('green').fichas.arr[0].posruta)
            config.set("green",  'rutaficha2',  self.jugadores.jugador('green').fichas.arr[1].posruta)
            config.set("green",  'rutaficha3',  self.jugadores.jugador('green').fichas.arr[2].posruta)
            config.set("green",  'rutaficha4',  self.jugadores.jugador('green').fichas.arr[3].posruta)    
        config.add_section("game")
        config.set("game", 'playerstarts',self.jugadoractual.color.name)
        config.set("game", 'fakedice','')
        with open(filename, 'w') as configfile:
            config.write(configfile)            
        os.chdir(cwd)

                    
    def generar_casillas(self):
        def defineSeguro( id):
            if id==5 or id==12 or id==17 or id==22 or id==29 or id==34 or id==39 or id==46 or id==51  or id==56 or id==63 or id==68:
                return True
            elif id>=69 and id<=100:#Las de la rampa de llegada también son seguras
                return True
            else:
                return False
    
        def defineMaxFichas( id):
            if id==101 or id==102 or id==103 or id==104 or id==76 or id==84 or id==92 or id==100:
                return 4
            else:
                return 2
    
        def defineRampaLlegada(id):
            if id>=69 and id<= 100:
               return True
            return False
    
        def defineTipo( id):
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
    
        def defineColor( id):
            if id==5 or (id>=69 and id<=76) or id==101:
               return Color(255, 255, 30)       #amarillo 
            elif id==39 or (id>=85 and id<=92) or id==103:
               return Color(255, 30, 30)#rojo
            elif id==22 or (id>=77 and id<=84) or id==102:
               return Color(30, 30, 255)#azul
            elif id==56 or (id>=93 and id<=100) or id==104:
               return Color(30, 255, 30) #verde
#            elif id==68 or  id==63 or  id==51 or id==46 or id==34 or  id==29 or  id==17 or   id==12:  
#               return Color(128, 128, 128)#gris
            else:
                return Color(255, 255, 255)            
                
        def defineRotate( id):
            if (id>=10 and id<=24) or (id>=77 and id<=83) or(id>=43 and id <=59) or (id>=93 and id<=100):
               return 90
            if id==60 or id==8 or id==76:
                return 180
            if id==9 or id==25 or id==84:
                return 270
            else:
                return 0        
                
        ##############################        
        posFichas=[None]*105
        posFichas[0]=((0, 0, 0), (0, 0, 0))
        posFichas[1]=((22.7, 61.5, 0.9), (26.3, 61.5, 0.9))
        posFichas[2]=((22.7, 58.5, 0.9), (26.3, 58.5, 0.9))
        posFichas[3]=((22.7, 55.5, 0.9), (26.3, 55.5, 0.9))
        posFichas[4]=((22.7, 52.5, 0.9), (26.3, 52.5, 0.9))
        posFichas[5]=((22.7, 49.5, 0.9), (26.3, 49.5, 0.9))
        posFichas[6]=((22.7, 46.5, 0.9), (26.3, 46.5, 0.9))
        posFichas[7]=((22.7, 43.5, 0.9), (26.3, 43.5, 0.9))
        posFichas[8]=((24.5, 40.5, 0.9), (26.5, 40.5, 0.9))
        posFichas[9]=((22.5, 38.5, 0.9), (22.5, 36.5, 0.9))
        posFichas[10]=((19.5, 40.3, 0.9), (19.5, 36.7, 0.9))
        posFichas[11]=((16.5, 40.3, 0.9), (16.5, 36.7, 0.9))
        posFichas[12]=((13.5, 40.3, 0.9), (13.5, 36.7, 0.9))
        posFichas[13]=((10.5, 40.3, 0.9), (10.5, 36.7, 0.9))
        posFichas[14]=((7.5, 40.3, 0.9), (7.5, 36.7, 0.9))
        posFichas[15]=((4.5, 40.3, 0.9), (4.5, 36.7, 0.9))
        posFichas[16]=((1.5, 40.3, 0.9), (1.5, 36.7, 0.9))
        posFichas[17]=((1.5, 33.3, 0.9), (1.5, 29.7, 0.9))
        posFichas[18]=((1.5, 26.3, 0.9), (1.5, 22.7, 0.9))
        posFichas[19]=((4.5, 26.3, 0.9), (4.5, 22.7, 0.9))
        posFichas[20]=((7.5, 26.3, 0.9), (7.5, 22.7, 0.9))
        posFichas[21]=((10.5, 26.3, 0.9), (10.5, 22.7, 0.9))
        posFichas[22]=((13.5, 26.3, 0.9), (13.5, 22.7, 0.9))
        posFichas[23]=((16.5, 26.3, 0.9), (16.5, 22.7, 0.9))
        posFichas[24]=((19.5, 26.3, 0.9), (19.5, 22.7, 0.9))
        posFichas[25]=((22.5, 26.5, 0.9), (22.5, 24.5, 0.9))
        posFichas[26]=((24.5, 22.5, 0.9), (26.5, 22.5, 0.9))
        posFichas[27]=((22.7, 19.5, 0.9), (26.3, 19.5, 0.9))
        posFichas[28]=((22.7, 16.5, 0.9), (26.3, 16.5, 0.9))
        posFichas[29]=((22.7, 13.5, 0.9), (26.3, 13.5, 0.9))
        posFichas[30]=((22.7, 10.5, 0.9), (26.3, 10.5, 0.9))
        posFichas[31]=((22.7, 7.5, 0.9), (26.3, 7.5, 0.9))
        posFichas[32]=((22.7, 4.5, 0.9), (26.3, 4.5, 0.9))
        posFichas[33]=((22.7, 1.5, 0.9), (26.3, 1.5, 0.9))
        posFichas[34]=((29.7, 1.5, 0.9), (33.3, 1.5, 0.9))
        posFichas[35]=((36.7, 1.5, 0.9), (40.3, 1.5, 0.9))
        posFichas[36]=((36.7, 4.5, 0.9), (40.3, 4.5, 0.9))
        posFichas[37]=((36.7, 7.5, 0.9), (40.3, 7.5, 0.9))
        posFichas[38]=((36.7, 10.5, 0.9), (40.3, 10.5, 0.9))
        posFichas[39]=((36.7, 13.5, 0.9), (40.3, 13.5, 0.9))
        posFichas[40]=((36.7, 16.5, 0.9), (40.3, 16.5, 0.9))
        posFichas[41]=((36.7, 19.5, 0.9), (40.3, 19.5, 0.9))
        posFichas[42]=((36.5, 22.5, 0.9), (38.5, 22.5, 0.9))
        posFichas[43]=((40.5, 26.5, 0.9), (40.5, 24.5, 0.9))
        posFichas[44]=((43.5, 26.3, 0.9), (43.5, 22.7, 0.9))
        posFichas[45]=((46.5, 26.3, 0.9), (46.5, 22.7, 0.9))
        posFichas[46]=((49.5, 26.3, 0.9), (49.5, 22.7, 0.9))
        posFichas[47]=((52.5, 26.3, 0.9), (52.5, 22.7, 0.9))
        posFichas[48]=((55.5, 26.3, 0.9), (55.5, 22.7, 0.9))
        posFichas[49]=((58.5, 26.3, 0.9), (58.5, 22.7, 0.9))
        posFichas[50]=((61.5, 26.3, 0.9), (61.5, 22.7, 0.9))
        posFichas[51]=((61.5, 33.3, 0.9), (61.5, 29.7, 0.9))
        posFichas[52]=((61.5, 40.3, 0.9), (61.5, 36.7, 0.9))
        posFichas[53]=((58.5, 40.3, 0.9), (58.5, 36.7, 0.9))
        posFichas[54]=((55.5, 40.3, 0.9), (55.5, 36.7, 0.9))
        posFichas[55]=((52.5, 40.3, 0.9), (52.5, 36.7, 0.9))
        posFichas[56]=((49.5, 40.3, 0.9), (49.5, 36.7, 0.9))
        posFichas[57]=((46.5, 40.3, 0.9), (46.5, 36.7, 0.9))
        posFichas[58]=((43.5, 40.3, 0.9), (43.5, 36.7, 0.9))
        posFichas[59]=((40.5, 38.5, 0.9), (40.5, 36.5, 0.9))
        posFichas[60]=((36.5, 40.5, 0.9), (38.5, 40.5, 0.9))
        posFichas[61]=((36.7, 43.5, 0.9), (40.3, 43.5, 0.9))
        posFichas[62]=((36.7, 46.5, 0.9), (40.3, 46.5, 0.9))
        posFichas[63]=((36.7, 49.5, 0.9), (40.3, 49.5, 0.9))
        posFichas[64]=((36.7, 52.5, 0.9), (40.3, 52.5, 0.9))
        posFichas[65]=((36.7, 55.5, 0.9), (40.3, 55.5, 0.9))
        posFichas[66]=((36.7, 58.5, 0.9), (40.3, 58.5, 0.9))
        posFichas[67]=((36.7, 61.5, 0.9), (40.3, 61.5, 0.9))
        posFichas[68]=((29.7, 61.5, 0.9), (33.3, 61.5, 0.9))
        posFichas[69]=((29.7, 58.5, 0.9), (33.3, 58.5, 0.9))
        posFichas[70]=((29.7, 55.5, 0.9), (33.3, 55.5, 0.9))
        posFichas[71]=((29.7, 52.5, 0.9), (33.3, 52.5, 0.9))
        posFichas[72]=((29.7, 49.5, 0.9), (33.3, 49.5, 0.9))
        posFichas[73]=((29.7, 46.5, 0.9), (33.3, 46.5, 0.9))
        posFichas[74]=((29.7, 43.5, 0.9), (33.3, 43.5, 0.9))
        posFichas[75]=((29.7, 40.5, 0.9), (33.3, 40.5, 0.9))
        posFichas[76]=((28.5, 37.5, 0.9), (31.5, 37.5, 0.9),  (34.5, 37.5, 0.9),  (31.5, 34.5, 0.9))
        posFichas[77]=((4.5, 33.3, 0.9), (4.5, 29.7, 0.9))
        posFichas[78]=((7.5, 33.3, 0.9), (7.5, 29.7, 0.9))
        posFichas[79]=((10.5, 33.3, 0.9), (10.5, 29.7, 0.9))
        posFichas[80]=((13.5, 33.3, 0.9), (13.5, 29.7, 0.9))
        posFichas[81]=((16.5, 33.3, 0.9), (16.5, 29.7, 0.9))
        posFichas[82]=((19.5, 33.3, 0.9), (19.5, 29.7, 0.9))
        posFichas[83]=((22.5, 33.3, 0.9), (22.5, 29.7, 0.9))
        posFichas[84]=((25.5, 31.5, 0.9), (25.5, 28.5, 0.9), (25.5, 34.5, 0.9), (28.5, 31.5, 0.9))
        posFichas[85]=((29.7, 4.5, 0.9), (33.3, 4.5, 0.9))
        posFichas[86]=((29.7, 7.5, 0.9), (33.3, 7.5, 0.9))
        posFichas[87]=((29.7, 10.5, 0.9), (33.3, 10.5, 0.9))
        posFichas[88]=((29.7, 13.5, 0.9), (33.3, 13.5, 0.9))
        posFichas[89]=((29.7, 16.5, 0.9), (33.3, 16.5, 0.9))
        posFichas[90]=((29.7, 19.5, 0.9), (33.3, 19.5, 0.9))
        posFichas[91]=((29.7, 22.5, 0.9), (33.3, 22.5, 0.9))
        posFichas[92]=((28.5, 25.5, 0.9), (31.5, 25.5, 0.9), (34.5, 25.5, 0.9),  (31.5, 28.5, 0.9))
        posFichas[93]=((58.5, 33.3, 0.9), (58.5, 29.7, 0.9))
        posFichas[94]=((55.5, 33.3, 0.9), (55.5, 29.7, 0.9))
        posFichas[95]=((52.5, 33.3, 0.9), (52.5, 29.7, 0.9))
        posFichas[96]=((49.5, 33.3, 0.9), (49.5, 29.7, 0.9))
        posFichas[97]=((46.5, 33.3, 0.9), (46.5, 29.7, 0.9))
        posFichas[98]=((43.5, 33.3, 0.9), (43.5, 29.7, 0.9))
        posFichas[99]=((40.5, 33.3, 0.9), (40.5, 29.7, 0.9))
        posFichas[100]=((37.5, 31.5, 0.9), (37.5, 28.5, 0.9), (37.5, 34.5, 0.9), (34.5, 31.5, 0.9))
        posFichas[101]=((7, 49, 0.9), (14, 49, 0.9), (14, 56, 0.9), (7, 56, 0.9))
        posFichas[102]=((7, 7, 0.9), (14, 7, 0.9), (14, 14, 0.9), (7, 14, 0.9))
        posFichas[103]=((49, 7, 0.9), (56, 7, 0.9), (49, 14, 0.9), (56, 14, 0.9))
        posFichas[104]=((49, 49, 0.9), (56, 49, 0.9), (49, 56, 0.9), (56, 56, 0.9))        
        
        
        posCasillas=[None]*105
        posCasillas[0]=(0, 0, 0)
        posCasillas[1]=(21, 60, 0.7)
        posCasillas[2]=(21, 57, 0.7)
        posCasillas[3]=(21, 54, 0.7)
        posCasillas[4]=(21, 51, 0.7)
        posCasillas[5]=(21, 48, 0.7)
        posCasillas[6]=(21, 45, 0.7)
        posCasillas[7]=(21, 42, 0.7)
        posCasillas[8]=(28,  42, 0.7)
        posCasillas[9]=(21, 42, 0.7)
        posCasillas[10]=(21, 35, 0.7)
        posCasillas[11]=(18, 35, 0.7)
        posCasillas[12]=(15, 35, 0.7)
        posCasillas[13]=(12, 35, 0.7)
        posCasillas[14]=(9, 35, 0.7)
        posCasillas[15]=(6, 35, 0.7)
        posCasillas[16]=(3, 35, 0.7)
        posCasillas[17]=(3, 28, 0.7)
        posCasillas[18]=(3, 21, 0.7)
        posCasillas[19]=(6, 21, 0.7)
        posCasillas[20]=(9, 21, 0.7)
        posCasillas[21]=(12, 21, 0.7)
        posCasillas[22]=(15, 21, 0.7)
        posCasillas[23]=(18, 21, 0.7)
        posCasillas[24]=(21, 21, 0.7)
        posCasillas[25]=(21, 28, 0.7)
        posCasillas[26]=(21, 21, 0.7)
        posCasillas[27]=(21, 18, 0.7)
        posCasillas[28]=(21, 15, 0.7)
        posCasillas[29]=(21, 12, 0.7)
        posCasillas[30]=(21, 9, 0.7)
        posCasillas[31]=(21, 6, 0.7)
        posCasillas[32]=(21, 3, 0.7)
        posCasillas[33]=(21, 0, 0.7)
        posCasillas[34]=(28, 0, 0.7)
        posCasillas[35]=(35, 0, 0.7)
        posCasillas[36]=(35, 3, 0.7)
        posCasillas[37]=(35, 6, 0.7)
        posCasillas[38]=(35, 9, 0.7)
        posCasillas[39]=(35, 12, 0.7)
        posCasillas[40]=(35, 15, 0.7)
        posCasillas[41]=(35, 18, 0.7)
        posCasillas[42]=(35, 21, 0.7)
        posCasillas[43]=(42, 21, 0.7)
        posCasillas[44]=(45, 21, 0.7)
        posCasillas[45]=(48, 21, 0.7)
        posCasillas[46]=(51, 21, 0.7)
        posCasillas[47]=(54, 21, 0.7)
        posCasillas[48]=(57, 21, 0.7)
        posCasillas[49]=(60, 21, 0.7)
        posCasillas[50]=(63, 21, 0.7)
        posCasillas[51]=(63, 28, 0.7)
        posCasillas[52]=(63, 35, 0.7)
        posCasillas[53]=(60, 35, 0.7)
        posCasillas[54]=(57, 35, 0.7)
        posCasillas[55]=(54, 35, 0.7)
        posCasillas[56]=(51, 35, 0.7)
        posCasillas[57]=(48, 35, 0.7)
        posCasillas[58]=(45, 35, 0.7)
        posCasillas[59]=(42, 35, 0.7)
        posCasillas[60]=(42 ,42, 0.7)
        posCasillas[61]=(35, 42, 0.7)
        posCasillas[62]=(35, 45, 0.7)
        posCasillas[63]=(35, 48, 0.7)
        posCasillas[64]=(35, 51, 0.7)
        posCasillas[65]=(35, 54, 0.7)
        posCasillas[66]=(35, 57, 0.7)
        posCasillas[67]=(35, 60, 0.7)
        posCasillas[68]=(28, 60, 0.7)
        posCasillas[69]=(28, 57, 0.7)
        posCasillas[70]=(28, 54, 0.7)
        posCasillas[71]=(28, 51, 0.7)
        posCasillas[72]=(28, 48, 0.7)
        posCasillas[73]=(28, 45, 0.7)
        posCasillas[74]=(28, 42, 0.7)
        posCasillas[75]=(28, 39, 0.7)
        posCasillas[76]=(39, 39, 0.7)
        posCasillas[77]=(6, 28, 0.7)
        posCasillas[78]=(9, 28, 0.7)
        posCasillas[79]=(12, 28, 0.7)
        posCasillas[80]=(15, 28, 0.7)
        posCasillas[81]=(18, 28, 0.7)
        posCasillas[82]=(21, 28, 0.7)
        posCasillas[83]=(24, 28, 0.7)
        posCasillas[84]=(24, 39, 0.7)
        posCasillas[85]=(28, 3, 0.7)
        posCasillas[86]=(28, 6, 0.7)
        posCasillas[87]=(28, 9, 0.7)
        posCasillas[88]=(28, 12, 0.7)
        posCasillas[89]=(28, 15, 0.7)
        posCasillas[90]=(28, 18, 0.7)
        posCasillas[91]=(28, 21, 0.7)
        posCasillas[92]=(24, 24, 0.7)
        posCasillas[93]=(60, 28, 0.7)
        posCasillas[94]=(57, 28, 0.7)
        posCasillas[95]=(54, 28, 0.7)
        posCasillas[96]=(51, 28, 0.7)
        posCasillas[97]=(48, 28, 0.7)
        posCasillas[98]=(45, 28, 0.7)
        posCasillas[99]=(42, 28, 0.7)
        posCasillas[100]=(39, 24, 0.7)
        posCasillas[101]=(0, 42, 0.7)
        posCasillas[102]=(0, 0, 0.7)
        posCasillas[103]=(42, 0, 0.7)
        posCasillas[104]=(42,  42, 0.7)
        for i in range(0, 105):#Se debe inializar Antes que las fichas
            self.dic_casillas[str(i)]=Casilla( i, defineMaxFichas(i), defineColor(i), posCasillas[i],  defineRotate(i) , defineRampaLlegada(i), defineTipo(i), defineSeguro(i), posFichas[i])
            
            
            
    def load(self, filename):       
#        os.chdir("/home/keko/Proyectos/glparchis/pyglParchis/saves/") #SOLO DEBUGGING
        cwd=os.getcwd()
        os.chdir(os.path.expanduser("~/.glparchis/"))
        config = ConfigParser.ConfigParser()
        config.read(filename)

        yellow=self.jugadores.jugador('yellow')
        yellow.name=config.get('yellow', 'name')
        yellow.ia=i2b(config.getint("yellow", "ia"))
        yellow.plays=(i2b(config.getint("yellow", "plays")))
        
        blue=self.jugadores.jugador('blue')
        blue.name=config.get("blue", "name")
        blue.ia=i2b(config.getint("blue", "ia"))
        blue.plays=(i2b(config.getint("blue", "plays")))
        
        red=self.jugadores.jugador('red')
        red.name=config.get("red", "name")
        red.ia=i2b(config.getint("red", "ia"))
        red.plays=(i2b(config.getint("red", "plays")))
        
        green=self.jugadores.jugador('green')
        green.name=config.get("green", "name")
        green.ia=i2b(config.getint("green", "ia"))
        green.plays=(i2b(config.getint("green", "plays")))  

        for j in self.jugadores.arr:
            if j.plays==True:
                j.fichas.arr[0].mover(config.getint(j.color.name, "rutaficha1"), False,  True)
                j.fichas.arr[1].mover(config.getint(j.color.name, "rutaficha2"), False,  True)
                j.fichas.arr[2].mover(config.getint(j.color.name, "rutaficha3"), False,  True)
                j.fichas.arr[3].mover(config.getint(j.color.name, "rutaficha4"), False,  True)

        fake=config.get("game", 'fakedice')
        if fake!="":
            for i in  fake.split(";")  :
                self.dado.fake.append(int(i))
        self.jugadoractual=self.jugadores.jugador(config.get("game", 'playerstarts'))    
        self.jugadoractual.movimientos_acumulados=None#Comidas ymetidas
        self.jugadoractual.LastFichaMovida=None #Se utiliza cuando se va a casa

        os.chdir(cwd)
            
def dic2list(dic):
    """Función que convierte un diccionario pasado como parametro a una lista de objetos"""
    resultado=[]
    for k,  v in dic.items():
        resultado.append(v)
    return resultado


def cargarQTranslator(cfgfile):  
    """language es un string"""
    so=os.environ['glparchisso']
    if so=="src.linux":
        cfgfile.qtranslator.load("/usr/share/glparchis/glparchis_" + cfgfile.language + ".qm")
    elif so=="src.windows":
        cfgfile.qtranslator.load("../share/glparchis/glparchis_" + cfgfile.language + ".qm")
    elif so=="bin.windows" or so=="bin.linux":
        cfgfile.qtranslator.load("glparchis_" + cfgfile.language + ".qm")
    qApp.installTranslator(cfgfile.qtranslator);
