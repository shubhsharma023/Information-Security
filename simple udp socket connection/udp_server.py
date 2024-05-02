import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('',2000))

message, address=server.recvfrom(1024)
print(message.decode('utf-8'))
server.sendto("Hello World from server".encode('utf-8'),address)