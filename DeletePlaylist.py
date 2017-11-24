# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeletePlaylist.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt4 import QtCore, QtGui

import PlayLists
from PlayList import playlist

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

class Ui_DeletePlaylist(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, DeletePlaylist):
        DeletePlaylist.setObjectName(_fromUtf8("DeletePlaylist"))
        DeletePlaylist.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeletePlaylist.setWindowIcon(icon)
        self.label = QtGui.QLabel(DeletePlaylist)
        self.label.setGeometry(QtCore.QRect(10, 20, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(DeletePlaylist)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 191, 61))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(DeletePlaylist)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.deleteplaylist)

        self.retranslateUi(DeletePlaylist)
        QtCore.QMetaObject.connectSlotsByName(DeletePlaylist)

    def deleteplaylist(self):

        pl = self.lineEdit.text()

        conn = sqlite3.connect('MusiclyApp.db')
        cursor = conn.execute("SELECT name from playlist ;")

        k = False

        for r in cursor:

            if r[0]==pl:
                k = True
                break

        if k==True:
            pl = playlist(pl)
            pl.DeletePlaylist()

            choice = self.msg = QtGui.QMessageBox.information(self,"Notification !","The Playlist has been deleted successfully !",QtGui.QMessageBox.Ok)

            if choice == QtGui.QMessageBox.Ok:
                self.p = PlayLists.Ui_Playlists()
                self.p.show()
                self.hide()

        else:

            choice = self.msg = QtGui.QMessageBox.question(self,"Question ?","This Playlist does not exist,\n Do you want to try again ?!",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if choice==QtGui.QMessageBox.No:
                self.p = PlayLists.Ui_Playlists()
                self.p.show()
                self.hide()

    def retranslateUi(self, DeletePlaylist):
        DeletePlaylist.setWindowTitle(_translate("DeletePlaylist", "Musicly", None))
        self.label.setText(_translate("DeletePlaylist", "<html><head/><body><p>Enter the name of the playlist </p><p>you want to delete here !</p></body></html>", None))
        self.pushButton.setText(_translate("DeletePlaylist", "Delete", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_DeletePlaylist()
    ui.show()
    sys.exit(app.exec_())

