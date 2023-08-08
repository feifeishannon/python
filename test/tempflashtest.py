import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, QTimer


class ThermometerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.target_temperature = 1
        self.animation_duration = 2000  # milliseconds
        self.animation_step = 1  # degrees

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTemperature)
        self.timer.start(self.animation_duration // (self.temperature - self.target_temperature))

    def setTemperature(self, temperature):
        if self.temperature != temperature:
            self.target_temperature = temperature
            self.timer.start(self.animation_duration // abs(self.temperature - self.target_temperature))

    def updateTemperature(self):
        if self.temperature != self.target_temperature:
            if self.temperature < self.target_temperature:
                self.temperature += self.animation_step
            else:
                self.temperature -= self.animation_step
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw thermometer background
        painter.fillRect(30, 30, 30, 150, QColor(200, 200, 200))

        # Draw temperature bar
        temperature_height = 150 * (self.temperature / 100)
        painter.fillRect(30, 180 - temperature_height, 30, temperature_height, QColor(255, 0, 0))

        # Draw temperature value
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 12))
        painter.drawText(70, 200, f"{self.temperature}°C")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thermometer UI with Animation")
        self.setGeometry(100, 100, 200, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.thermometer_widget = ThermometerWidget()
        self.layout.addWidget(self.thermometer_widget)

        self.thermometer_widget.setTemperature(50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
