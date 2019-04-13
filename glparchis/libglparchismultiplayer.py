from PyQt5.QtCore import QObject
import datetime
import socket
import uuid
from glparchis.libmanagers import ObjectManager_With_Id
from glparchis.libglparchis import Mem4
from _thread import start_new_thread


## Class to manage server
class Server():
    def __init__(self):
        self.games=ObjectManager_With_Id()
        self.players=ObjectManager_With_Id()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        

        server = '127.0.0.1'
        port = 65432

        try:
            self.socket.bind((server, port))

        except socket.error as e:
            print(str(e))

        self.socket.listen(2)
        print("Waiting for a connection")
        while True:
            conn, addr = self.socket.accept()
            print("Connected to: ", addr)
            player=ServerPlayer(conn)
            self.players.append(player)

            start_new_thread(self.threaded_client, (player,))
        
        
    def generate_tockent(self):
        return str(datetime.datetime.now())
    
    def threaded_client(self, player):
        def mem2bytes(mem):
            mem.save("/tmp/glparchis.glparchis")
            return open("/tmp/glparchis.glparchis").read()
        print("threaded_client")
        data=b2list(player.socket.recv(1024))
        if data[0]=="creategame":
            game=ServerGame(data[1])
            player.socket.send(s2b("gamecreated {}\n".format(game.id)))
            b2list(player.socket.recv(1024))#OK
            player.socket.send(s2b("gameuserid {}_{}\n".format(game.id, game.assign_id())))
            b2list(player.socket.recv(1024))#OK
            player.socket.send(s2b("gamestart\n"))
            b2list(player.socket.recv(1024))#OK
            mem=Mem4()                     
            mem.jugadores.actual=mem.jugadores.arr[0]
            mem.playedtime=datetime.datetime.now()
            for j in mem.jugadores.arr:
                j.name=str("Jug")
                j.fichas.arr[0].mover(0, False,  True)
                j.fichas.arr[1].mover(0, False,  True)
                j.fichas.arr[2].mover(0, False,  True)
                j.fichas.arr[3].mover(0, False,  True)
            mem.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
            mem.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
            player.socket.send(s2b("status {}\n".format(mem2bytes(mem))))
            player.socket.send(s2b("yourturn\n"))
            b2list(player.socket.recv(1024))#OK
#            ## Ahora recibe interacciones del juego luego se pone a escuchar
#            while needServer==False:
        elif data[0]=="joingame":
            print ("Not developped yet")
                
        
        
    def close(self):
        self.socket.close()



## Class to manage a 
class ServerGame:
    def __init__(self, numplayers):
        self.id=uuid.uuid4()
        self.numplayers=numplayers
        self.start=datetime.datetime.now()
        
    def assign_id(self):
        return 1

## Class to manage server
class ServerPlayerManager(ObjectManager_With_Id):
    def __init__(self):
        ObjectManager_With_Id.__init__(self)

                
class ServerPlayer(QObject):
    def __init__(self, socket):
        QObject.__init__(self)
        self.id=None
        self.ia=None
        self.socket=socket
        
def b2list(data):
    data=data.replace(b"\n", b"")
    return data.decode("UTF-8").split(" ")

def s2b(data):
    return data.encode("UTF-8")
