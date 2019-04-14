import datetime
import uuid
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpServer
from glparchis.libmanagers import ObjectManager_With_Id
from glparchis.libglparchis import Mem4
from glparchis.libglparchistypes import TGameMode
import threading
## Class to manage server
class Server(QTcpServer):
    quit=pyqtSignal()
    def __init__(self, ip,  port):
        QTcpServer.__init__(self)
        self.ip=ip
        self.port=port
        self.games=ObjectManager_With_Id()
        self.players=ObjectManager_With_Id()
        self.listen(self.ip, self.port)
        self.newConnection.connect(self.on_newConnection)
        print(self.tr("The server is running on {}:{}").format(self.ip,  self.serverPort()))

    def on_newConnection(self):
        sock=self.nextPendingConnection()
        player=NetPlayer(sock, self)
        self.players.append(player)
#        player.start()
        print(self.status())
        
    def status(self):
        return """Server status
    - Connections: {}
    - Games: {}
""".format(self.players.length(), self.games.length())
        
    def close(self):
        self.close()

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
        return str(self.games.arr+["COSITA"])

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
        netplayer.sock.write(s2b(a))
        netplayer.sock.flush()
        netplayer.sock.waitForReadyRead()
        return netplayer.sock.readAll()

                
class NetPlayer:
    def __init__(self, sock,  server):
        self.sock=sock
        self.sock.readyRead.connect(self.readSocketData)
        self.sock.stateChanged.connect(self.on_stateChanged)
        self.server=server
        self.game=None #Assignes in Server.c2s_creategame
#        self.event=threading.Event()        
        self.destroy=False
        self.buffer=b""
        self.player=None #glparchis

    def on_stateChanged(self):
        print("on_stateChanged")
        print(self.sock.state())

    def readSocketData(self):
        self.buffer=self.sock.readAll().data()#To convert to bytes data    
        print("on readSocketData", self.buffer)
        data=b2s(self.buffer)
        if data.startswith("server_"):
            result=self.server.process_commands(b2s(self.buffer), self)
            print(result)
            self.sock.write(s2b(result))
            self.sock.flush()
        else:#Send command to Game
            result=self.game.process_commands(b2s(self.buffer), self)
            self.sock.write(s2b(result))
            self.sock.flush()
#void connectToHost(QString hostname, int port){
#    if(!m_pTcpSocket)
#{
#    m_pTcpSocket = new QTcpSocket(this);
#    m_pTcpSocket->setSocketOption(QAbstractSocket::KeepAliveOption,1);
#}
#connect(m_pTcpSocket,SIGNAL(readyRead()),SLOT(readSocketData()),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(error(QAbstractSocket::SocketError)),SIGNAL(connectionError(QAbstractSocket::SocketError)),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(stateChanged(QAbstractSocket::SocketState)),SIGNAL(tcpSocketState(QAbstractSocket::SocketState)),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(disconnected()),SLOT(onConnectionTerminated()),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(connected()),SLOT(onConnectionEstablished()),Qt::UniqueConnection);
#
#if(!(QAbstractSocket::ConnectedState == m_pTcpSocket->state())){
#    m_pTcpSocket->connectToHost(hostname,port, QIODevice::ReadWrite);
#}
#}
#
#Write:
#
#void sendMessage(QString msgToSend){
#QByteArray l_vDataToBeSent;
#QDataStream l_vStream(&l_vDataToBeSent, QIODevice::WriteOnly);
#l_vStream.setByteOrder(QDataStream::LittleEndian);
#l_vStream << msgToSend.length();
#l_vDataToBeSent.append(msgToSend);
#
#m_pTcpSocket->write(l_vDataToBeSent, l_vDataToBeSent.length());
#}
#
#Read:
#
#void readSocketData(){
#while(m_pTcpSocket->bytesAvailable()){
#    QByteArray receivedData = m_pTcpSocket->readAll();       
#}
#}


#
#    if(!m_pTcpSocket)
#{
#    m_pTcpSocket = new QTcpSocket(this);
#    m_pTcpSocket->setSocketOption(QAbstractSocket::KeepAliveOption,1);
#}
#connect(m_pTcpSocket,SIGNAL(readyRead()),SLOT(readSocketData()),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(error(QAbstractSocket::SocketError)),SIGNAL(connectionError(QAbstractSocket::SocketError)),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(stateChanged(QAbstractSocket::SocketState)),SIGNAL(tcpSocketState(QAbstractSocket::SocketState)),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(disconnected()),SLOT(onConnectionTerminated()),Qt::UniqueConnection);
#connect(m_pTcpSocket,SIGNAL(connected()),SLOT(onConnectionEstablished()),Qt::UniqueConnection);
#
#if(!(QAbstractSocket::ConnectedState == m_pTcpSocket->state())){
#    m_pTcpSocket->connectToHost(hostname,port, QIODevice::ReadWrite);
#}
#}


def socket_configuration(socket):
    socket.readyRead()


def socket_write(socket, message):
    socket.write(message, message.length())
#Write:
#
#void sendMessage(QString msgToSend){
#QByteArray l_vDataToBeSent;
#QDataStream l_vStream(&l_vDataToBeSent, QIODevice::WriteOnly);
#l_vStream.setByteOrder(QDataStream::LittleEndian);
#l_vStream << msgToSend.length();
#l_vDataToBeSent.append(msgToSend);
#
#m_pTcpSocket->write(l_vDataToBeSent, l_vDataToBeSent.length());
#}

def socket_read(socket, ):
    pass
#
#Read:
#
#void readSocketData(){
#while(m_pTcpSocket->bytesAvailable()){
#    QByteArray receivedData = m_pTcpSocket->readAll();       
#}
#}


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
