from flask import Flask
from flask import render_template
from flask import abort
from sufee import app

@app.route("/")
@app.route("/home")
def index():
    template = 'index.html'
    return render_template(template)

@app.route("/login")
def login():
    template = "page-login.html"
    return render_template(template)


# @app.route("/about")
# def aboutindex():
#     template = 'about.html'
#     return render_template(template)
#