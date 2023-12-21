from flask import Flask,render_template,request
import ClientSocket
import socket
import threading

IP = "172.20.134.41"
PORT = 3060




app = Flask(__name__)



@app.route("/", methods = ["GET", "POST"])
def first_page():

    if request.method == "POST":
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((IP, PORT))
        name = request.form["Name"]
        phone = request.form["Phone"]
        email = request.form["Email"]
        print(name,phone,email)
        client_socket.send("shhs".encode())
        #object_socket.send(":".join([name,phone,email]).encode())
        return render_template("index.html")
    else:
        return render_template("index.html")

app.run(port =80,debug=True,host="172.20.134.41")