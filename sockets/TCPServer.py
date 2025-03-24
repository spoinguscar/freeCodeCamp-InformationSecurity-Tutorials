#!/usr/bin/python3

import socket  # Import the socket module to create a server

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine's hostname
host = socket.gethostname()
port = 444  # Define the port number

# Bind the socket to the specified host and port
server_socket.bind((host, port))

# Start listening for incoming connections (maximum 3 clients in the queue)
server_socket.listen(3)

print(f"Server started on {host}:{port}")  # Inform that the server is running

while True:
    # Accept a new client connection
    client_socket, address = server_socket.accept()
    
    print(f"Connection established to {address}")
    
    # Send a welcome message to the client
    message = "Hello! Thank you for connecting to the server. This is an example of how sockets can be used.\n"
    client_socket.send(message.encode('ascii'))  # Encoding and sending the message
    
    # Close the connection with the client
    client_socket.close()