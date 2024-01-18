import socket
import pickle

class PC:
    def __init__(self, name, age, some):
        self.name = name
        self.age = age
        self.some = some


if __name__ == "__main__":
    instance_class = PC("MICHAEL",17,['hello','world'])
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(('127.0.0.1',1234))
    instance_pickle_dump = pickle.dumps(instance_class)
    my_socket.listen(1)
    client_socket, client_tuple = my_socket.accept()

    client_socket.send(instance_pickle_dump)
