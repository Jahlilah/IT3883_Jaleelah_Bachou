# Program Name: program_a.py
# Course: IT3883/Section 01
# Student Name: Jaleelah Bachou
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: This program asks the user to enter a string, sends that string
# to Program B through a socket connection, waits for the response, and
# prints the returned message to the screen.
# Resources Used: Class notes, lecture examples, and general debugging

import socket

# Store the server IP address and port number
server_ip = "127.0.0.1"
port = 45000

# Create a client socket using IPv4 and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect this program to Program B
client.connect((server_ip, port))

# Ask the user to type a message
user_input = input("Type something to send: ")

# Send the user's message to Program B
client.send(user_input.encode())

# Receive the response from Program B
reply = client.recv(1024).decode()

print("Received from Program B:", reply)

client.close()
