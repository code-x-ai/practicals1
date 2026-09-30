import socket

HOST = "127.0.0.1"
PORT = 5003

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("=" * 50)
print("UDP IOT TEMPERATURE MONITORING SERVER")
print("=" * 50)
print(f"Server running on {HOST}:{PORT}")
print("Waiting for temperature readings...")
print("-" * 50)

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode().strip()

    try:
        temperature = float(message)

        if temperature < 0:
            status = "ALERT: Extremely Low Temperature"
        elif temperature < 15:
            status = "LOW Temperature"
        elif temperature <= 35:
            status = "NORMAL Temperature"
        elif temperature <= 45:
            status = "WARNING: High Temperature"
        else:
            status = "CRITICAL: Immediate Attention Required"

    except ValueError:
        status = "Invalid temperature value."

    server_socket.sendto(status.encode(), client_address)
    print(f"Temperature received: {message} C")
    print(f"Status sent: {status}")
    print("-" * 50)