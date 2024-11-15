from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set_value", methods=["POST"])
def set_value():
    new_value = request.form.get("new_value")
    if new_value is not None:
        try:
            new_value = int(new_value)
            cnt.set_value(new_value)
        except ValueError:
            pass
    return redirect("/")