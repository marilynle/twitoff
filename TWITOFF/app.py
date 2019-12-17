"""Code for our app"""

from flask import Flask

# Make our app factory

def creat_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Welcome to twitoff!!"
    return app
        
