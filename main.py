import sys
from PyQt5.QtWidgets import QApplication,  QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00", self)
        self.timer = QTimer()
        self.initGui()

    def initGui(self):
        self.setWindowTitle("My Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        


def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()