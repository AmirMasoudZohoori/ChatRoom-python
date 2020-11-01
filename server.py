from socket import *
from threading import Thread


server_port = 1830
config_server = ('', server_port)


server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(config_server)
server_socket.listen()

clients = []
clients_name = []


def broadcast_message(message , c ):
    for client in clients:
        if client is not c:
            client.send(message.encode())


def get_message(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
            broadcast_message(message , client)
        except:
            index = clients.index(client)
            client.close()
            clients.remove(client)
            name = clients_name[index]
            clients_name.remove(name)
            break


def join_client():
    while True:

        client, info_client = server_socket.accept()
        print(f"the clinet {info_client} join in server chat")

        client.send("102457854210".encode())
        name = client.recv(1024)
        name= name.decode()
        clients_name.append(name)
        print(f"{name} join to chat ")
        clients.append(client)
        client.send("connected to chat ...".encode())
        thread = Thread(target=get_message, args=(client, ))
        thread.start()


if __name__ == "__main__":
    while True:
        try:
            print("server start ...")
            join_client()
        except:
            print("connection loss ...")
