import socket

HOST = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("TCP Chat Server")
print(f"Server listening on {HOST}:{PORT}")
print("Waiting for client...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)
print("Type 'exit' to end the chat.")

while True:
    message = client_socket.recv(1024).decode()

    if not message:
        break

    if message.lower() == "exit":
        print("Client ended the chat.")
        break

    print("Client:", message)

    reply = input("Server: ")
    client_socket.send(reply.encode())

    if reply.lower() == "exit":
        break

client_socket.close()
server_socket.close()
print("Chat connection closed.")