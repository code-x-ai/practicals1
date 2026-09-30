import socket

HOST = "127.0.0.1"
PORT = 5002   # Corrected: client also uses 5002

services = {
    "DNS": {
        "name": "Domain Name System",
        "port": "53",
        "protocol": "UDP/TCP",
        "purpose": "Translates domain names into IP addresses."
    },
    "DHCP": {
        "name": "Dynamic Host Configuration Protocol",
        "port": "67/68",
        "protocol": "UDP",
        "purpose": "Automatically assigns IP addresses and network configuration."
    },
    "HTTP": {
        "name": "Hypertext Transfer Protocol",
        "port": "80",
        "protocol": "TCP",
        "purpose": "Transfers web pages and other web resources."
    },
    "HTTPS": {
        "name": "Hypertext Transfer Protocol Secure",
        "port": "443",
        "protocol": "TCP",
        "purpose": "Provides secure and encrypted web communication."
    },
    "SSH": {
        "name": "Secure Shell",
        "port": "22",
        "protocol": "TCP",
        "purpose": "Provides secure remote access to computers and servers."
    },
    "NTP": {
        "name": "Network Time Protocol",
        "port": "123",
        "protocol": "UDP",
        "purpose": "Synchronizes the time of computers and network devices."
    }
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("=" * 55)
print("UDP NETWORK SERVICE LOOKUP SERVER")
print("=" * 55)
print(f"Server running on {HOST}:{PORT}")
print("Available services:")
for service_name in services:
    print("-", service_name)
print("\nWaiting for client requests...")
print("Press CTRL + C to stop the server.")
print("-" * 55)

while True:
    data, client_address = server_socket.recvfrom(1024)
    request = data.decode().strip()

    print("\nRequest received from:", client_address)
    print("Service requested:", request)

    service_name = request.upper()

    if service_name in services:
        service = services[service_name]
        response = (
            f"Service Name: {service['name']}\n"
            f"Default Port: {service['port']}\n"
            f"Transport Protocol: {service['protocol']}\n"
            f"Purpose: {service['purpose']}"
        )
    else:
        response = (
            f"Service '{request}' was not found.\n"
            "Available services: DNS, DHCP, HTTP, HTTPS, SSH, NTP"
        )

    server_socket.sendto(response.encode(), client_address)
    print("Response sent successfully.")
    print("-" * 55)