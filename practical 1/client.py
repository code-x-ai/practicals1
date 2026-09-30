import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to TCP Prime Server")
print("Enter an integer or type 'exit' to close.")

while True:
    number = input("Enter number: ")
    client_socket.send(number.encode())

    if number.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()
    print("Server:", response)

client_socket.close()
print("Connection closed.")