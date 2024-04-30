import socket

HOST = '127.0.0.1'  
PORT = 65432     

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received:', repr(data.decode()))

while True:
    message_to_send = input("Enter your message: ")
    if message_to_send == 'exit':
        break
    send_message(message_to_send)
