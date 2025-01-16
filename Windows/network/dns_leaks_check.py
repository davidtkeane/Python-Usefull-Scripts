import socket

def check_dns_leak(domain):
    try:
        # Resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain)
        
        # Compare the resolved IP address with the expected DNS server IP
        if ip_address == "156.146.54.84":
            print(f"No DNS Leak detected. Resolved IP: {ip_address}")
        else:
            print(f"DNS Leak detected! Resolved IP: {ip_address}")
    except socket.gaierror as e:
        print(f"Error resolving DNS: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace "your_dns_server_ip" with the IP of your DNS server
check_dns_leak("example.com")
