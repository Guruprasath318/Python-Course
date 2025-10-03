import sys
from PyQt5.Qtwidgets import QApplication, QWidget, QLabel, QVBoxLayout
from pyqt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 200, 100)
        layout = QVBoxLayout()
        self.time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.time_label)
        self.setLayout(layout)
        self.update_time()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
