from flask import Flask, render_template

app = Flask(__name__)

name = "moshe"
list_names = ["moshe", "shalom", "Itzik"]
@app.route("/")
def first_page():
    return render_template("index.html", name=name,listnames = list_names)

@app.route("/bank")
def bank_hapoalim():
    return "<h1>hello</h1>"

if __name__ == "__main__":
    app.run(port =80,debug=True,host="172.20.129.23")