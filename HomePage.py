# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import PlayLists

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
        Form.resize(462, 328)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.PlaylistsButton = QtGui.QPushButton(Form)
        self.PlaylistsButton.setGeometry(QtCore.QRect(100, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PlaylistsButton.setFont(font)
        self.PlaylistsButton.setObjectName(_fromUtf8("PlaylistsButton"))

        self.PlaylistsButton.clicked.connect(self.viewPlaylist)

        self.ArtistsButton = QtGui.QPushButton(Form)
        self.ArtistsButton.setGeometry(QtCore.QRect(240, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ArtistsButton.setFont(font)
        self.ArtistsButton.setObjectName(_fromUtf8("ArtistsButton"))

        # self.ArtistsButton.clicked.connect(self.closeEvent)

        self.libraryButton = QtGui.QPushButton(Form)
        self.libraryButton.setGeometry(QtCore.QRect(240, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.libraryButton.setFont(font)
        self.libraryButton.setObjectName(_fromUtf8("libraryButton"))
        self.AlbumsButton = QtGui.QPushButton(Form)
        self.AlbumsButton.setGeometry(QtCore.QRect(100, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AlbumsButton.setFont(font)
        self.AlbumsButton.setObjectName(_fromUtf8("AlbumsButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 250, 491, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Handwriting"))
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def viewPlaylist(self):
        self.p = PlayLists.Ui_Playlists()
        self.p.show()

    def closeEvent(self,event):
        import sys
        print("exit")
        sys.exit()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Musicly", None))
        self.PlaylistsButton.setText(_translate("Form", "Playlists", None))
        self.ArtistsButton.setText(_translate("Form", "Artists", None))
        self.libraryButton.setText(_translate("Form", "Library ", None))
        self.AlbumsButton.setText(_translate("Form", "Albums", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff007f;\">“One good thing about music, when it hits you, you feel no pain.” </span></p><p><span style=\" font-size:9pt; color:#ff007f;\">― Bob Marley</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())

