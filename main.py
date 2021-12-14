import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import  QTimer, QTime
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('GUI4.ui', self)

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.reloj.setText(displayText)
        self.lcdNumber.display(displayText)
  
app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
