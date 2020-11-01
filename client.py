from socket import *
from threading import Thread

server_info = ("194.5.188.46", 1830)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_info)
name = input("Enter Your Name : ")


def get_message():
    while True:
        try:
            massage = client_socket.recv(1024).decode()
            if massage == "102457854210":
                client_socket.send(name.encode())

            elif massage != '':
                print(massage)
        except:
            client_socket.close()
            break


def send_massage():
    while True:
        c = input("")
        message = f'{name} : {c}'
        client_socket.send(message.encode())

		
send = Thread(target=send_massage)
get = Thread(target=get_message)

get.start()
send.start()
