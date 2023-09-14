import socket



server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET =Ipv4 | SOCK_STREAM- TCP

server_socket.bind(('172.20.130.69',3050))
server_socket.listen()

client_obj, ip = server_socket.accept()

print("ip :",ip)
print("obj client :",client_obj)
data = client_obj.recv(6000).decode()
print(data)
client_obj.close()
