import obd
obd.logger.setLevel(obd.logging.DEBUG)
ports = obd.scan_serial()
print(ports)
connection = obd.OBD("/dev/ttyUSB0", baudrate=38400) # /dev/pts/6
if connection.is_connected():
    print("connected")
    # Send a simple command (engine RPM as an example)
    print("Sending request for Engine RPM...")
    cmd = obd.commands.RPM  # OBD-II command for RPM
    response = connection.query(cmd, timeout=5)  # Query the command

    # Check and display response
    if response.is_successful():
        print(f"Engine RPM: {response.value}")
    else:
        print("Failed to retrieve Engine RPM. The response was not successful.")

# ps aux | grep socat
# sudo socat pty,link=/dev/ttyUSB0,waitslave tcp:192.168.0.10:35000 &
# ls -l /dev/ttyUSB0
# nc -zv 192.168.0.10 35000
# sudo socat -d -d pty,link=/dev/ttyUSB0,waitslave tcp:192.168.0.10:35000
# ls -l /dev/ttyUSB0
    # serial_port = "/dev/pts/3"
# sudo chmod 666 /dev/pts/6



"""
Steps to run this atm:
sudo socat -d -d pty,link=/dev/ttyUSB0,waitslave tcp:192.168.0.10:35000&
sudo chmod 666 /dev/ttyUSB0
python3 scripts/testingNewIp.py 
"""
