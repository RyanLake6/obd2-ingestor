import time

from obdii import OBD2Client
from gui.app import DashClient 

if __name__ == '__main__':
    client = OBD2Client("192.168.0.10", port=3500, baudrate=38400, debug=True)
    client.connect()

    # While running output some rpm values every 3 seconds
    while True:
        print("current rpm is: ", client.get_rpm())
        time.sleep(3)

    # gui = DashClient()
    # gui.create_app()
    # gui.run_dash()