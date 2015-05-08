__author__ = 'Administrator'

import socket
from PyQt4 import QtCore, QtNetwork, QtGui


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon('user1.png'))
        self.setWindowTitle('DHPP')
        self.send_msg = []
        self.resize(500, 400)
        self.receiver = 0
        self.header = [0, 0, 0]
        self.initUI()
        self.heading = None
        host = socket.gethostname()
        port = 9999
        # host = '158.132.11.182'
        # port = 25002
        self.receive_msg = []
        self.s = QtNetwork.QTcpSocket(self)
        self.s.readyRead.connect(self.receive)
        self.s.connectToHost(host, port)


    def initUI(self):
        self.button = QtGui.QPushButton('Send')
        self.friend = QtGui.QPushButton('Friend')
        self.myid = QtGui.QPushButton('My id')
        self.con = QtGui.QPushButton('Connect')
        self.inp = QtGui.QLineEdit()
        self.disp = QtGui.QLabel()
        self.instruction = QtGui.QLabel(
            'Instruction:\n "My id":get your own id;\n "Friend":get all the friends on line;\n "Connect":get connection to the friend you type in the editor;\n "Send":send the message to the friend you just connected.')

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.friend)
        hbox.addWidget(self.myid)
        hbox.addWidget(self.con)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.instruction)
        vbox.addWidget(self.disp)
        vbox.addWidget(self.inp)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.layout_send)
        self.connect(self.friend, QtCore.SIGNAL('clicked()'), self.layout_send)
        self.connect(self.myid, QtCore.SIGNAL('clicked()'), self.layout_send)
        self.connect(self.con, QtCore.SIGNAL('clicked()'), self.layout_send)


    def layout_send(self):
        print('The layout is sending data to the client')

        sender = self.sender()
        msg = ''

        if sender == self.button:
            msg = self.inp.text()
            self.header = [3, len(msg), self.receiver]

        elif sender == self.con:
            msg = self.inp.text()
            self.receiver = int(msg)
            self.header = [2, len(msg), 0]

        elif sender == self.friend:
            msg = ''
            self.header = [1, len(msg), 0]

        elif sender == self.myid:
            msg = ''
            self.header = [0, len(msg), 0]

        self.send_msg.append(msg)

        print('The client is sending data to the server')
        block = QtCore.QByteArray()

        out = QtCore.QDataStream(block, QtCore.QIODevice.WriteOnly)
        out.setVersion(QtCore.QDataStream.Qt_4_0)

        content = self.send_msg.pop(0)
        content = bytes(content, encoding='ascii')
        self.header[1] = len(content)
        out.writeUInt16(self.header[0])
        out.writeUInt16(self.header[1])
        out.writeUInt16(self.header[2])
        out.writeRawData(content)
        self.s.write(block)


    def layout_disp(self, receive_msg):
        print('The layout is displaying data')
        self.disp.setText(receive_msg.pop(0))



        # import sys

        # app = QtGui.QApplication(sys.argv)

        # win = Window()
        # win.show()

        # sys.exit(app.exec_())


    def receive(self):
        print('The client is receiving data from the server')
        instr = QtCore.QDataStream(self.s)
        instr.setVersion(QtCore.QDataStream.Qt_4_0)


        if self.heading == None:
            print('initialize the heading')
            if self.s.bytesAvailable() < 6:
                return
            self.heading = [0,0,0]
            self.heading[0] = instr.readUInt16()
            self.heading[1] = instr.readUInt16()
            self.heading[2] = instr.readUInt16()
            print('receive the message',str(self.heading))
        if self.s.bytesAvailable() < self.heading[1]:
            return



        self.data = instr.readRawData(self.heading[1])
        print(self.data)
        self.data = self.data.decode("ascii")
        print(self.data)
        self.receive_msg.append(self.data)
        self.layout_disp(self.receive_msg)
        self.heading = None