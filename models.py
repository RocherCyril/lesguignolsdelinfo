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

    def init_db():
    lg.warning('Suppression des tables existantes...')
    db.drop_all()
    lg.warning('Création des tables...')
    db.create_all()
    lg.warning('Création du jeu de données...')
    #db.session.add(Etudiant("Ben Jaafar","Imen",15.5,11))
    #db.session.add(Etudiant("Yete","Hona",14.5,12))
    #db.session.add(Etudiant("Errami","Abdeljalil",12.5,6))
    lg.warning('Enregistrement...')
    db.session.commit()
    lg.warning('Base de donnée initialisée')

db.create_all()




