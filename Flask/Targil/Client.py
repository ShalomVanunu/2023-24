from flask import Flask,render_template,request
import threading
import socket
import ClientSocket

app = Flask(__name__)

IP = "192.168.1.144"
PORT = 6050




@app.route("/", methods = ["GET", "POST"])
def first_page():

    if request.method == "POST":
        name = request.form["Name"]
        phone = request.form["Phone"]
        email = request.form["Email"]
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        client_socket.send(":".join([name,phone,email]).encode())
        print(client_socket.recv(1024).decode())
    return render_template("index.html")



app.run(port =80,debug=True,host=IP)