

def send_socket_data(data):
    import socket
    IP = "192.168.1.144"
    PORT = 6050
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    client_socket.send(data.encode())
    print(client_socket.recv(1024).decode())



