from flask import Flask, render_templates

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("homeclone.html")