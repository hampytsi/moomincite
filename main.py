from flask import Flask, redirect,url_for, render_template, request

app = Flask(__name__, template_folder='/Users/vladimirrukavisnikov/Documents/python_2021/templates')


@app.route("/", methods=["POST", "GET"])  # this sets the route to this page
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>", methods=["POST", "GET"])
def user(usr):
    if request.method == "POST":
        if request.form["pic"] == "книги":
            return render_template("mumi_papa.html")
        if request.form["pic"] == "цветы":
            return render_template("mumi_mama.html")
        if request.form["pic"] == "зонтик":
            return render_template("little_my.html")
    else:
        return render_template("opros.html")


if __name__ == "__main__":
    app.run()