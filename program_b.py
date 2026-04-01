# Program Name: program_b.py
# Course: IT3883/Section 01
# Student Name: Jaleelah Bachou
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: This program waits for a connection from Program A, receives a
# string, changes the string to uppercase, prints it, and sends it back
# to Program A.
# Resources Used: Class notes, lecture examples, and general debugging 

import socket

# Store the host IP address and port number
host = "127.0.0.1"
port = 45000

# Create a server socket using IPv4 and TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the selected host and port
server.bind((host, port))

# Listen for one incoming connection
server.listen(1)
print("Waiting for connection...")

# Accept the connection from Program A
conn, addr = server.accept()
print("Connected to:", addr)

# Receive the message from Program A
data = conn.recv(1024).decode()

# Convert the message to uppercase
upper_data = data.upper()

print("Uppercase message:", upper_data)

# Send the uppercase message back to Program A
conn.send(upper_data.encode())

conn.close()
server.close()
