# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPlayList.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from PlayList import playlist
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

class Ui_AddPlaylist(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, AddPlaylist):
        AddPlaylist.setObjectName(_fromUtf8("AddPlaylist"))
        AddPlaylist.resize(400, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("download (1).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddPlaylist.setWindowIcon(icon)
        self.label = QtGui.QLabel(AddPlaylist)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(AddPlaylist)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 201, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(AddPlaylist)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(AddPlaylist)
        self.textEdit.setGeometry(QtCore.QRect(20, 170, 211, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(AddPlaylist)
        self.pushButton.setGeometry(QtCore.QRect(274, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.AddPlaylist)

        self.retranslateUi(AddPlaylist)
        QtCore.QMetaObject.connectSlotsByName(AddPlaylist)

    def AddPlaylist(self):

        name = self.lineEdit.text()
        des = self.textEdit.toPlainText()

        p = playlist(name,des)
        p.addToDatabase()

        self.p = PlayLists.Ui_Playlists()
        self.p.show()
        self.hide()

    def retranslateUi(self, AddPlaylist):
        AddPlaylist.setWindowTitle(_translate("AddPlaylist", "Musicly", None))
        self.label.setText(_translate("AddPlaylist", "Name", None))
        self.label_2.setText(_translate("AddPlaylist", "Description", None))
        self.pushButton.setText(_translate("AddPlaylist", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Ui_AddPlaylist()
    ui.show()
    sys.exit(app.exec_())

