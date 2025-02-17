# NetworkRecon - Basic Network Reconnaissance Tool

## Description
NetworkRecon is a lightweight Python tool for network reconnaissance. It scans open ports on a target, retrieves service banners, and logs the results.

## Features
- **Port Scanning**: Identifies open ports on a target host.
- **Banner Grabbing**: Retrieves basic information about running services.
- **Threading for Faster Scans**: Uses multi-threading to improve performance.
- **Report Generation**: Saves results to a text file in the `reports/` directory.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/NetworkRecon.git
   cd NetworkRecon
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script and provide a target IP or domain:
```bash
python network_recon.py
```

## Example Output
```
Starting network reconnaissance on 192.168.1.1...
Port 22/tcp is open. Banner: OpenSSH 8.2p1 Ubuntu 4ubuntu0.3
Port 80/tcp is open. Banner: Apache/2.4.41 (Ubuntu)
Scan completed in 2.45 seconds.
Report saved to reports/scan_report.txt
```

## Dependencies
- Python 3
- socket
- threading
- os

## Disclaimer
This tool is for educational purposes only. Use it legally and responsibly.
