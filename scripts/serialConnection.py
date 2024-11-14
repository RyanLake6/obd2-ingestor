import obd
import subprocess
import getpass

"""
Script to make a serial connection to OBD. You will need to virtualize the wifi connection to a USB port.
"""

def virtualizeUsbPort(sudo_password, socat_port, tcp_port):
    # Define the socat command
    command = f"echo {sudo_password} | sudo -S socat pty,link={socat_port},waitslave tcp:192.168.0.150:{tcp_port}"

    print(f"Running socat command for {socat_port} and {tcp_port}")
    
    # Run the socat command in the background and return the process object
    process = subprocess.Popen(command, shell=True)
    
    # Return the process to manage later
    return process

def getConnection():
    # Scan for available OBD-II serial ports
    ports = obd.scan_serial()  # return list of valid USB or RF ports
    print("Available ports are: ", ports)
    
    if ports:
        # Establish connection to the first valid port in the list
        connection = obd.OBD(ports[0])  # connect to the first port in the list
        if connection.is_open():
            print(f"Successfully connected to {ports[0]}")
            response = connection.query(obd.commands.RPM)
            print(f"Response from obd rpm is {response}")
            return True
        else:
            print(f"Failed to connect to {ports[0]}")
            return False
    else:
        print("No valid OBD-II ports found.")
        return False

def closeSubprocess(process):
    # Kill the subprocess once done
    print(f"Killing socat process {process.pid}")
    process.terminate()  # Try to terminate gracefully
    
    try:
        process.wait(timeout=5)  # Wait up to 5 seconds for the process to finish
    except subprocess.TimeoutExpired:
        print(f"Process {process.pid} did not terminate in time, killing it")
        process.kill()  # Force kill the process


# Main logic to attempt serial connection
try:
    socat_ports = ['/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyUSB3']
    open_ports = ["135", "137", "139", "445", "3306", "5040", "6666", "8080", "27036", "33060", "49664", "49665", "49666", "49667", "49668", "49684"]

    # Prompt for sudo password
    sudo_password = getpass.getpass("Enter your sudo password: ")

    for socat_port in socat_ports:
        for open_port in open_ports:
        
            # Virtualize the USB port using socat
            socat_process = virtualizeUsbPort(sudo_password, socat_port, open_port)

            # Once the port is virtualized, try to get the OBD connection
            if getConnection():
                print("OBD connection established successfully.")
            else:
                print("Failed to establish OBD connection.")

            # After getting the connection or after an attempt, kill the socat process
            closeSubprocess(socat_process)

except Exception as e:
    print("Exception hit: ", e)

