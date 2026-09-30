import socket

HOST = "127.0.0.1"
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to TCP Chat Server")
print("Type 'exit' to end the chat.")

while True:
    message = input("Client: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    response = client_socket.recv(1024).decode()
    print("Server:", response)

    if response.lower() == "exit":
        break

client_socket.close()
print("Chat connection closed.")