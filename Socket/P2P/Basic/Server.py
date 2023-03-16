import socket



server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET =Ipv4 | SOCK_STREAM- TCP

server_socket.bind(('172.20.147.241',5050))
server_socket.listen()

client_obj, ip = server_socket.accept()

data = client_obj.recv(1024).decode()
print(data)
client_obj.close()
