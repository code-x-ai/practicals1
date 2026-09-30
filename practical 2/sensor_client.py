import socket

HOST = "127.0.0.1"
PORT = 5003

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("=" * 50)
print("IOT TEMPERATURE MONITORING CLIENT")
print("=" * 50)
print("Enter temperature readings.")
print("Type 'exit' to close.")
print("-" * 50)

while True:
    temperature = input("\nEnter temperature in C: ").strip()

    if not temperature:
        print("Please enter a temperature value.")
        continue

    if temperature.lower() == "exit":
        print("UDP client closed.")
        break

    client_socket.sendto(temperature.encode(), (HOST, PORT))
    response, server_address = client_socket.recvfrom(1024)

    print("Server Status:", response.decode())
    print("-" * 50)

client_socket.close()