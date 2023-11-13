import socket

#SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_IP = socket.gethostbyname_ex(socket.gethostname())

print(SERVER_IP)

