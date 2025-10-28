"""
Port Scanner Tool
Author: Edward Hudson Jr.
Version: 1.0
Description:
    A lightweight Python tool to scan for open ports on a target host.
    Useful for network diagnostics and cybersecurity education.
"""

import socket
from datetime import datetime

# Function to perform a simple port scan
def scan_ports(target_host, start_port=1, end_port=1024):
    print(f"\n🔍 Scanning Target: {target_host}")
    print(f"📅 Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                open_ports.append(port)
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"✅ Port {port} is open ({service})")
            sock.close()
    except KeyboardInterrupt:
        print("\n⛔ Scan stopped by user.")
        return
    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        return
    except socket.error:
        print("❌ Could not connect to server.")
        return

    print("-" * 50)
    print(f"Scan complete. {len(open_ports)} open ports found.")
    if open_ports:
        print("🟢 Open Ports:", open_ports)
    print(f"📅 End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)


# Main program
def main():
    print("🔐 Simple Port Scanner (Educational Use Only)")
    print("=" * 50)
    target = input("Enter target host (IP or domain): ")
    start_port = int(input("Enter start port (default 1): ") or 1)
    end_port = int(input("Enter end port (default 1024): ") or 1024)
    scan_ports(target, start_port, end_port)


if __name__ == "__main__":
    main()
