#pip install PyQt6 PyQt6-tools 
from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/loginn.ui", self)
        self.controller = LoginController(self, self)

class Bloom(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/floreria_maiin.ui", self)

class AppManager:
    def __init__(self):
        self.login_window = Login()
        self.bloom_window = Bloom()
        #muestra pantalla
        self.login_window.show()
        
app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())