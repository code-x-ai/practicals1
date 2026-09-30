import socket

HOST = "127.0.0.1"
PORT = 5000


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("TCP Prime Server")
print(f"Server listening on {HOST}:{PORT}")
print("Waiting for client...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

while True:
    data = client_socket.recv(1024).decode()

    if not data:
        break

    if data.lower() == "exit":
        break

    try:
        number = int(data)
        if is_prime(number):
            result = f"{number} is a PRIME number."
        else:
            result = f"{number} is NOT a prime number."
    except ValueError:
        result = "Invalid input. Please enter an integer."

    client_socket.send(result.encode())

client_socket.close()
server_socket.close()
print("Connection closed.")