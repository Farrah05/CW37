from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = "Farrah"
    return render_template("home.html",user_name=name )



