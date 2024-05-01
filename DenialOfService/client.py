import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send messages to the server
while True:
    message = input("Enter message to send (type 'quit' to exit): ")
    if message == 'quit':
        break
    client_socket.send(message.encode())

# Close the connection
client_socket.close()
