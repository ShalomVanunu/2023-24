from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def TODO ():
    if request.method == "POST":
       ip = request.form["ip"]
       return render_template("ToDoButton.html", ip= ip)
    else:
        return render_template("ToDoButton.html" , ip="")



if __name__ == "__main__":
    app.run(port =8080,debug=True,host="172.20.129.109")


