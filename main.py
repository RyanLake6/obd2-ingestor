import time

from obdii import OBD2Client
from gui.app import DashClient 

if __name__ == '__main__':
    client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)

    print("sleeping until socat process is started in other thread")
    time.sleep(8)
    print("attempting to connect to OBD-II device")

    client.connect()


    # While running output some rpm values every 3 seconds
    while True:
        rpm_data = client.get_rpm()
        if rpm_data:
            rpm_value, rpm_unit = rpm_data
            print(f"Current RPM: {rpm_value} {rpm_unit}")
        else:
            print("no rpm data returned")
        time.sleep(3)

    # gui = DashClient()
    # gui.create_app()
    # gui.run_dash()