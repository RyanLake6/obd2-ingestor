import time
import sys
import argparse

from obdii.obdii_client import OBD2Client
from gui.app import PyQtClient 
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    """Parse argument flags"""
    parser = argparse.ArgumentParser(description="OBD-II Ingestory with display")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    """Build OBD-II Connection"""
    obd2Client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)

    print("Awaiting for OBD-II client to intialize")
    while not obd2Client.connected:
        time.sleep(3)
        print("awaiting OBD-II connection...")
    print("Initialized OBD-II device, connecting...")

    obd2Client.connect()

    # # Test all obd commands in enum
    # for command in OBDCommand:
    #     telemetry_value, telemetry_unit = obd2Client.get_telemetry(command)
    #     print(f"returning telemetry: {telemetry_value}, {telemetry_unit}")

    """Startup GUI"""
    app = QApplication(sys.argv)
    main_window = PyQtClient(obd2Client, debug_mode=args.debug)
    main_window.show()
    sys.exit(app.exec_())
