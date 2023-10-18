import socket

CLIENT_IP = "192.168.1.120"
CLIENT_PORT = 6060

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((CLIENT_IP,CLIENT_PORT))

while True:
    data_receive = client_socket.recv(1024).decode()
    print(data_receive)
    client_socket.send("ACK2".encode())