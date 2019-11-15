"""Minimum flask app"""

from flask import Flask, render_template

#Make the application
app = Flask(__name__)

#Make the route

@app.route("/")

#now we define a function
def hello():
    return render_template('home.html')


#creating another route
@app.route("/about")
def preds():
    return render_template('about.html')
