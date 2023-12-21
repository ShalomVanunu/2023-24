from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1> Hi, Wellcome My First Page </h1>"

@app.route("/name")
def my_name():
    return "<h2> My name is Shalom </h2>"

if __name__ == "__main__":
    app.run(port =80,debug=True,host="192.168.1.144")