# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PickPlaylist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt4 import QtCore, QtGui

import PlaylistView
# from PlaylistView import Ui_PlaylistView

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

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 181, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        # self.pushButton = QtGui.QPushButton(Form)
        # self.pushButton.setGeometry(QtCore.QRect(320, 230, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        # self.pushButton.setFont(font)
        # self.pushButton.setObjectName(_fromUtf8("pushButton"))

        conn = sqlite3.connect('MusiclyApp.db')
        cursor = conn.execute("SELECT name from playlist ;")

        for r in cursor:
            self.comboBox.addItem(r[0])

        self.comboBox.activated[str].connect(self.pick)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def pick(self,text):
        self.p = PlaylistView.Ui_PlaylistView(text)
        self.p.show()
        self.hide()

    def closeEvent(self,event):
        self.hide()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Musicly", None))
        self.label.setText(_translate("Form", "Pick a Playlist !", None))
        # self.pushButton.setText(_translate("Form", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

