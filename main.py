from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<int:num>")
def kto(num):
    if num == 1:
        return render_template("True.html")
    if num == 2:
        return render_template("True.html")


@app.route("/instruction")
def instruction():
    return render_template("Instruction.html")


@app.route("/Gorod_1")
def Gorod_1():
    return render_template("Gorod_1.html")


@app.route("/Gorod_2")
def Gorod_2():
    return render_template("Gorod_2.html")


@app.route("/Gorod_3")
def Gorod_3():
    return render_template("Gorod_3.html")


@app.route("/Gorod_4")
def Gorod_4():
    return render_template("Gorod_4.html")


@app.route("/Gorod_5")
def Gorod_5():
    return render_template("Gorod_5.html")


@app.route("/Verno")
def verno():
    return render_template("Verno.html")


if __name__ == '__main__':
    app.run()