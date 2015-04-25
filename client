__author__ = 'Administrator'
import socket
from PyQt4 import QtCore
import struct
import threading


class clientThread(threading.Thread,QtCore.QObject):
    rec_sin = QtCore.pyqtSignal(list)

    def __init__(self, lock):
        super(clientThread, self).__init__()
        # host = socket.gethostbyaddr()
        host = socket.gethostname()
        port = 9999
        self.lock = lock
        self.receive_msg = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

    def run(self):
        while self.is_alive():
            while True:
                if self.lock.acquire():
                    print('The client has acquired the lock')
                    signal = struct.unpack('b', self.s.recv(1))
                    if signal == 2:
                        self.receive()
                    self.lock.release()

    def send(self, heading, msg):
        print('The client is sending data to the server')
        heading = struct.pack('bbb', heading[0], heading[1], heading[2])
        content = msg.pop(0)
        content = content.encode('ascii')
        self.s.send(heading)
        self.s.send(content)

    def receive(self):
        print('The client is receiving data from the server')
        self.heading = struct.unpack('bbb', self.s.recv(3))
        length = self.heading[1]
        self.data = self.s.recv(length)
        self.data = self.data.decode('ascii')
        self.receive_msg.append(self.data)
        self.rec_sin.emit(self.receive_msg)

    def close(self):
        self.s.close()

