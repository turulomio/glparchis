 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_frmHelp import *

class frmHelp(QDialog, Ui_frmHelp):
    def __init__(self, parent = None, name = None, modal = False):
        """
        Constructor
        
        @param parent The parent widget of this dialog. (QWidget)
        @param name The name of this dialog. (QString)
        @param modal Flag indicating a modal dialog. (boolean)
        """
        QDialog.__init__(self, parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        self.browser.setHtml(
            self.trUtf8(u"<h2>Historia</h2>")+
            self.trUtf8(u"El juego del Parchís es una variación del Parchisi, un juego que tiene su origen en la India (Siglo XVI). Más información puede obtenerla en la <a href='http://es.wikipedia.org/wiki/Parchis'>Wikipedia</a>")+
            self.trUtf8(u"<h2>Reglas de juego</h2>")+            
            self.trUtf8(u"Hay muchas variantes del juego, dependiendo fundamentalmente del lugar en el que se juega. España ha sido uno de los países en los que más arraigo ha tenido el juego. Es por ello que glParchis utiliza las normas más comunes de juego en España")+
            self.trUtf8(u"<h3>Reglas de juego en glParchis</h3>")+
            self.trUtf8(u"Cada jugador dispone de 4 fichas que deberá mover por el tablero usando un dado y siguiendo un turno entre los distintos jugadores.<p>")+
            self.trUtf8(u"Cada ficha partirá de una casilla inicial, de la que sólo podrá salir con un 5. Recorrerá una ruta con un número de casillas igual para todos los jugadores, que termina en una rampa de llegada de su color y una casilla final. Este movimiento lo realizará en sentido contrario a las agujas del reloj<p>")+
            self.trUtf8(u"Existen unas casillas seguras (casillas con circulo gris), en las que dos fichas de distintos jugadores pueden convivir. En el resto (casillas blancas), la ficha que llega en segundo lugar come (manda a la casilla inicial) a la que llegó en primer lugar y obtiene el derecho de mover 20 casillas.<p>")+
            self.trUtf8(u"Cuando una ficha llega a la casilla final, el jugador obtiene el derecho de mover 10 puntos.<p>")+
            self.trUtf8(u"Cuando dos fichas del mismo color están en una misma casilla, se produce una barrera. Este hecho impide que el resto de jugadores puedan avanzar por ella. El jugador está obligado a abrir la barrera cuando obtiene un 6 con el dado.<p>")+
            self.trUtf8(u"Cuando un jugador tiene todas sus fichas fuera de casa (casilla inicial) y obtiene un 6, contará 7 casillas de movimiento en el tablero.<p>")+
            self.trUtf8(u"Cuando en la casilla de salida de un jugador hay dos fichas distintas y el jugador del mismo color de la casilla de salida saca un cinco y debe sacar una ficha, la última ficha que llegó se va a casa.<p>")+    
            self.trUtf8(u"<h3>Puntuación</h3>")+
            self.trUtf8(u"La puntuación viene dada por el número de casillas que le falta recorrer a los otros jugadores menos las que me faltan a mí. A esta cantidad se le suma la diferencia entre las fichas que he comido y las que me han comido, multiplicadas por 40.<p>")+        
            self.trUtf8(u"<h2>Interfaz de usuario</h2>")+
            self.trUtf8(u"<h3>Guardado automático</h3>")+            
            self.trUtf8(u"La aplicación guarda automáticamente el estado de la partida cada vez que hay un turno de un jugador humano. Se guardan 10 ficheros por defecto, pudiéndose cambiar el menú de configuración.<p>")+
            self.trUtf8(u"<h3>Separador de pantalla</h3>")+            
            self.trUtf8(u"Existe un splitter entre los paneles de usuario y el tablero de parchís, que podrá ser movido según las preferencias del usuario. En algunas resoluciones de pantalla, al empezar el juego, el tablero aparece en negro hasta que se utiliza el splitter para darle el tamaño mínimo necesario.<p>")+
            self.trUtf8(u"<h3>Lanzamiento de dado</h3>")+                 
            self.trUtf8(u"Para tirar el dado se puede hacer click en el botón 'Tirar el dado' o hacer doble-click encima del tablero, cuando le toque a un jugador humano.<p>")+
            self.trUtf8(u"<h3>Vistas del tablero</h3>")+                 
            self.trUtf8(u"Se puede cambiar la vista del tablero pulsando la tecla 'm'.<p>")
        )

