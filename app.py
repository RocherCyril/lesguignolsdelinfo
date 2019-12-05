from flask import Flask
from flask_sqlalchemy import SQLAlchemy

appero = Flask(__name__)

appero.config['SECRET_KEY'] = 'paella55156tartiflette565'

@appero.route('/')
def home():
    return "hello world"


if __name__== "__main__":
    appero.run(debug=True)
    
