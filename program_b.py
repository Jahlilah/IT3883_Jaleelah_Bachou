import socket

host = "127.0.0.1"
port = 45000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

data = conn.recv(1024).decode()

upper_data = data.upper()

print("Uppercase message:", upper_data)

conn.send(upper_data.encode())

conn.close()
server.close()
