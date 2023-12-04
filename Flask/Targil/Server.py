import socket
import threading
import DBHandle

IP = "192.168.1.144"
PORT = 6050

server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET =Ipv4 | SOCK_STREAM- TCP
server_socket.bind((IP,PORT))
server_socket.listen()

while True:
    client_obj, ip = server_socket.accept()
    data = client_obj.recv(1024).decode()
    name,phone,email = data.split(":")[0],data.split(":")[1],data.split(":")[2]
    try:
        DBname= 'DB.db'
        sql = f"INSERT INTO users VALUES ('{name}', '{phone}', '{email}')"
        DBHandle.create_in_db(DBname, sql)
        print("DB Updated....")
        client_obj.send("OK".encode())
    except:
        print("Error")
        client_obj.send("BAD".encode())

