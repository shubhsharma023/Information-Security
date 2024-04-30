UPLOAD client.py
import socket

# Server configuration
SERVER_HOST = '127.0.0.1'  # Localhost
SERVER_PORT = 12345        # Port to connect to

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

try:
    while True:
        # Input command from the user
        command = input("Enter command (UPLOAD/DOWNLOAD): ").upper()
        if command not in ["UPLOAD", "DOWNLOAD"]:
            print("Invalid command. Please enter UPLOAD or DOWNLOAD.")
            continue
        filename = input("Enter filename: ")
        # Send the command and filename to the server
        client_socket.send(f"{command} {filename}".encode())
        if command == "UPLOAD":
            # Read file and send it to the server
            with open(filename, "rb") as f:
                file_data = f.read()
                client_socket.sendall(file_data)
            print("File", filename, "uploaded successfully.")
        elif command == "DOWNLOAD":
            # Receive file from the server and save it
            file_data = client_socket.recv(1024)
            if file_data == b"File not found.":
                print("File not found on server.")
            else:
                with open(filename, "wb") as f:
                    f.write(file_data)
                print("File", filename, "downloaded successfully.")
except KeyboardInterrupt:
    print("Client shutting down...")
    client_socket.close()
DOWNLOAD client.py