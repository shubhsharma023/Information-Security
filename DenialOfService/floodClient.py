import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send flooding messages to the server
while True:
    message = "Flooding the server!"
    client_socket.send(message.encode())

# Close the connection
client_socket.close()
