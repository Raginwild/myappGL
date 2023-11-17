#modèles (tables) d'utilisateur avec ORM
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    id_fonction = db.Column(db.String, unique=True)

class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    date_passage = db.Column(db.DateTime, default=datetime.utcnow)
    nb_enfant = db.Column(db.Integer)
    ville = db.Column(db.String)
    cat_sociopro = db.Column(db.String)
    collectes = db.relationship('Collecte', backref='client', lazy=True)

class Collecte(db.Model):
    id_collecte = db.Column(db.Integer, primary_key=True)
    commandes = db.relationship('Client', backref='collecte', lazy=True)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id_client'), nullable=False)
    produits = db.relationship('Produit', backref='collecte', lazy=True)

class Produit(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    cat_produit = db.Column(db.String(90))
    prix = db.Column(db.Float, nullable=False)
    id_collecte = db.Column(db.Integer, db.ForeignKey('collecte.id_collecte'), nullable=False)
