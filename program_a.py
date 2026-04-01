import socket

server_ip = "127.0.0.1"
port = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

user_input = input("Type something to send: ")
client.send(user_input.encode())

reply = client.recv(1024).decode()

print("Received from Program B:", reply)

client.close()
