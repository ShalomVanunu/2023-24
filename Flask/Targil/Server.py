import socket
IP = "172.20.134.41"
PORT = 3060

server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET =Ipv4 | SOCK_STREAM- TCP
server_socket.bind((IP,PORT))
server_socket.listen()
client_obj, ip = server_socket.accept()
print(ip)

data = client_obj.recv(1024).decode()
print(data)
