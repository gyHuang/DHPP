__author__ = 'Administrator'
import socket
from PyQt4 import QtCore
import struct
from PyQt4.QtCore import QThread


class clientThread(QThread):
    rec_sin = QtCore.pyqtSignal(list)

    def __init__(self):
        super(clientThread, self).__init__()
        # host = socket.gethostbyaddr()
        host = socket.gethostname()
        port = 9999
        self.receive_msg = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.is_run = False

    def my_start(self):
        self.is_run = True
        self.start()

    def my_stop(self):
        self.is_run = False

    def run(self):
        while self.is_run:
            while True:
                print('The client''s run function')
                signal = struct.unpack('b', self.s.recv(1))
                print(signal[0])
                if signal[0] == 2:
                    self.receive()

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

