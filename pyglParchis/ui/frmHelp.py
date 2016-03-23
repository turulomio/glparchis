 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
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
            self.tr("<h2>Historia</h2>")+
            self.tr("El juego del Parchís es una variación del Parchisi, un juego que tiene su origen en la India (Siglo XVI). Más información puede obtenerla en la <a href='http://es.wikipedia.org/wiki/Parchis'>Wikipedia</a>")+
            self.tr("<h2>Reglas de juego</h2>")+            
            self.tr("Hay muchas variantes del juego, dependiendo fundamentalmente del lugar en el que se juega. España ha sido uno de los países en los que más arraigo ha tenido el juego. Es por ello que glParchis utiliza las normas más comunes de juego en España")+
            self.tr("<h3>Reglas de juego en glParchis</h3>")+
            self.tr("Cada jugador dispone de 4 fichas que deberá mover por el tablero usando un dado y siguiendo un turno entre los distintos jugadores.<p>")+
            self.tr("Cada ficha partirá de una casilla inicial, de la que sólo podrá salir con un 5. Recorrerá una ruta con un número de casillas igual para todos los jugadores, que termina en una rampa de llegada de su color y una casilla final. Este movimiento lo realizará en sentido contrario a las agujas del reloj<p>")+
            self.tr("Existen unas casillas seguras (casillas con circulo gris), en las que dos fichas de distintos jugadores pueden convivir. En el resto (casillas blancas), la ficha que llega en segundo lugar come (manda a la casilla inicial) a la que llegó en primer lugar y obtiene el derecho de mover 20 casillas.<p>")+
            self.tr("Cuando una ficha llega a la casilla final, el jugador obtiene el derecho de mover 10 puntos.<p>")+
            self.tr("Cuando dos fichas del mismo color están en una misma casilla, se produce una barrera. Este hecho impide que el resto de jugadores puedan avanzar por ella. El jugador está obligado a abrir la barrera cuando obtiene un 6 con el dado.<p>")+
            self.tr("Cuando un jugador tiene todas sus fichas fuera de casa (casilla inicial) y obtiene un 6, contará 7 casillas de movimiento en el tablero.<p>")+
            self.tr("Cuando en la casilla de salida de un jugador hay dos fichas distintas y el jugador del mismo color de la casilla de salida saca un cinco y debe sacar una ficha, la última ficha que llegó se va a casa.<p>")+    
            self.tr("<h3>Puntuación</h3>")+
            self.tr("La puntuación viene dada por el número de casillas que le falta recorrer a los otros jugadores menos las que me faltan a mí. A esta cantidad se le suma la diferencia entre las fichas que he comido y las que me han comido, multiplicadas por 40.<p>")+        
            self.tr("<h2>Interfaz de usuario</h2>")+
            self.tr("<h3>Guardado automático</h3>")+            
            self.tr("La aplicación guarda automáticamente el estado de la partida cada vez que hay un turno de un jugador humano. Se guardan 10 ficheros por defecto, pudiéndose cambiar el menú de configuración.<p>")+
            self.tr("<h3>Separador de pantalla</h3>")+            
            self.tr("Existe un splitter entre los paneles de usuario y el tablero de parchís, que podrá ser movido según las preferencias del usuario. En algunas resoluciones de pantalla, al empezar el juego, el tablero aparece en negro hasta que se utiliza el splitter para darle el tamaño mínimo necesario.<p>")+
            self.tr("<h3>Lanzamiento de dado</h3>")+                 
            self.tr("Para tirar el dado se puede hacer click en el botón 'Tirar el dado' o hacer doble-click encima del tablero, cuando le toque a un jugador humano.<p>")+
            self.tr("<h3>Vistas del tablero</h3>")+                 
            self.tr("Se puede cambiar la vista del tablero pulsando la tecla 'm'.<p>")
        )
"""
Basics: Parcheesi is played with two dice and the goal of the game is to move each of your pawns home to the center space. The most popular Parcheesi boards in America have seventy-two spaces around the board, twelve of which are darkened safe spaces where a pawn cannot be captured.

Each player selects four pawns of the same color and places them in their “nest” or starting area. The game board should be positioned so that each player's nest is to their right hand. Pawns enter play onto the darkened space toward the left of their nest and continue counter-clockwise around the board to the home path directly in front of the player.

Each player rolls a die, highest roller goes first, play continues clockwise to the left. Each turn players throw both dice and use the values shown to move their pawns around the board. If an amount on one or both of the dice cannot be moved that amount is forfeited.

Entering Pawns: Five has a special value in entering pawns out of the nest where they begin the game. A player may enter a pawn only by throwing a total of five on the dice or if either of the dice shows a five. Each time a five is tossed, the player must enter a pawn when possible.

Capture: An opponent's pawn resting on a lighter, non-safe space can be captured by landing on the same space by the amount shown on either die. The captured pawn is sent back to its nest and the turn continues with playing of any additional values shown on the dice. Also, each time a player captures an opponent’s pawn that player is awarded twenty movement points that may be moved with any one pawn at the end of their turn. If the bonus movement amount cannot be used it is forfeited.

An opponent’s pawn on a darker safe space is not capturable except when a pawn is entering onto that space from its nest. In this case enter the pawn as usual and the opponent’s pawn is captured.

It is not possible to end a turn with a pawn resting on the same space as an opponent’s pawn, even on a safety space.

Blockade: Two of a player's pawns resting on the same space can form a blockade preventing all players from passing, including the blockading player’s pawns. The player whose pawns are blocking the path may keep them together for three turns or until there is no other pawn for that player to move. After three turns of blockading, at least one of the pawns must be moved on the fourth turn so that the two pawns rest on different spaces at end of the turn. If a player's move can't get beyond the blockade he can go as close as he wants. And he can win the game if he wants too.

Should a blockade occupy a player’s entry space, it will prevent that player from entering pawns into play.

It is not possible for a player to rest more than two pawns on the same space.

Doublet: When a doublet (doubles) is tossed, the player gains another roll of the dice. In addition, if all that player’s pawns are outside the nest, the values on reverse side of dice are also used. For example, a player who rolls 6-6 can also move 1-1 in any combination. Therefore, when a doublet is tossed, the player has a total of fourteen spaces to move one or more pawns.

Third consecutive doublet rolled in one turn is a penalty and pawns are not moved amount shown on dice. Player with three doublet penalty also removes their pawn closest to home, back to their nest and turn ends.

Home: The center home space can only be entered by exact throw of the die or dice. When a pawn enters the center space by exact count, that player is awarded ten movement points that may be moved with any one pawn still in play at the end of their turn. If the bonus movement amount cannot be used it is forfeit.

Each player has their own home path in front of them and may not enter another’s, so when a pawn is on its home path it can no longer be captured.

Winning: The first player to get all four pawns home wins, at which point the winner must yell "PARCHEESI"."""
