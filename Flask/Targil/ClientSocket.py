import socket



def init():
    IP = "192.168.1.144"
    PORT = 3050
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    return client_socket

def send_data(client_socket,data):
    client_socket.send(data.encode())



