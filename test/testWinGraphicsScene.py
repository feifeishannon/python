import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class WaveformPlot:
    def __init__(self):
        self.data = []  # This assumes waveform data is a one-dimensional array

    def set_data(self, data):
        self.data = data

    def draw(self, scene):
        scene.clear()
        if len(self.data) == 0:
            return

        height = scene.height()
        width = scene.width()

        # Calculate the horizontal interval between points
        interval = width / len(self.data)

        # Draw the waveform
        prev_x, prev_y = 0, height / 2
        for i, value in enumerate(self.data):
            x = i * interval
            y = height / 2 - value * height / 2
            line = QGraphicsLineItem(prev_x, prev_y, x, y)
            scene.addItem(line)
            prev_x, prev_y = x, y


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waveform Plot")
        self.setGeometry(100, 100, 800, 400)

        # Create QGraphicsView and QGraphicsScene
        self.graphics_view = QGraphicsView(self)
        self.graphics_scene = QGraphicsScene(self)
        self.graphics_view.setScene(self.graphics_scene)

        # Create waveform plot object
        self.waveform_plot = WaveformPlot()

        # Add QGraphicsView to layout
        layout = QVBoxLayout()
        layout.addWidget(self.graphics_view)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_waveform(self, data):
        self.waveform_plot.set_data(data)
        self.waveform_plot.draw(self.graphics_scene)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()

    # Generate some waveform data (example data: a sinusoidal waveform)
    frequency = 5.0
    sampling_rate = 1000
    num_samples = 100
    time = np.linspace(0, (num_samples - 1) / sampling_rate, num_samples)
    waveform_data = np.sin(2 * np.pi * frequency * time)

    main_window.update_waveform(waveform_data)
    main_window.show()

    sys.exit(app.exec_())
    