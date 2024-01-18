import pickle
import socket
from PickleDemo.ex_pickle_client import PC
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(('127.0.0.1',1234))

recv_dumps = my_socket.recv(1024)
PC_instance:PC = pickle.loads(recv_dumps)
print('received',PC_instance.name,PC_instance.age, PC_instance.some)

my_socket.close()