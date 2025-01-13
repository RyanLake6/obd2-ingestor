import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
import random


class PyQtClient(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("OBD-II Telemetry")
        self.resize(800, 600)

        # Create a central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Create a horizontal layout for the labels
        labels_layout = QHBoxLayout()

        # Create labels for displaying up-to-date values
        self.rpm_label = QLabel("RPM: --", self)
        self.voltage_label = QLabel("Voltage: --", self)
        self.fuel_level_label = QLabel("Fuel Level: --", self)
        self.ambient_air_label = QLabel("Outside Temp: --", self)

        # Add labels to the horizontal layout
        labels_layout.addWidget(self.rpm_label)
        labels_layout.addWidget(self.voltage_label)
        labels_layout.addWidget(self.fuel_level_label)
        labels_layout.addWidget(self.ambient_air_label)

        # Add the horizontal layout with labels at the top of the window
        layout.addLayout(labels_layout)

        # Create a central GraphicsLayoutWidget for multiple plots
        self.graph_layout = pg.GraphicsLayoutWidget()
        layout.addWidget(self.graph_layout)

        # Add multiple plots to the layout
        self.plot1 = self.graph_layout.addPlot(title="RPM")
        self.curve1 = self.plot1.plot(pen=pg.mkPen(color='y', width=2))

        self.plot2 = self.graph_layout.addPlot(title="RPM 2")
        self.curve2 = self.plot2.plot(pen=pg.mkPen(color='y', width=2))

        # Initialize data storage for the plots
        self.data1 = np.zeros(100)  # Buffer for RPM plot
        self.data2 = np.zeros(100)  # Buffer for Engine Load plot
        self.data3 = np.zeros(100)  # Buffer for Fuel Level plot
        self.data4 = np.zeros(100)  # Buffer for ambient air label
        self.ptr = 0

        # Set up a timer for periodic updates
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(1000)  # Update every 1000ms

    def update_plots(self):
        """Update both plots and labels with simulated data."""
        # Update RPM plot with random data between 500 and 7000
        self.data1[:-1] = self.data1[1:]  # Shift data left
        rpm_value = random.randint(500, 7000)  # Random RPM value
        self.data1[-1] = rpm_value  # Add a new RPM value
        self.curve1.setData(self.data1)

        # Update Engine Load plot with random data between 0 and 100
        self.data2[:-1] = self.data2[1:]  # Shift data left
        voltage_value = random.uniform(0, 100)  # Random Engine Load value
        self.data2[-1] = voltage_value  # Add a new Engine Load value
        self.curve2.setData(self.data2)

        # Update Fuel Level plot with random data between 0 and 100
        self.data3[:-1] = self.data3[1:]  # Shift data left
        fuel_level_value = random.uniform(0, 100)  # Random Fuel Level value
        self.data3[-1] = fuel_level_value  # Add a new Fuel Level value
        # self.curve3.setData(self.data3)

        # Update ambient air plot with random data between 0 and 100
        self.data4[:-1] = self.data4[1:]  # Shift data left
        ambient_air_value = random.uniform(0, 100)  # Random Fuel Level value
        self.data4[-1] = ambient_air_value  # Add a new Fuel Level value
        # self.curve4.setData(self.data4)

        # Update labels with latest random values
        self.rpm_label.setText(f"RPM: {rpm_value}")
        self.voltage_label.setText(f"Voltage: {voltage_value:.2f}")
        self.fuel_level_label.setText(f"Fuel Level: {fuel_level_value:.2f}%")
        self.ambient_air_label.setText(f"Outside Temp: {ambient_air_value:.2f}\u00B0 C")

    def show(self):
        super().showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize the PyQtClient without the OBD2Client (using random data)
    window = PyQtClient()
    window.show()

    sys.exit(app.exec_())
