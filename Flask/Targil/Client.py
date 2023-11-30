from flask import Flask,render_template,request
import threading
import ClientSocket


object_socket  = ClientSocket.init_socket()



app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def first_page():
    if request.method == "POST":
        name = request.form["Name"]
        phone = request.form["Phone"]
        email = request.form["Email"]
        ClientSocket.send("hello")
        #object_socket.send(":".join([name,phone,email]).encode())
        return render_template("index.html")
    else:
        return render_template("index.html")


app.run(port =80,debug=True,host="172.20.134.41")