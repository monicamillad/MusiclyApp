# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Playlists.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt4 import QtCore, QtGui

import AddPlayList
import DeletePlaylist
import HomePage

import PickPlaylist
# from PickPlaylist import Ui_Form

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

class Ui_Playlists(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Playlists):
        Playlists.setObjectName(_fromUtf8("Playlists"))
        Playlists.resize(502, 434)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Playlists.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Playlists)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Playlists)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 482, 414))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.backButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setObjectName(_fromUtf8("backButton"))

        self.backButton.clicked.connect(self.backtohome)

        self.gridLayout_2.addWidget(self.backButton, 0, 3, 1, 1)
        self.deletePlaylistButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deletePlaylistButton.setFont(font)
        self.deletePlaylistButton.setObjectName(_fromUtf8("deletePlaylistButton"))

        self.deletePlaylistButton.clicked.connect(self.deleteplaylist)

        self.gridLayout_2.addWidget(self.deletePlaylistButton, 1, 3, 1, 1)
        self.addPlaylistButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addPlaylistButton.setFont(font)
        self.addPlaylistButton.setObjectName(_fromUtf8("addPlaylistButton"))

        self.addPlaylistButton.clicked.connect(self.addplaylistview)

        self.gridLayout_2.addWidget(self.addPlaylistButton, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        self.viewPlylistButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.viewPlylistButton.setFont(font)
        self.viewPlylistButton.setObjectName(_fromUtf8("viewPlylistButton"))

        self.viewPlylistButton.clicked.connect(self.viewpickplaylist)

        self.gridLayout_2.addWidget(self.viewPlylistButton, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2.addLayout(self.verticalLayout_2, 4, 3, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2.addLayout(self.verticalLayout, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        conn = sqlite3.connect('MusiclyApp.db')
        cursor = conn.execute("SELECT name from playlist ;")

        font = QtGui.QFont()
        font.setPointSize(9)

        for row in cursor:
            self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.label_2.setText("* "+row[0])
            self.label_2.setFont(font)
            self.verticalLayout.addWidget(self.label_2)

            cursor2 = conn.execute("SELECT COUNT(*) from songinplaylist WHERE ( playlist = '" +row[0]+"') ;")
            num = cursor2.fetchone()

            self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.label_3.setText("tracks: " + num[0].__str__())
            self.label_3.setFont(font)
            self.verticalLayout_2.addWidget(self.label_3)


        self.retranslateUi(Playlists)
        QtCore.QMetaObject.connectSlotsByName(Playlists)

    def deleteplaylist(self):
        self.d = DeletePlaylist.Ui_DeletePlaylist()
        self.d.show()
        self.hide()

    def addplaylistview(self):
        self.a = AddPlayList.Ui_AddPlaylist()
        self.a.show()
        self.hide()

    def viewpickplaylist(self):
        self.p = PickPlaylist.Ui_Form()
        self.p.show()
        self.hide()

    def backtohome(self):
        self.hide()

    def closeEvent(self, event):
        self.hide()

    def retranslateUi(self, Playlists):
        Playlists.setWindowTitle(_translate("Playlists", "Musicly", None))
        self.backButton.setText(_translate("Playlists", "Back To Home", None))
        self.deletePlaylistButton.setText(_translate("Playlists", "Delete Playlist", None))
        self.addPlaylistButton.setText(_translate("Playlists", "Add Playlist", None))
        self.label.setText(_translate("Playlists", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Playlists : </span></p></body></html>", None))
        self.viewPlylistButton.setText(_translate("Playlists", "View Playlist", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Playlists()
    ui.show()
    sys.exit(app.exec_())

