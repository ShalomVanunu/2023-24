
import os
import socket

PORT = 5566
#IP = socket.gethostbyname(socket.gethostname()) # get IP of server generic
IP = "172.20.133.7"
FILE_NAME  = "326493905.zip"

def get_file_data_info():
    with open(FILE_NAME, "rb") as file:
        data_file = file.read()
    file_size = os.path.getsize(FILE_NAME)
    return data_file,file_size



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((IP,PORT))
server_socket.listen()
print(" Waiting for client...")

client_obj, ip_port = server_socket.accept()
print("The Client Connected is..",ip_port)

data_file,file_size = get_file_data_info()

#client_obj.send((FILE_NAME,file_size))
client_obj.send((FILE_NAME+":"+str(file_size)).encode())

accept = client_obj.recv(1024).decode() # recv OK
if accept :
    client_obj.send(data_file)
accept = client_obj.recv(1024).decode()
if accept == "FileOK":
    print("File Transfer Successfully")
    client_obj.close()













