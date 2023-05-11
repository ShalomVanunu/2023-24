import socket


# define Object Socket
server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET =Ipv4 | SOCK_STREAM- TCP

server_socket.bind(('172.20.133.7',5050)) # Define Listener
server_socket.listen()
print("Waiting for Client..........")

client_obj, ip = server_socket.accept() #object Client | IP+Port Client
print(f"the ip of the client is  :{ip[0]}")
while True:
    data = client_obj.recv(1024).decode()# recieve data byte
    print(data)
    data = input("Write back :")
    client_obj.send(data.encode())

client_obj.close()
