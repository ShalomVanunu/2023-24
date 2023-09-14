import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('172.20.130.69',3050))

file_content = open('text',"r")
data = file_content.read()

#data = input("Write data to server :")
client_socket.send(data.encode())

client_socket.close()
