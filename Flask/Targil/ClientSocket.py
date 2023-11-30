import socket

IP = "172.20.134.41"
PORT = 3050
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def init_socket():
    client_socket.connect((IP,PORT))
    return client_socket

def send(data):
    client_socket.send(data.encode())
