# Server
import socket
import tqdm
import os

SEPERATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# create the server socket
# TCP socket
s = socket.socket()

# bind the socket to a public host, and a well-known port
s.bind(("", 5001))

# become a server socket
s.listen(5)
print("[+] Listening as {}".format(s.getsockname()))

# accept connections and process them
client_socket, address = s.accept()
print("[+] {} connected.".format(address))

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPERATOR)

# remove absolute path if there is
filename = os.path.basename(filename)

# convert to integer
filesize = int(filesize)

# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for _ in progress:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()
