
import socket

PORT = 4444
SERVER = "172.20.129.35"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((SERVER,PORT))

while True:
    data_receive = client.recv(1024).decode()
    print(f" {data_receive}")
    client.send("Client1 received".encode())
