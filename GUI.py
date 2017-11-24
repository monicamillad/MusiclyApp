import sys
from PyQt4 import QtGui, QtCore
from PyQt4 import Qt
from PyQt4.QtGui import QWidget

from gui2 import Window2

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()

        self.connect(self, Qt.SIGNAL('triggered()'), self.closeEvent)

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("MusiclyApp")

        action = QtGui.QAction("&Add Playlist" , self)
        action.setStatusTip("adding playlist")
        action.triggered.connect(self.closeEvent)

        self.statusBar()

        menu = self.menuBar()
        PlaylistMenu = menu.addMenu("&PlayList")
        PlaylistMenu.addAction(action)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Pick", self)
        btn.clicked.connect(self.link)

        btn.resize(btn.sizeHint())
        btn.move(200,200)

        btn2 = QtGui.QPushButton("link", self)
        btn2.clicked.connect(self.link)

        btn2.resize(btn.sizeHint())
        btn2.move(300, 200)

        self.le = QtGui.QLineEdit(self)
        self.btn1 = QtGui.QPushButton("get name",self)
        self.btn1.clicked.connect(self.gettext)

        arr = {'monica' , 'bt7eb' , 'blala'}

        y = 300

        i=0
        while i<100:

            l = QtGui.QLabel("monica",self)
            l.move(200,y)
            y += 20
            i += 1


        self.show()

    def gettext(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

        if ok:
            # self.le1.setText(str(text))
            print(text)


    def link(self):

        print("3asalya")
        self.f = Window2()
        self.f.show()

    def closeEvent(self,event):
        print("7madaa ")
        sys.exit()

    def pick(self):
        name = QtGui.QFileDialog.getOpenFileName(self,'pick file')
        print(name)

def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


main()