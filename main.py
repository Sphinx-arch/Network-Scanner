import socket
import ipaddress

def scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f"[+] Open:{ip}: {port} is open")
        s.close()
    except:
        pass

def main():
    ip = input("Enter the IP address/subnet: ")
    port = int(input("Enter the port number: "))

    try:
        # Handle the subnet or single IP address
        net = ipaddress.ip_network(ip, strict=False)
        for ip in net.hosts(): # Skips network and broadcast addresses
            scan(str(ip), port)
    except ValueError:
        # if it's not a subnet assume it's a single Ip address
        scan(ip, port)

if __name__ == "__main__":
    main()  
