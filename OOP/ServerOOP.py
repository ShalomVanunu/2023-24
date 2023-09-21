
import socket
import threading

class ChatServer:



    def __init__(self,IP,PORT):
        self.IP =IP
        self.PORT =PORT
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.IP, self.PORT))
        self.server.listen()
        print("SERVER is waiting for clients")
        self.list_of_obj_clients = []
        self.list_of_ip_clients = []

    def connection(self):
        for conn_obj in self.list_of_obj_clients:
            conn_obj.send("Wellcome to Shalom Server".encode())
            data_recieve = conn_obj.recv(1024).decode()
            print(f"{data_recieve}")

    def get_clients(self):
        while True:
            try:
                self.conn_obj, self.conn_address = self.server.accept()
                self.list_of_ip_clients.append(self.conn_address)
                self.list_of_obj_clients.append(self.conn_obj)
                print(self.list_of_ip_clients)
                conn_thread = threading.Thread(target=self.connection)
                conn_thread.start()
            except:
                print("Client Error")

server1 = ChatServer("172.20.129.27", 4444)
server1.get_clients()
