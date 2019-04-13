import datetime
import socket
import uuid
from glparchis.libmanagers import ObjectManager_With_Id
from glparchis.libglparchis import Mem4
import threading
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
            player=ServerPlayer(conn, self)
            self.players.append(player)
            player.start()

    def status(self):
        return """Server status
    - Connections: {}
    - Games: {}
""".format(self.players.length(), self.games.length())
        
    def close(self):
        self.socket.close()



## Class to manage a 
class ServerGame:
    def __init__(self, numplayers):
        self.id=uuid.uuid4()
        self.numplayers=numplayers
        self.players=ObjectManager_With_Id()
        self.start=datetime.datetime.now()
        
    def assign_id(self):
        return 1

## Class to manage server
class ServerPlayerManager(ObjectManager_With_Id):
    def __init__(self):
        ObjectManager_With_Id.__init__(self)

                
class ServerPlayer(threading.Thread):
    def __init__(self, sock,  server):
        threading.Thread.__init__(self)
        self.sock=sock
        self.server=server
        self.event=threading.Event()        
        self.destroy=False
        self.mode="s"#puede ser s send o r receive.
        self.buffer=b""
    
    def send(self, buffer):
        self.mode
        pass
        
    def receive(self):
        pass

    def run(self):
        while self.destroy==False:
            print("Esperando",  self)
            self.buffer=self.sock.recv(1024)
            data=b2list(self.buffer)
            if data[0]=="creategame":
                game=ServerGame(data[1])
                self.server.games.append(game)
                self.sock.send(s2b("OK\n"))
                self.sock.send(s2b("gamecreated {}\n".format(game.id)))
                b2list(self.sock.recv(1024))#OK
                self.sock.send(s2b("gameuserid {}_{}\n".format(game.id, game.assign_id())))
                b2list(self.sock.recv(1024))#OK
                self.sock.send(s2b("gamestart\n"))
                b2list(self.sock.recv(1024))#OK
                game.mem=Mem4()                     
                game.mem.jugadores.actual=game.mem.jugadores.arr[0]
                game.mem.playedtime=datetime.datetime.now()
                for j in game.mem.jugadores.arr:
                    j.name=str("Jug")
                    j.fichas.arr[0].mover(0, False,  True)
                    j.fichas.arr[1].mover(0, False,  True)
                    j.fichas.arr[2].mover(0, False,  True)
                    j.fichas.arr[3].mover(0, False,  True)
                game.mem.jugadores.actual.movimientos_acumulados=None#Comidas ymetidas
                game.mem.jugadores.actual.LastFichaMovida=None #Se utiliza cuando se va a casa
                self.sock.send(s2b("status {}\n".format(game.mem.mem2bytes())))
                self.sock.send(s2b("yourturn\n"))
                b2list(self.sock.recv(1024))#OK
            elif data[0]=="listgames":
                game=ServerGame(data[1])
                self.sock.send(s2b(str(self.server.games.arr)))
            print(self.server.status())
                    
def b2list(data):
    data=data.replace(b"\n", b"")
    return data.decode("UTF-8").split(" ")

def s2b(data):
    return data.encode("UTF-8")
