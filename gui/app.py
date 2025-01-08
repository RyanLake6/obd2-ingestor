import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from obdii.obdii_client import OBD2Client


class PyQtClient(QMainWindow):
    def __init__(self, obd2Client: OBD2Client, parent=None):
        super().__init__(parent)
        self.setWindowTitle("OBD-II Telemetry")
        self.resize(800, 600)

        # Create a central GraphicsLayoutWidget for multiple plots
        self.central_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.central_widget)

        # Add multiple plots to the layout
        self.plot1 = self.central_widget.addPlot(title="RPM")
        self.curve1 = self.plot1.plot(pen=pg.mkPen(color='y', width=2))

        self.central_widget.nextRow()  # Move to the next row in the layout
        self.plot2 = self.central_widget.addPlot(title="Plot 2: Sine Wave")
        self.curve2 = self.plot2.plot(pen=pg.mkPen(color='r', width=2))

        # Initialize data storage
        self.data1 = np.zeros(1000)  # Buffer for plot1
        self.x_data2 = np.linspace(0, 2 * np.pi, 1000)  # X-axis for sine wave
        self.y_data2 = np.sin(self.x_data2)  # Initial sine wave data
        self.ptr = 0

        # Set up a timer for periodic updates
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.update_plots(obd2Client))
        self.timer.start(1000)  # Update every 1000ms

    def update_plots(self, obd2Client: OBD2Client):
        """Update both plots with new data."""
        # Update Plot 1 with random data
        self.data1[:-1] = self.data1[1:]  # Shift data left
        rpm_value, _ = obd2Client.get_rpm()
        self.data1[-1] = rpm_value # np.random.normal()  # Add a new random value, here to use the client rpm call
        self.curve1.setData(self.data1)

        # Update Plot 2 with a scrolling sine wave
        self.ptr += 1
        self.y_data2 = np.sin(self.x_data2 + 0.1 * self.ptr)  # Shift sine wave
        self.curve2.setData(self.x_data2, self.y_data2)

