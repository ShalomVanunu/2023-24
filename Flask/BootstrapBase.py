from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def first_page():
    return render_template("BootstrapTest.html")

if __name__ == "__main__":
    app.run(port =8080,debug=True,host="172.20.129.23")