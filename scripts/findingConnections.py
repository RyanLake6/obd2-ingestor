import subprocess
import time
import os

# Define the IP of your OBD-II device and the ports you want to scan
OBD2_IP = "192.168.0.150"  # IP address of the OBD-II device
COMMON_PORTS = [35000, 35001, 35002, 35003, 35004, 35005]  # Common OBD-II ports to check
SCAN_INTERVAL = 1  # Time between scans (in seconds)
MAX_ATTEMPTS = 10  # Maximum number of scan attempts

# Function to run nmap command
def run_nmap_scan(ip, port):
    try:
        print(f"Scanning {ip} on port {port}...")
        # Run the Nmap scan for a specific port
        result = subprocess.run(
            ["nmap", "-p", str(port), ip],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output = result.stdout.decode('utf-8')
        if "open" in output:
            print(f"Port {port} is open on {ip}")
            return True
        else:
            print(f"Port {port} is closed on {ip}")
            return False
    except Exception as e:
        print(f"Error during nmap scan: {e}")
        return False

# Function to perform a series of scans to detect open ports
def scan_for_obd2_port(ip, ports, max_attempts=MAX_ATTEMPTS, scan_interval=SCAN_INTERVAL):
    attempt = 0
    while attempt < max_attempts:
        print(f"Attempt {attempt + 1} of {max_attempts}...")
        # Scan each port in the list
        for port in ports:
            if run_nmap_scan(ip, port):
                return port
        attempt += 1
        print(f"Waiting {scan_interval} seconds before retrying...")
        time.sleep(scan_interval)
    print("Max attempts reached, no open ports found.")
    return None

# Main function
if __name__ == "__main__":
    print(f"Starting scan on {OBD2_IP}...")
    open_port = scan_for_obd2_port(OBD2_IP, COMMON_PORTS)
    
    if open_port:
        print(f"Found open OBD-II port: {open_port}")
    else:
        print("No open OBD-II ports found. Please ensure your car is on and try again.")
