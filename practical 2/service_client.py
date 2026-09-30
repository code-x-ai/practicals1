import socket

HOST = "127.0.0.1"
PORT = 5002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("=" * 55)
print("UDP NETWORK SERVICE LOOKUP CLIENT")
print("=" * 55)
print("Available services:")
print("1. DNS")
print("2. DHCP")
print("3. HTTP")
print("4. HTTPS")
print("5. SSH")
print("6. NTP")
print("\nType 'exit' to close the client.")
print("-" * 55)

while True:
    service_name = input("\nEnter service name: ").strip()

    if not service_name:
        print("Please enter a service name.")
        continue

    if service_name.lower() == "exit":
        print("UDP client closed.")
        break

    client_socket.sendto(service_name.encode(), (HOST, PORT))
    response, server_address = client_socket.recvfrom(2048)

    print("\n" + "-" * 55)
    print("SERVER RESPONSE")
    print("-" * 55)
    print(response.decode())
    print("-" * 55)

client_socket.close()