import socket

PORT = 80
IP = "192.168.1.188"
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

result = client_socket.connect_ex((IP,PORT))
if result == 0 :
    print(f"the port {PORT} is OPEN on {IP}" )
else:
    print(f"the port {PORT} is CLOSED on {IP}")