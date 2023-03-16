import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('172.20.147.241',5050))

data = input("Write data to server :")
client_socket.send(data.encode())

client_socket.close()
