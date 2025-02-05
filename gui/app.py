import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
import random

from obdii.obdii_client import OBD2Client, OBDCommand


class PyQtClient(QMainWindow):
    def __init__(self, obd2Client: OBD2Client, parent=None, debug_mode=False):
        if debug_mode:
            print("debug mode - mocking all data produced")

        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("OBD-II Telemetry")
        self.resize(800, 600)
        self.debug_mode = debug_mode
        self.obd2Client = obd2Client

        # Create a central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Create a horizontal layout for the labels
        labels_layout = QHBoxLayout()

        # Create labels for displaying single values
        self.rpm_label = QLabel("RPM: --", self)
        self.fuel_level_label = QLabel("Fuel Level: --", self)
        self.ambient_air_label = QLabel("Outside Temp: --", self)
        self.voltage_label = QLabel("Voltage: --", self)

        # Add labels to the horizontal layout
        labels_layout.addWidget(self.rpm_label)
        labels_layout.addWidget(self.fuel_level_label)
        labels_layout.addWidget(self.ambient_air_label)
        labels_layout.addWidget(self.voltage_label)

        # Add the horizontal layout with labels at the top of the window
        layout.addLayout(labels_layout)

        # Create a central GraphicsLayoutWidget for multiple plots
        self.graph_layout = pg.GraphicsLayoutWidget()
        layout.addWidget(self.graph_layout)

        # Adding live plots
        self.plot1 = self.graph_layout.addPlot(title="RPM")
        self.curve1 = self.plot1.plot(pen=pg.mkPen(color='y', width=2))

        self.plot2 = self.graph_layout.addPlot(title="Engine Load")
        self.curve2 = self.plot2.plot(pen=pg.mkPen(color='y', width=2))

        # Initialize data storage for the plots
        self.data1 = np.zeros(100)  # Buffer for RPM plot
        self.data2 = np.zeros(100)  # Buffer for Engine Load plot
        self.data3 = np.zeros(100)  # Buffer for Fuel Level plot
        self.data4 = np.zeros(100)  # Buffer for ambient air label
        self.data5 = np.zeros(100)  # Buffer for voltage plot
        self.ptr = 0

        # Set up a timer for periodic updates
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plots)
        self.timer.start(1000)  # Update every 1000ms

    def update_plots(self):
        """Update both plots and labels with simulated data."""
        # Update RPM plot
        self.data1[:-1] = self.data1[1:]
        if self.debug_mode:
            rpm_value = random.randint(500, 7000)
        else:
            rpm_value, _ = self.obd2Client.get_telemetry(OBDCommand.RPM)
        self.data1[-1] = rpm_value
        self.curve1.setData(self.data1)

        # Update Engine Load plot
        self.data2[:-1] = self.data2[1:]  
        if self.debug_mode:
            engine_load_value = random.uniform(0, 100)
        else:
            engine_load_value, _ = self.obd2Client.get_telemetry(OBDCommand.ENGINE_LOAD)
        self.data2[-1] = engine_load_value
        self.curve2.setData(self.data2)

        # Update Fuel Level value
        self.data3[:-1] = self.data3[1:]  
        if self.debug_mode:
            fuel_level_value = random.uniform(0, 100)
        else:
            fuel_level_value, _ = self.obd2Client.get_telemetry(OBDCommand.FUEL_LEVEL)
        self.data3[-1] = fuel_level_value

        # Update ambient air value
        self.data4[:-1] = self.data4[1:]
        if self.debug_mode:
            ambient_air_value = random.uniform(0, 100)
        else:
            ambient_air_value, _ = self.obd2Client.get_telemetry(OBDCommand.AMBIENT_AIR_TEMP)
        ambient_air_value_fahrenheit = (ambient_air_value * 9/5) + 32
        self.data4[-1] = ambient_air_value_fahrenheit

        # Update voltage value
        self.data5[:-1] = self.data5[1:]  
        if self.debug_mode:
            voltage_value = random.uniform(0, 100)  # Random Engine Load value
        else:
            voltage_value, _ = self.obd2Client.get_telemetry(OBDCommand.VOLTAGE)
        self.data5[-1] = voltage_value

        # Update labels with latest values
        self.rpm_label.setText(f"RPM: {rpm_value}")
        self.fuel_level_label.setText(f"Fuel Level: {fuel_level_value:.2f}%")
        self.ambient_air_label.setText(f"Outside Temp: {ambient_air_value_fahrenheit:.2f}\u00B0 C")
        self.voltage_label.setText(f"Voltage: {voltage_value:.2f}")

    def show(self):
        super().showFullScreen()
