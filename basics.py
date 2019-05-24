"""
 * @Author: Kaustav Vats 
 * @Date: 2019-05-23 23:50:43 
"""

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QMainWindow, QMessageBox, QCheckBox, QProgressBar, QLabel, QComboBox, QStyleFactory
from PyQt5.QtGui import QIcon
import time

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Yo!'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480

        # MenuBar and Status Bar
        ExtractAction = QAction("&Fanny Magnet", self)
        ExtractAction.setShortcut("Ctrl+Q")
        ExtractAction.setStatusTip("Leave Me Alone")    # Shown Below just like browsers.
        ExtractAction.triggered.connect(self.CloseApp)
        self.statusBar()
        mainMenu = self.menuBar()
        FileMenu = mainMenu.addMenu("&File")
        HelpMenu = mainMenu.addMenu("&Help")
        FileMenu.addAction(ExtractAction)

        self.initGUI()

    def initGUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  # Sets starting point of display on windows
        self.setWindowIcon(QIcon('favicon.ico'))
        self.home()

    def home(self):
        btn = QPushButton(QIcon('favicon.ico'), "Quit", self)
        # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.CloseApp)
        # btn.resize(100, 100)
        btn.resize(btn.sizeHint())
        btn.move(self.width/2, self.height/2)

        # ToolBar
        ExtractAction = QAction(QIcon('favicon.ico'), "BAAM", self) # Icon, Hover, Parent
        ExtractAction.triggered.connect(self.CloseApp)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(ExtractAction)

        # CheckBox
        CheckBox = QCheckBox('First CheckBox', self)
        CheckBox.stateChanged.connect(self.TestCheckBox)
        CheckBox.setChecked(False)
        CheckBox.move(100, 100)

        # ProgressBar
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(300, 100, 250, 20)
        self.downloadBtn = QPushButton("Download", self)
        self.downloadBtn.move(300, 150)
        self.downloadBtn.clicked.connect(self.Download)
        
        # Style
        print(self.style().objectName())
        self.styleChoice = QLabel("Windows", self)

        # Drop-down menu to change options.
        comboBox = QComboBox(self)
        comboBox.addItems(["motif", "Windows", "cde", "Plastique", "Cleanlooks", "windowsvista"])
        comboBox.move(100, 300)
        self.styleChoice.move(100, 350)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def Download(self):
        self.completed = 0
        while self.completed < 10:
            time.sleep(1)
            self.completed += 1
            self.progressBar.setValue(self.completed*10)

    def TestCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(self.left, self.top, self.width+100, self.height+100)
        else:
            self.setGeometry(self.left, self.top, self.width, self.height)

    def CloseApp(self):
        print("Closing App...")
        Choice = QMessageBox.question(self, "Quit", "Close the Application?", QMessageBox.Yes | QMessageBox.Cancel)
        if Choice == QMessageBox.Yes:
            print("Done!")
            sys.exit()
        else:
            print("Not now!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
