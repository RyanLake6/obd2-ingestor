import obd
import subprocess
import time
import threading

from enum import Enum

class OBDCommand(Enum):
    RPM = obd.commands.RPM
    VOLTAGE = obd.commands.ELM_VOLTAGE
    # OIL_TEMP = obd.commands.OIL_TEMP # Unable to pull this data from my car computer / scanner
    ENGINE_LOAD = obd.commands.ENGINE_LOAD
    FUEL_LEVEL = obd.commands.FUEL_LEVEL
    AMBIENT_AIR_TEMP = obd.commands.AMBIANT_AIR_TEMP
    COOLANT_TEMP = obd.commands.COOLANT_TEMP

"""
Class to setup a obd connection to pull live sensor data over an OBD-II connection
"""

class OBD2Client:
    def __init__(self, ip = "", port=3500, serial_port="/dev/ttyUSB0", baudrate=9600, timeout=5, debug=False):
        """Initializes the OBD-II client with the given parameters.

        Args:
            ip (str, optional): ip address of a wifi enabled OBD-II device. Defaults to "".
            port (int, optional): port number of a wifi enabled OBD-II device. Defaults to 3500.
            serial_port (str, optional): serial port of a USB connected OBD-II device. Defaults to "/dev/ttyUSB0".
            baudrate (int, optional): rate at which data is transmitted over serial communication (bits per second). Defaults to 9600.
            timeout (int, optional): timeout of when trying to run commands (in seconds). Defaults to 5.
            debug (bool, optional): whether or not to print debugging logs. Defaults to False.
        """
        self.ip = ip
        self.port = port
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection = None
        self.debug = debug
        self.connected = False

        # virtualize a serial connection from wifi
        if ip != "" and port != 0:
            self.virtualize_connection_thread()


    def virtualize_connection_thread(self):
        """calling virtualize_connection in another thread to not block the main process"""
        print("Starting virtualize connection in a seperate thread")
        thread = threading.Thread(target=self.virtualize_connection, daemon=True)
        thread.start()
        print("Virtualized connection in a another thread")

    def virtualize_connection(self):
        """Virtualizes a wifi connection to be serial"""

        socat_command = [
            "sudo", "socat", "-d", "-d",
            "pty,link=/dev/ttyUSB0,waitslave",
            "tcp:192.168.0.10:35000"
        ]

        chmod_command = ["sudo", "chmod", "666", "/dev/ttyUSB0"]

        # Start the socat command in a separate process
        process = subprocess.Popen(
            socat_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        print(f"Started virtual serial port with PID: {process.pid}")

        try:
            # Wait briefly to ensure the /dev/ttyUSB0 device is created
            time.sleep(3)

            # Make sure we have the correct permission on the serial port
            print("Changing serial port permissions...")
            subprocess.run(chmod_command, check=True)
            print("Permissions updated successfully.")

            self.connected = True
        except KeyboardInterrupt:
            print("Killing socat process...")
            process.terminate()
            process.wait()  # Ensure the process has stopped


    def connect(self):
        """Creates serial connection to the OBD-II sensor"""
        if self.debug:
            obd.logger.setLevel(obd.logging.DEBUG)
            ports = obd.scan_serial()
            print("OBD-II scanned serial ports:" , ports)

        connection = obd.OBD(self.serial_port, baudrate=self.baudrate)
        self.connection = connection

    def get_telemetry(self, telemetry: OBDCommand) -> tuple[float, str] | None:
        """Fetch the requested telemetry data from obd

        Args:
            telemetry (OBDCommand): The obd command to pull from the OBDII sensor

        Returns:
            tuple[float, str] | None: A tuple of the value and unit of the telemetry field
        """
        if not self.connection:
            print("No connection to OBD-II device.")
            return None
        
        if isinstance(telemetry, Enum):
            telemetry = telemetry.value

        response = self.connection.query(telemetry)

        if response and not response.is_null():
            return response.value.magnitude, response.unit
        else:
            print("Failed to get telemetry no data available")
            return None
    