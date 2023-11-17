# app.py
# fichier back-end de l'application 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model_insert import insert_csv
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_PARAM.get('user')}:{DB_PARAM.get('password')}@{DB_PARAM.get('host')}/{DB_PARAM.get('dbname')}"
db = SQLAlchemy(app)

#modèles (tables) d'utilisateur avec ORM
class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Utilisateur(db.Model):
    id_user = db.Column(Integer, primary_key=True)
    nom = db.Column(String)
    email = db.Column(String, unique=True)

class Client(db.Model):
    id_cli = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    date_passage = nb.Column(db.Datetime, default=datetime.utcnow)
    nb_enfant = db.Column(db.Integer)
    ville = db.Column(db.String)
    cat_sociopro = db.Column(db.String)
    collectes = db.relationship('Collecte', backref='client', lazy=True)

class Collecte(db.Model):
    id_collecte = db.Column(db.Integer, primary_key=True)
    commandes = db.relationship('Client', backref='collecte', lazy=True)
    id_cli = db.Column(db.Integer, db.ForeignKey('client.id_cli'), nullable=False)
    produits = db.relationship('Produit', backref='collecte', lazy=True)

class Produit(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    prix = db.Column(db.Float, nullable=False)
    id_collecte = db.Column(db.Integer, db.ForeignKey('collecte.id_collecte'), nullable=False)

#insertions des données socles dans la base de données SQL

#routes pour l'accès aux différentes pages 
@app.route('/index')


@app.route('/login')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)