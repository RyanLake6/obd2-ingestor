import obd
import subprocess
import time
import threading

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
        print("running virtualize connection in a another thread")

    def virtualize_connection(self):
        """Virtualizes a wifi connection to be serial"""

        # Define the socat command
        socat_command = [
            "sudo", "socat", "-d", "-d",
            "pty,link=/dev/ttyUSB0,waitslave",
            "tcp:192.168.0.10:35000"
        ]

        # Define the chmod command
        chmod_command = ["sudo", "chmod", "666", "/dev/ttyUSB0"]

        # Start the socat command in a separate process
        process = subprocess.Popen(
            socat_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        print(f"Socat process started with PID: {process.pid}")

        try:
            # Wait briefly to ensure the /dev/ttyUSB0 device is created
            time.sleep(3)

            # Run the chmod command while socat is running
            print("Running chmod command...")
            subprocess.run(chmod_command, check=True)
            print("Permissions updated successfully.")

            self.connected = True

            # # Optional: Read the socat output 
            # while True:
            #     output = process.stdout.readline()
            #     error = process.stderr.readline()

            #     if output:
            #         print(f"Socat STDOUT: {output.decode().strip()}")
            #     if error:
            #         print(f"Socat STDERR: {error.decode().strip()}")
                
            #     # Check if socat has exited
            #     if process.poll() is not None:
            #         break
        except KeyboardInterrupt:
            print("Stopping socat process...")
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


    def get_rpm(self) -> tuple[float, str] | None:
        """Gets the current RPM

        Returns:
            tuple[float, str] | None: rpm data tuple of the value and units or None, if nothing is connected or query failed
        """
        if not self.connection:
            print("No connection to OBD-II device.")
            return None
        cmd = obd.commands.RPM
        response = self.connection.query(cmd)

        if response and not response.is_null():
            return response.value.magnitude, response.unit
        else:
            print("Failed to get rpm or no data available")
            return None
        
    def get_voltage(self) -> tuple[float, str] | None:
        """Gets the current voltage

        Returns:
            tuple[float, str] | None: voltage data tuple of the value and units or None, if nothing is connected or query failed
        """
        if not self.connection:
            print("No connection to OBD-II device.")
            return None
        cmd = obd.commands.ELM_VOLTAGE
        response = self.connection.query(cmd)

        if response and not response.is_null():
            return response.value, response.unit
        else:
            print("Failed to get voltage or no data available")
            return None
        
    def get_oil_temp(self) -> tuple[float, str] | None:
        """Gets the current oil temp
        Returns:
            tuple[float, str] | None: oil temp data tuple of the value and units or None, if nothing is connected or query failed
        """
        if not self.connection:
            print("No connection to OBD-II device.")
            return None
        cmd = obd.commands.OIL_TEMP
        response = self.connection.query(cmd)

        if response and not response.is_null():
            return response.value, response.unit
        else:
            print("Failed to get oil temp or no data available")
            return None
        
    def get_engine_load(self) -> tuple[float, str] | None:
        """Gets the current engine load as a percent
        Returns:
            tuple[float, str] | None: engine load data tuple of the value and units or None, if nothing is connected or query failed
        """
        if not self.connection:
            print("No connection to OBD-II device.")
            return None
        cmd = obd.commands.OIL_TEMP
        response = self.connection.query(cmd)

        if response and not response.is_null():
            return response.value, response.unit
        else:
            print("Failed to get engine load or no data available")
            return None