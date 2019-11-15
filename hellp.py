"""Minimum flask app"""

from flask import Flask

#Make the application
app = Flask(__name__)

#Make the route

@app.route("/")

#now we define a function
def hello():
    return "Hello beautiful world!"
