from flask import Flask,render_template,request
import threading
import socket
import ClientSocket

app = Flask(__name__)

IP = "192.168.1.144" # of Flask Server


@app.route("/", methods = ["GET", "POST"])
def first_page():

    if request.method == "POST":
        name = request.form["Name"]
        phone = request.form["Phone"]
        email = request.form["Email"]
        data = ":".join([name,phone,email])
        print(type(data))
        ClientSocket.send_socket_data(data)
        #client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #client_socket.connect((IP, PORT))
        #client_socket.send(":".join([name,phone,email]).encode())

    return render_template("index.html")



app.run(port =80,debug=True,host=IP)