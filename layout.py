# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ying\DHPP\layout.ui'
#
# Created: Mon Apr 20 20:54:50 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.setWindowModality(QtCore.Qt.NonModal)
        dialog.resize(615, 503)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(dialog)
        self.widget.setGeometry(QtCore.QRect(1, 1, 611, 501))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.disp = QtGui.QTextEdit(self.widget)
        self.disp.setObjectName(_fromUtf8("disp"))
        self.verticalLayout.addWidget(self.disp)
        self.inp = QtGui.QTextEdit(self.widget)
        self.inp.setObjectName(_fromUtf8("inp"))
        self.verticalLayout.addWidget(self.inp)
        self.send = QtGui.QPushButton(self.widget)
        self.send.setObjectName(_fromUtf8("send"))
        self.verticalLayout.addWidget(self.send)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.user1 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user1.sizePolicy().hasHeightForWidth())
        self.user1.setSizePolicy(sizePolicy)
        self.user1.setText(_fromUtf8(""))
        self.user1.setScaledContents(True)
        self.user1.setObjectName(_fromUtf8("user1"))
        self.verticalLayout_2.addWidget(self.user1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "DHPP", None))
        self.send.setText(_translate("dialog", "send", None))

