import threading
import socket

host='127.0.0.1' #localhost
port=55555

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Bind the server to a specific address and port number
server.bind((host,port))

#Maximum number of clients that can connect to the server at once
server.listen() #clients can connect to the server simultaneously
print("Server is running on host: ",host)   #print the host address
print("Server is listening on port: ",port)  #print the port number

clients=[]
nicknames=[]


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address=server.accept()
        print(f"Connected with {str(address)}")

        client.send('PRIMUS'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

print('Server is listening...')
receive()