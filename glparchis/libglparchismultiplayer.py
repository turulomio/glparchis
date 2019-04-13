from PyQt5.QtCore import QObject
import datetime
import socket
import uuid
from glparchis.libmanagers import ObjectManager_With_Id
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
        print("threaded_client")
        data=b2list(player.socket.recv(1024))
        if data[0]=="creategame":
            game=ServerGame(data[1])
            player.socket.send(s2b("gamecreated {}\n".format(game.id)))
            ok=b2list(player.socket.recv(1024))
            player.socket.send(s2b("gameuserid {}_{}\n".format(game.id, game.assign_id())))
            ok=b2list(player.socket.recv(1024))
            player.socket.send(s2b("gamestart\n"))
            ok=b2list(player.socket.recv(1024))
#            ## Ahora recibe interacciones del juego luego se pone a escuchar
#            while needServer==False:
                
        
        
    def close(self):
        self.socket.close()
#        conn.send(str.encode(currentId))
#        currentId = "1"
#        reply = ''
#        while True:
#            try:
#                data = conn.recv(2048)
#                reply = data.decode('utf-8')
#                if not data:
#                    conn.send(str.encode("Goodbye"))
#                    break
#                else:
#                    print("Recieved: " + reply)
#                    arr = reply.split(":")
#                    id = int(arr[0])
#                    pos[id] = reply
#
#                    if id == 0: nid = 1
#                    if id == 1: nid = 0
#
#                    reply = pos[nid][:]
#                    print("Sending: " + reply)
#
#                conn.sendall(str.encode(reply))
#            except:
#                break



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
