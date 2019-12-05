from flask import Flask, render_template, url_for, flash, redirect
from forms import formulaireRegister, formulaireLogin, formulaireDb
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from AwesomeProject import create_app

#appero = Flask(__name__) fait dans le init.py
appero = create_app()

appero.config['SECRET_KEY'] = 'paella55156tartiflette565'




@appero.route('/')
def gotohomard():
    return redirect(url_for('homard'))

@appero.route('/homard')
def homard():
    return "hello world"


if __name__== "__main__":
    db.drop_all()
    db.create_all()
    appero.run(debug=True)
    
