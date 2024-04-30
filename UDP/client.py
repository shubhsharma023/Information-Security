import socket

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message == 'exit':
                break
            s.sendto(message.encode(), (HOST, PORT))
            data, addr = s.recvfrom(1024)
            print(f"Received from server at {addr}: {data.decode()}")

if __name__ == "__main__":
    start_client()
