"""Entry point for our twitoff flask app"""

from .app import create_app

#APP is global variable
APP = create_app()

#run this in the terminal FLASK_APP=TWITOFF:APP falsk run 
