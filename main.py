#main.py

from PyQt4 import QtGui, QtCore
import sys
import main_layout
import client
import threading

lock = threading.Lock()

app = QtGui.QApplication(sys.argv)

user = client.clientThread(lock)
user.start()

win = main_layout.Window()
win.show()

user.rec_sin.connect(win.layout_disp)
win.sin.connect(user.send)

thread_client = client.client()
sys.exit(app.exec_())