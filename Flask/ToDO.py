from flask import Flask, render_template,request
import os

app = Flask(__name__)

def run_ping(ip):
    ping_result = os.popen(f"ping {ip}").read()
    return ping_result

@app.route("/", methods=['GET','POST'])
def TODO ():
    if request.method == "POST":
       ip = request.form["ip"]
       return render_template("ToDoButton.html", ip= run_ping(ip))
    else:
        return render_template("ToDoButton.html" , ip="")



if __name__ == "__main__":
    app.run(port =8080,debug=True,host="172.20.129.23")


