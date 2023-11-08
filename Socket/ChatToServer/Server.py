import socket
import threading

PORT = 5050
MSG_LENGTH = 1024
#SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_IP = "172.20.129.8"
DISCONNECT_MESSAGE = "Bye"
Obj_Clients = []
Username_Clients = []


def handle_clients(client_obj,client_addr, username):
    print(f"The Client {client_addr[0]} is connected")
    connect = True
    while connect:
        msg = client_obj.recv(MSG_LENGTH).decode()
        if msg == DISCONNECT_MESSAGE:
            connect = False
        print(f"{username} : {msg}")
        client_obj.send("Msg recived".encode())


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP,PORT))
    server.listen()
    print(f"Server in listening....on {SERVER_IP} on port {PORT}")
    while True:
        client_obj, client_addr = server.accept()
        Obj_Clients.append(client_obj)
        username = client_obj.recv(MSG_LENGTH).decode()
        Username_Clients.append(username)
        client_obj.send("Welcome to Server".encode())
        th = threading.Thread(target=handle_clients ,args=(client_obj,client_addr, username))
        th.start()
        print(f"Active Connections {threading.active_count() -1}")


if __name__ == "__main__":
    main()








