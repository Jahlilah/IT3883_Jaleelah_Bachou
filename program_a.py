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

server_ip = "127.0.0.1"
port = 45000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

user_input = input("Type something to send: ")
client.send(user_input.encode())

reply = client.recv(1024).decode()

print("Received from Program B:", reply)

client.close()
