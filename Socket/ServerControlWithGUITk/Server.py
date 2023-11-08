import time
import socket
import threading
from tkinter import *

SERVER_IP = "192.168.1.120"
SERVER_PORT = 6060
clients_objects =[]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP,SERVER_PORT))
server_socket.listen()
print(" Waiting for clients......")

def main():


    while True:
        client_object, client_IP_PORT = server_socket.accept()
        clients_objects.append(client_object)
        client_object.send("Wellcome to Control Server....".encode())


if __name__ == "__main__":
    main_th = threading.Thread(target=main)
    main_th.start()

    app = Tk()
    app.title("Control Server")
    app.geometry("450x300")
    app.resizable(False, False)

    label1 = Label(app, text="Control Server", font=('Ariel Bold', 20))
    label1.pack()
    label2 = Label(app, text="Command", font=('Ariel Bold', 12))
    label2.pack()
    entry1 = Entry(app, font=('Ariel Bold', 12))
    entry1.pack()
    def send_data():
        for client in clients_objects:
            client.send(entry1.get().encode())
            received_data = client.recv(1024).decode()
            text1.insert(INSERT,received_data )
            #print(received_data)

    button1 = Button(app, text="Send", font=('Ariel Bold', 10), command=send_data)
    button1.pack()

    text1 = Text(app)
    text1.pack()

    app.mainloop()

