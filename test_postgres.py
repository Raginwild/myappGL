#test injection de données dans la base de données 
import psycopg2
from tabulate import tabulate
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import pandas as pd
from db_set import DB_PARAM
from abc import ABC


DATABASE_URL = f"postgresql://{DB_PARAM.get('user')}:{DB_PARAM.get('password')}@{DB_PARAM.get('host')}/{DB_PARAM.get('dbname')}"

# Création d'une instance SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

# Définition des modèles
class Personne(ABC):
    pass
class Utilisateur(Personne):
    __tablename__ = 'utilisateurs'
    id_user = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String, unique=True)
"""
class Client(Personne):
    __tablename__='clients'
    id_cli = Column(Integer, primary_key=True)
    nom = Column(String)
    montant_achat = Column(Integer)
    nb_enfant = Column(Integer)
    ville = Column(String)
    cat_sociopro = Column(String)
    collecte_id = Column(Integer, ForeignKey('collectes.id_collecte'))

    collecte = relationship('Collecte', back_populates='clients')

class Collecte(Base):
    __tablename__ = 'collectes'
    id_collecte = Column(Integer, primary_key=True)
    collecte_id = Column(Integer, ForeignKey('produits.id_produit'))

    collecte = relationship('Produit', back_populates='collecte')

class Produit(Base):
    __tablename__ = 'produits'
    id_produit = Column(Integer, primary_key=True)
    nom = Column(String)
    categorie_produit = Column(String)
    prix = Column(Float)

# Ajout de la relation inverse pour les foreign keys
Collecte.clients = relationship('Client', order_by=Client.id_cli, back_populates='utilisateur')
Produit.collecte = relationship('Collecte', order_by=Collecte.id_collecte, back_populates='collectes')
"""

# Création des tables dans la base de données
Base.metadata.create_all(engine)

#chargement de données fictives dans la database
def insertion_enregistrements():
    df_insert=pd.read_csv('user_test.csv', sep=';')
    print(df_insert)
    df_insert.to_sql('utilisateurs', engine, index=False, if_exists='append')
    print('les lignes ont bien été enregistrées')


# Visualisation des tables avec Pandas
def afficher_tables():
    tables = ['utilisateurs']
    for t in tables:
        query = f"SELECT * FROM {t};"
        df = pd.read_sql_query(query, engine)
        print(f"\nContenu de la table {t}:\n{df}")



if __name__=='__main__':
    insertion_enregistrements()
    afficher_tables()