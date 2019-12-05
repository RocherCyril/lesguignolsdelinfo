from flask import render_template, request
from flask import current_app as appero
from .models import db

@appero.route('/')
def gotohomard():
    return redirect(url_for('homard'))

@appero.route('/homard')
def homard():
    return "hello world"

#Exemple de routes 

""" @app.route('/notes/')
def notes():
    etudiants = Etudiant.query.all()
    return render_template('notes.html', etudiants = etudiants)

@app.route('/students/<int:post_id>')
def show_post(post_id):
    etudiants = Etudiant.query.filter_by(id=post_id)
    # show the post with the given id, the id is an integer
    return render_template('notes.html', etudiants = etudiants)
 """