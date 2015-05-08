#main.py

from PyQt4 import QtGui, QtCore
import sys
#import main_layout
import qtlayout
import threading

lock = threading.Lock()

app = QtGui.QApplication(sys.argv)

#user = qtlayout.clientThread()
#user.my_start()

#win = main_layout.Window()
win = qtlayout.Window()
win.show()

#user.rec_sin.connect(win.layout_disp)
#win.sin.connect(user.send)


sys.exit(app.exec_())