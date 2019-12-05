from flask import Flask, render_template, url_for, flash, redirect
from forms import formulaireRegister, formulaireLogin, formulaireDb
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class brownie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    date = db.Column(db.Text,nullable=False,default=datetime.utcnow)
    title = db.Column(db.Text,nullable=False)


    def __init__()


