import socket

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6543))
server.listen()

while True:
    client,address=server.accept()
    print(f"Connection from {address}")
    print(client.recv(1024).decode('utf-8'))
    client.send("Hello World".encode('utf-8'))
    client.close()