import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = ''
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

# Function to handle client connections
def handle_client(client_socket):
    print("Connected to {}".format(client_socket.getpeername()))
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received from client: {}".format(data.decode()))

    # Close the connection
    client_socket.close()

# Accept connections from clients
while True:
    # Wait for a connection
    client_socket, addr = server_socket.accept()
    print("Got connection from {}".format(addr))

    # Handle the client in a separate thread or process
    handle_client(client_socket)
