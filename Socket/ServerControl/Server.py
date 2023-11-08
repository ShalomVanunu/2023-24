import time
import socket
import threading

SERVER_IP = "192.168.1.120"
SERVER_PORT = 6060
clients_objects =[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP,SERVER_PORT))
server_socket.listen()
print(" Waiting for clients......")


def clients_handle():
    while True :
        control_data = input(" Write Command -> \n")
        for client in clients_objects:
            client.send(control_data.encode())
            received_data = client.recv(1024).decode()
            print(received_data)


while True:
    client_object, client_IP_PORT = server_socket.accept()
    clients_objects.append(client_object)
    client_object.send("Wellcome to Control Server....".encode())
    client_th = threading.Thread(target=clients_handle)
    client_th.start()
