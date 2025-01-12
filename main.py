import random
import threading
import time
import sys

from obdii.obdii_client import OBD2Client, OBDCommand
from gui.app import PyQtClient 
from PyQt5.QtWidgets import QApplication


# def mock_generate_external_data_thread(dash_client):
#     """Start generate_external_data in a seperate thread

#     Args:
#         dash_client (DashClient): dash client class for gui
#     """
#     data_thread = threading.Thread(target=mock_generate_external_data, args=(dash_client,), daemon=True)
#     data_thread.start()


# def mock_generate_external_data(dash_client):
#     """sends data for dash gui to display

#     Args:
#         dash_client (DashClient): dash client class for gui
#     """
#     while True:
#         new_x = time.time()
#         new_y = random.randint(0, 5)
#         dash_client.update_data(new_x, new_y)
#         time.sleep(1)  # Simulate data coming every second



# def generate_external_data_thread(dash_client, obd2client):
#     """Start generate_external_data in a seperate thread

#     Args:
#         dash_client (DashClient): dash client class for gui
#     """
#     data_thread = threading.Thread(target=generate_external_data, args=(dash_client,obd2client,), daemon=True)
#     data_thread.start()


# def generate_external_data(dash_client, obd2client):
#     """sends data for dash gui to display

#     Args:
#         dash_client (DashClient): dash client class for gui
#     """
#     while True:
#         rpm_data = obd2client.get_rpm()
#         if rpm_data:
#             rpm_value, rpm_unit = rpm_data
#             print(f"Current rpm: {rpm_value} and value: {rpm_unit}")
#             print(f"the type of hte rpm value is: {type(rpm_value)}")
#             new_x = time.time()
#             new_y = rpm_value
#             dash_client.update_data(new_x, new_y)
#         else:
#             print("no rpm data returned")
#         time.sleep(1)



if __name__ == '__main__':
    """Use this code block to setup the pulling of data from the obd2 device"""
    obd2Client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)

    print("Awaiting for OBD-II client to intialize")
    while not obd2Client.connected:
        time.sleep(3)
        print("awaiting...")
    print("Initialized OBD-II device, connecting...")

    obd2Client.connect()

    """Use this code block to show a example of pyqt window with fake data for now"""
    # app = QApplication(sys.argv)
    # main_window = PyQtClient(obd2Client)
    # main_window.show()
    # sys.exit(app.exec_())



    # While running output some rpm values every 3 seconds
    while True:
        rpm_data = obd2Client.get_rpm()
        voltage_data = obd2Client.get_voltage()
        oil_temp_data = obd2Client.get_oil_temp()
        engine_load_data = obd2Client.get_engine_load()
        fuel_level_data = obd2Client.get_fuel_level()
        ambient_temp_data = obd2Client.get_ambient_temp()
        coolant_temp_data = obd2Client.get_coolant_temp()
        better_rpm_data = obd2Client.get_telemetry(OBDCommand.RPM)
        if rpm_data:
            rpm_value, rpm_unit = rpm_data
            print(f"Current RPM: {rpm_value} {rpm_unit}")
            voltage_value, voltage_unit = voltage_data
            print(f"Current voltage: {voltage_value} {voltage_unit}")
            oil_temp_value, oil_temp_unit = oil_temp_data
            print(f"Current oil temp: {oil_temp_value} {oil_temp_unit}")
            engine_load_value, engine_load_unit = engine_load_data
            print(f"Current engine load: {engine_load_value} {engine_load_unit}")
            fuel_level_value, fuel_level_unit = fuel_level_data
            print(f"Current fuel level: {fuel_level_value} {fuel_level_unit}")
            ambient_temp_value, ambient_temp_unit = ambient_temp_data
            print(f"Current ambient temp: {ambient_temp_value} {ambient_temp_value}")
            coolant_temp_value, coolant_temp_unit = coolant_temp_data
            print(f"Current coolant temp: {coolant_temp_value} {coolant_temp_unit}")
            rpm_value_generic, rpm_unit_generic = better_rpm_data
            print(f"Current RPM (this is from the generic function with enums): {rpm_value_generic} {rpm_unit_generic}")
        else:
            print("no rpm data returned")
        time.sleep(5)