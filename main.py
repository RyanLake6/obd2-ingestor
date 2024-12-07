import random
import threading
import time

from obdii.obdii_client import OBD2Client
from gui.app import DashClient 


def mock_generate_external_data_thread(dash_client):
    """Start generate_external_data in a seperate thread

    Args:
        dash_client (DashClient): dash client class for gui
    """
    data_thread = threading.Thread(target=mock_generate_external_data, args=(dash_client,), daemon=True)
    data_thread.start()


def mock_generate_external_data(dash_client):
    """sends data for dash gui to display

    Args:
        dash_client (DashClient): dash client class for gui
    """
    while True:
        new_x = time.time()
        new_y = random.randint(0, 5)
        dash_client.update_data(new_x, new_y)
        time.sleep(1)  # Simulate data coming every second



def generate_external_data_thread(dash_client, obd2client):
    """Start generate_external_data in a seperate thread

    Args:
        dash_client (DashClient): dash client class for gui
    """
    data_thread = threading.Thread(target=generate_external_data, args=(dash_client,obd2client,), daemon=True)
    data_thread.start()


def generate_external_data(dash_client, obd2client):
    """sends data for dash gui to display

    Args:
        dash_client (DashClient): dash client class for gui
    """
    while True:
        rpm_data = client.get_rpm()
        if rpm_data:
            rpm_value, rpm_unit = rpm_data
            print(f"Current RPM: {rpm_value} {rpm_unit}")
            new_x = time.time()
            new_y = rpm_value
            dash_client.update_data(new_x, new_y)
        else:
            print("no rpm data returned")
        time.sleep(1)


if __name__ == '__main__':
    client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)

    print("Awaiting for OBD-II client to intialize", end="")
    while not client.connected:
        print(".", end="")
        time.sleep(.5)
    print("\nInitialized OBD-II device, connecting...")

    # print("sleeping until socat process is started in other thread")
    # time.sleep(8)
    # print("attempting to connect to OBD-II device")

    client.connect()


    # While running output some rpm values every 3 seconds
    # while True:
    #     rpm_data = client.get_rpm()
    #     if rpm_data:
    #         rpm_value, rpm_unit = rpm_data
    #         print(f"Current RPM: {rpm_value} {rpm_unit}")
    #     else:
    #         print("no rpm data returned")
    #     time.sleep(3)


    # example of mocked data generation
    # gui = DashClient()
    # gui.create_app()
    # mock_generate_external_data_thread(gui)
    # gui.run_dash()

    # trying to show real car data:
    gui = DashClient()
    gui.create_app()
    generate_external_data_thread(gui, client)
    gui.run_dash()