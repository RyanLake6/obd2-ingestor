import obd
import threading

"""
This script is meant to go through all ports from the nmap and find which one can send a command and get data
"""

# List of open ports from nmap scan
open_ports = [135, 137, 139, 445, 3306, 5040, 6666, 8080, 27036, 33060, 49664, 49665, 49666, 49667, 49668, 49684]

# Timeout in seconds for each connection attempt
timeout = 5

# Function to attempt OBD connection on a specific port
def try_port(port):
    try:
        connection = obd.OBD(f"192.168.0.150:{port}")
        if connection.is_connected():
            print(f"\033[32mSUCCESS on port {port}\033[0m")
            # Test an OBD command
            print("attempting to send a pbd query for rpm")
            response = connection.query(obd.commands.RPM)
            print("RPM:", response.value)
            return connection
    except Exception as e:
        print(f"Port {port} failed with error: {e}")
    finally:
        if connection:
            connection.close()
    return None

# Attempt to connect to each port with a timeout
for port in open_ports:
    print(f"Trying port {port}")
    connection = None
    thread = threading.Thread(target=lambda p=port: try_port(p))
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print(f"Port {port} timed out.")
        thread.join()  # Ensure the thread is cleaned up before moving to the next port
    elif connection:
        # Break if a successful connection is found
        break
