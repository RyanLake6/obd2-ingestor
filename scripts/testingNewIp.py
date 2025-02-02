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

