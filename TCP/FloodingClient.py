import socket

HOST = '127.0.0.1'  
PORT = 65432     

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received:', repr(data.decode()))

def start_flood():
    while True:
        message = "Flood" # Construct a large message
        send_message(message)

if __name__ == "__main__":
    start_flood()
