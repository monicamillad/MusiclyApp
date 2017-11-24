import sys
from PyQt4 import QtGui, QtCore
from PyQt4 import Qt

class Window2(QtGui.QMainWindow):

    def __init__(self):
        super(Window2,self).__init__()

        self.connect(self, Qt.SIGNAL('triggered()'), self.closeEvent)

        self.setGeometry(50,50,500,300)
        self.setWindowTitle("3asalya")

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
        btn.clicked.connect(self.pick)

        btn.resize(btn.sizeHint())
        btn.move(200,200)



        self.show()

    def closeEvent(self,event):
        print("7madaa ")
        sys.exit()

    def pick(self):
        name = QtGui.QFileDialog.getOpenFileName(self,'pick file')
        print(name)

# def main():
#     app = QtGui.QApplication(sys.argv)
#     GUI = Window2()
#     sys.exit(app.exec_())
#
#
# main()