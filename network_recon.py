# network_recon.py
import socket
import threading
import time
import os
from utils.port_scanner import scan_ports
from utils.banner_grabber import grab_banner

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Ensure reports directory exists
report_dir = "reports"
os.makedirs(report_dir, exist_ok=True)
report_file = os.path.join(report_dir, "scan_report.txt")

def save_report(data):
    with open(report_file, "a") as file:
        file.write(data + "\n")

# Main function
if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    start_time = time.time()

    try:
        print(f"{Colors.HEADER}Starting network reconnaissance on {target}...{Colors.ENDC}\n")
        
        # Port scanning
        open_ports = scan_ports(target, 1, 1024)  # Scans ports 1 to 1024
        if not open_ports:
            print(f"{Colors.WARNING}No open ports found.{Colors.ENDC}")
        else:
            for port in open_ports:
                banner = grab_banner(target, port)
                result = f"Port {port}/tcp is open. Banner: {banner}"
                print(f"{Colors.OKGREEN}{result}{Colors.ENDC}")
                save_report(result)
        
        print(f"\n{Colors.OKBLUE}Scan completed in {time.time() - start_time:.2f} seconds.{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}Error: {str(e)}{Colors.ENDC}")
    finally:
        print(f"{Colors.HEADER}Report saved to {report_file}{Colors.ENDC}")
