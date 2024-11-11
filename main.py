import socket
import time

# Replace with the IP address of your OBD-II device and its port (e.g., port 35000)
OBD2_IP = "192.168.0.150"  # IP of the OBD-II device
OBD2_PORT = 35000  # Common port for many Wi-Fi OBD-II devices

# Connect to the OBD-II device via TCP/IP
def connect_to_obd2(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print(f"Connected to OBD-II sensor at {ip}:{port}")
        return s
    except socket.error as e:
        print(f"Failed to connect to {ip}:{port} - {e}")
        return None

# Send an OBD-II command (e.g., "010C" for RPM)
def send_obd2_command(s, command):
    try:
        s.sendall(command.encode())  # Send the command
        response = s.recv(1024).decode()  # Read the response
        print(f"Response: {response}")
        return response
    except socket.error as e:
        print(f"Failed to send command: {e}")
        return None

# Example usage
obd2_connection = connect_to_obd2(OBD2_IP, OBD2_PORT)

if obd2_connection:
    time.sleep(1)  # Wait for a second to establish connection
    
    # Send OBD-II request (example: "010C" for RPM data)
    response = send_obd2_command(obd2_connection, "010C")
    
    # Process the response
    if response:
        print(f"Received RPM data: {response}")
    
    # Close the connection when done
    obd2_connection.close()
