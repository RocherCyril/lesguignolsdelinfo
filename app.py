from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

appero = Flask(__name__)

appero.config['SECRET_KEY'] = 'paella55156tartiflette565'

@appero.route('/')
def gotohomard():
    return redirect(url_for('homard'))

@appero.route('/homard')
def homard():
    return "hello world"


if __name__== "__main__":
    appero.run(debug=True)
    
