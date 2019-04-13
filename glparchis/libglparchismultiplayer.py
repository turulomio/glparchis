import datetime
import socket
import uuid
import json
from glparchis.libmanagers import ObjectManager_With_Id
from glparchis.libglparchis import Mem4
from glparchis.libglparchistypes import TGameMode
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
            player=NetPlayer(conn, self)
            self.players.append(player)
            player.start()

    def status(self):
        return """Server status
    - Connections: {}
    - Games: {}
""".format(self.players.length(), self.games.length())
        
    def close(self):
        self.socket.close()

    def process_commands(self, s, netplayer):
        (command, args)=command_split(s)
        print(s, command,  args)
        if command=="server_creategame":
            a= self.c2s_creategame(command, args[1], args[2:],  netplayer)
            print(a)
            return (a)
        elif command=="server_listgames":
            return self.c2s_listgames(command, netplayer)
            
    def c2s_creategame(self, command, mode, arrPlays, netplayer):
        game=Game(mode)
        game.owner=netplayer
        netplayer.game=game
        game.players.append(netplayer)
        self.games.append(game)
        return "OK"
        
    def c2s_listgames(self, command, netplayer):
        return str(self.games.arr)

## Class to manage a 
class Game(threading.Thread):
    def __init__(self, numplayers):
        threading.Thread.__init__(self)
        self.id=uuid.uuid4()
        self.players=ObjectManager_With_Id()
        self.owner=None
        self.mem=None
        self.mode=None

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
        for i in range(self.players.length()):
            self.players.arr[i].player=self.mem.jugadores.arr[i]
            self.mem.jugadores.arr[i].netplayer=self.players.arr[i]
            print(self.mem.jugadores.arr[i],  self.mem.jugadores.arr[i].netplayer, self.players.arr[i])
         
        print("Game created")
        
        
        print("Updating display")
        self.g2c_display(self.mem.jugadores.actual.netplayer)
        
#
#        self.mem.jugadores.actual.netplayer.sock.send(s2b("gamecreated {}\n".format(self.game.id)))
#        b2list(self.sock.recv(1024))#OK
#        self.sock.send(s2b("gameuserid {}_{}\n".format(self.game.id, "MAL")))
#        b2list(self.sock.recv(1024))#OK
#        self.sock.send(s2b("gamestart\n"))
#        b2list(self.sock.recv(1024))#OK
            
            
    def process_commands(self, s,  netplayer):
        (command, args)=command_split(s)
        print(s, command, args)
        if command=="display":
            return self.g2c_status(command, args, netplayer)
        elif command=="startgame":
            self.start()
            return "OK"
        print ("GAME COMMAND NOT FOUND")

    def g2c_display(self, netplayer):
        a="display "+ self.mem.mem2bytes()
        print(a)
        netplayer.sock.send(s2b(a))
        netplayer.sock.recv(1024)#ok


## Class to manage server
class NetPlayerManager(ObjectManager_With_Id):
    def __init__(self):
        ObjectManager_With_Id.__init__(self)

                
class NetPlayer(threading.Thread):
    def __init__(self, sock,  server):
        threading.Thread.__init__(self)
        self.sock=sock
        self.server=server
        self.game=None #Assignes in Server.c2s_creategame
#        self.event=threading.Event()        
        self.destroy=False
        self.buffer=b""
        self.player=None #glparchis


    ## Commands from clients to server
    ## - creategame maxplayers True* players: Creates a game and returns the uuid
    ## - gamestart: Creates a game. returns the id of the player. and create virtual players
    def run(self):
        while self.destroy==False:
            print("Esperando",  self)
            self.buffer=self.sock.recv(1024)
            data=b2s(self.buffer)
            if data.startswith("server_"):
                result=self.server.process_commands(b2s(self.buffer), self)
                self.sock.send(s2b(result))
            else:#Send command to Game
                result=self.game.process_commands(b2s(self.buffer), self)
                self.sock.send(s2b(result))
                    
def b2list(data):
    data=data.replace(b"\n", b"")
    return data.decode("UTF-8").split(" ")

def s2b(data):
    return data.encode("UTF-8")
def b2s(data):
    return data.decode("UTF-8")
    
def command_split(s):
        arr=s.split(" ")
        return (arr[0], arr[1:])
    
class MemDisplay:
    def __init__(self, host,  port):
        self.BUFSIZ=2048
        self.host=host
        self.port=port
        self.status=None
        self.display=False
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        # Connect to server and send data
        print("Asking listgames")
        print(self.c2s_listgames())
        print("Asking creategame")
        print(self.c2s_creategame(TGameMode.Four, True, True, True, True))
        print("Asking startgame")
        print(self.c2s_startgame())
        while True:
            print("Cliente esperando")
            try:
                buffer=self.sock.recv(self.BUFSIZ)
                print(buffer)
                command, args=command_split(buffer.replace(b"\n", b""))
                if command=="display":
                    self.s2c_update_display(command, args)
            except OSError:  # Possibly client has left the chat.
                print("Error in client")
                break
    
    def s2c_update_display(self, command, stream,  wait=200):
        self.status = json.loads(stream)
        print("display",  self.status)
        self.sock.send(s2b("OK\n"))

    def c2s_creategame(self, mode, *arrPlays):
        self.sock.send(s2b("server_creategame {} True True True True".format(TGameMode.Four)))
        self.sock.recv(self.BUFSIZ)#OK
        return "OK"
        
    def c2s_startgame(self):
        self.sock.send(s2b("startgame"))
        self.sock.recv(self.BUFSIZ)#OK
        return "OK"

    def c2s_listgames(self):
        self.sock.send(s2b("server_listgames"))
        lists=self.sock.recv(self.BUFSIZ)
        return lists
