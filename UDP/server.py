import socket

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode().strip()
            print(f"Received from client at {addr}: {message}")
            if message == "exit":
                break
            s.sendto(data, addr)

if __name__ == "__main__":
    start_server()
