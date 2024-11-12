import socket
import time

# IP and port configuration
OBD2_IP = "192.168.0.150"
OBD2_PORT = 8080 ## 3306 auto fails

# Connect to the OBD-II device via TCP/IP
def connect_to_obd2(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)  # Set timeout to avoid hanging indefinitely
    try:
        s.connect((ip, port))
        print(f"Connected to OBD-II sensor at {ip}:{port}")
        return s
    except socket.error as e:
        print(f"Failed to connect to {ip}:{port} - {e}")
        return None

# Send initialization commands (if needed for your OBD-II model)
def initialize_obd2(s):
    init_commands = ["ATZ", "ATL0"]  # Resets and removes line feeds (optional commands)
    for command in init_commands:
        send_obd2_command(s, command)
        time.sleep(0.1)  # Short delay between init commands

# Send an OBD-II command (e.g., "010C" for RPM)
def send_obd2_command(s, command):
    try:
        s.sendall(f"{command}\r".encode())  # Send the command with carriage return
        response = s.recv(1024).decode()  # Read the response
        print(f"Response: {response}")
        return response
    except socket.error as e:
        print(f"Failed to send command: {e}")
        return None
    
open_ports = [135, 137, 139, 445, 3306, 5040, 6666, 8080, 27036, 33060, 49664, 49665, 49666, 49667, 49668, 49684]
for port in open_ports:
    # Example usage
    print(f"testing port: {port}")
    obd2_connection = connect_to_obd2(ip=OBD2_IP, port=port)

    if obd2_connection:
        initialize_obd2(obd2_connection)  # Send any initialization commands
        
        # Send OBD-II request (example: "010C" for RPM data)
        response = send_obd2_command(obd2_connection, "010C")
        print("The response is: ", response)
        
        # Process the response
        if response:
            print(f"Received RPM data: {response}")
        
        # Close the connection when done
        obd2_connection.close()
