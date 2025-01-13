import random
import threading
import time
import sys
import obd

from obdii.obdii_client import OBD2Client, OBDCommand
from gui.app import PyQtClient 
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    """Use this code block to setup the pulling of data from the obd2 device"""
    obd2Client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)

    print("Awaiting for OBD-II client to intialize")
    while not obd2Client.connected:
        time.sleep(3)
        print("awaiting...")
    print("Initialized OBD-II device, connecting...")

    obd2Client.connect()

    # # Test all obd commands in enum
    # for command in OBDCommand:
    #     telemetry_value, telemetry_unit = obd2Client.get_telemetry(command)
    #     print(f"returning telemetry: {telemetry_value}, {telemetry_unit}")


    """Use this code block to show a example of pyqt window with fake data for now"""
    app = QApplication(sys.argv)
    main_window = PyQtClient(obd2Client)
    main_window.show()
    sys.exit(app.exec_())
