import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',6543))

client.send("Hello World".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))