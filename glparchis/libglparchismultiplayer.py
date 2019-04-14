import datetime
import uuid
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpServer
from glparchis.libmanagers import ObjectManager_With_Id
from glparchis.libglparchis import Mem4
from glparchis.libglparchistypes import TGameMode
from glparchis.functions import s2b, command_split, bytes2bool
import threading

## Class to manage server
class Server(QTcpServer):
    quit=pyqtSignal()
    def __init__(self, ip,  port):
        QTcpServer.__init__(self)
        self.ip=ip
        self.port=port
        self.games=ObjectManager_With_Id()
        self.sockets=ObjectManager_With_Id()
        self.listen(self.ip, self.port)
        self.newConnection.connect(self.on_newConnection)
        print(self.tr("The server is running on {}:{}").format(self.serverAddress().toString(),  self.serverPort()))

    def find_game_from_socket(self, o):
        for game in self.games.arr:
            for socket in game.sockets.arr:
                if socket==o:
                    return game
        return None

    def on_newConnection(self):
        sock=self.nextPendingConnection()
        self.sockets.append(sock)
        sock.readyRead.connect(lambda: self.readSocketData(sock))# From https://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot/
        sock.stateChanged.connect(lambda: self.on_stateChanged(sock))
        print(self.status())
    
    def on_stateChanged(self, sock):
        pass
        #        print(sock.state())

    def readSocketData(self, sock):
        buffer=sock.readAll().data()#To convert to bytes data    
        (command, args)=command_split(buffer)
        
        if command=="server_creategame":
            self.c2s_creategame(command, args[1], args[2:],  sock)
        elif command=="server_listgames":
            self.c2s_listgames(command, sock)            
        elif command=="display":
            self.send_display(command, args, sock)
        elif command=="startgame":
            game=self.find_game_from_socket(sock)
            game.start()
        else:
            print ("COMMAND NOT FOUND")

    def status(self):
        return """Server status
    - Connections: {}
    - Games: {}
""".format(self.sockets.length(), self.games.length())
        
    def close(self):
        self.close()

    def c2s_creategame(self, command, mode, arrPlays, sock):
        game=Game(mode, self)
        game.owner=sock
        game.sockets.append(sock)
        self.games.append(game)
        sock.write(s2b("True"))
        sock.flush()
        
    def c2s_listgames(self, command, sock):
        r=str(self.games.arr+["COSITA"])
        sock.write(s2b(r))
        sock.flush()

    def send_display(self, sock):
        game=self.find_game_from_socket(sock)
        a="display "+ game.mem.mem2bytes()
        sock.write(s2b(a))
        sock.flush()
        sock.waitForReadyRead()
        sock.readAll()
        
    def send_must_throw(self, sock):
        sock.write(b"must_throw")
        sock.flush()
        sock.waitForReadyRead()
        return bytes2bool(sock.readAll())
        

## Class to manage a 
class Game(threading.Thread):
    def __init__(self, numplayers, server):
        threading.Thread.__init__(self)
        self.id=uuid.uuid4()
        self.sockets=ObjectManager_With_Id()
        self.owner=None#socket
        self.mem=None
        self.mode=None
        self.server=server

    ##Has the main loop of the game until it's  finished
    def start(self):
        self.mem=Mem4()
        self.mode=TGameMode.Four
        self.mem.jugadores.actual=self.mem.jugadores.arr[0]
        self.mem.playedtime=datetime.datetime.now()
        for j in self.mem.jugadores.arr:
            j.name=str("Jug")
            j.fichas.arr[0].mover(0, False,  True)
            j.fichas.arr[1].mover(0, False,  True)
            j.fichas.arr[2].mover(0, False,  True)
            j.fichas.arr[3].mover(0, False,  True)
        self.mem.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
        self.mem.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
        
        #Assigns network player to game players, not all players have netplayer. None if it hasn't.
        for i in range(self.sockets.length()):
            self.mem.jugadores.arr[i].sock=self.sockets.arr[i]
        
        self.server.send_display(self.mem.jugadores.actual.sock)
        
        print("Sending must throw")
        self.server.send_must_throw(self.mem.jugadores.actual.sock)
        
        print("Quiting")
        self.server.quit.emit()

