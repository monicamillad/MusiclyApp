# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlaylistView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3

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

class Ui_PlaylistView(QtGui.QWidget):

    def __init__(self,playlistname):
        self.playlistname = playlistname
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, PlaylistView):
        PlaylistView.setObjectName(_fromUtf8("PlaylistView"))
        PlaylistView.resize(391, 321)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlaylistView.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(PlaylistView)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(PlaylistView)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 371, 301))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(self.playlistname))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        conn = sqlite3.connect('MusiclyApp.db')
        cursor = conn.execute("SELECT description from playlist WHERE ( name = '" +self.playlistname+"') ;")
        des = cursor.fetchone()

        self.label_2.setText(_fromUtf8(des[0]))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        cursor2 = conn.execute("SELECT song from songinplaylist WHERE ( playlist = '" +self.playlistname+"') ;")

        font = QtGui.QFont()
        font.setPointSize(8)

        for r in cursor2:
            self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.label_3.setFont(font)
            self.label_3.setText("* " + r[0])
            self.verticalLayout.addWidget(self.label_3)

            cursor2 = conn.execute("SELECT lenght from song WHERE ( name = '" + r[0] + "') ;")
            r1 = cursor2.fetchone()

            self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.label_4.setFont(font)
            self.label_4.setText("Duration: " + r1[0])
            self.verticalLayout_2.addWidget(self.label_4)

        self.retranslateUi(PlaylistView)
        QtCore.QMetaObject.connectSlotsByName(PlaylistView)


    def closeEvent(self,event):
        self.hide()

    def retranslateUi(self, PlaylistView):
        PlaylistView.setWindowTitle(_translate("PlaylistView", "Musicly", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_PlaylistView()
    ui.show()
    sys.exit(app.exec_())

