__author__ = 'Administrator'

from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    sin = QtCore.pyqtSignal(list, list)


    def __init__(self):
        super(Window, self).__init__()
        self.setWindowIcon(QtGui.QIcon('user1.png'))
        self.setWindowTitle('DHPP')
        self.send_msg = []
        self.resize(500, 400)
        self.receiver = 0
        self.header = [0, 0, 0]
        self.initUI()


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
        self.sin.emit(self.header, self.send_msg)


    def layout_disp(self, receive_msg):
        print('The layout is displaying data')
        self.disp.setText(receive_msg.pop(0))



        # import sys

        # app = QtGui.QApplication(sys.argv)

        # win = Window()
        # win.show()

        # sys.exit(app.exec_())