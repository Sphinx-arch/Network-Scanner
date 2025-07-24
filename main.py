import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---- Scan a single port ----
def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)  # short timeout = faster scanning
        s.connect((ip, port))
        return port
    except:
        return None
    finally:
        s.close()

# ---- Scan a list of ports using threads ----
def scan_ports(ip, port_range=(1, 1024), max_threads=100):
    open_ports = []

    print(f"\n[🔍] Scanning {ip} from port {port_range[0]} to {port_range[1]}...")

    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(port_range[0], port_range[1] + 1)]

        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
                print(f"[+] Port {result} is OPEN")

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"\n✅ Scan complete. Open ports: {open_ports}")

# ---- Main Logic ----
if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ").strip()
    start_port = int(input("Enter start port (e.g. 1): ").strip())
    end_port = int(input("Enter end port (e.g. 1024): ").strip())

    scan_ports(target_ip, (start_port, end_port))
