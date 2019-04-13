from PyQt5.QtCore import QObject
import datetime
import socket
from glparchis.libmanagers import ObjectManager_With_Id
from _thread import start_new_thread


## Class to manage server
class Server(ObjectManager_With_Id):
    def __init__(self):
        ObjectManager_With_Id.__init__(self)
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
            self.append(ServerPlayer(conn))

            start_new_thread(self.threaded_client, (conn,))
        
    def threaded_client(self, conn):
        print("threaded_client")
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

    def close(self):
        self.socket.close()


## Class to manage a 
class ServerGame:
    def __init__(self):
        self.id=None
        self.start=datetime.datetime.now()

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
