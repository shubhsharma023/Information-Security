import socket

client= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto("Hello World from client".encode('utf-8'),('10.0.2.15',2000))

print(client.recvfrom(1024)[0].decode('utf-8'))