# app.py
# fichier back-end de l'application 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from model_insert import insert_csv

from datetime import datetime
from app.statics.db_set import DB_PARAM

import psycopg2
import plotly.express as px

from app.models import db, User, Client, Collecte,Produit  #importation du db depuis le fichier models.py
from config import DevelopmentConfig, ProductionConfig #fichier de configuration de l'application

import pandas as pd

#traitement des graphiques plus poussés
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64


conn = psycopg2.connect(
    host=DB_PARAM.get('host'),
    database=DB_PARAM.get('dbname'),
    user=DB_PARAM.get('user'),
    password=DB_PARAM.get('password')
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
bootstrap = Bootstrap(app)

db.init_app(app)

with app.app_context():
   
    db.create_all()

#routes pour l'accès aux différentes pages 
@app.route('/')
def index():
    csv_path='client_table.csv'
    csv_path2='collectes_table.csv'
    csv_path3='user_table.csv'
    csv_path4='produits_table.csv'

    if csv_path:
        # Lire le fichier CSV avec pandas
            df = pd.read_csv(csv_path, sep=";")

            # Ajouter les données à la base de données
            cursor = conn.cursor()

            
            for index, row in df.iterrows():
                id_row = Client.query.filter_by(id_client=int(row['id_client'])).first()
                if not id_row:
                
                    cursor.execute("INSERT INTO client (id_client, date_passage, nb_enfant, ville, cat_sociopro)\
                                    VALUES (%s, %s, %s, %s, %s);", (row['id_client'], row['date_passage'],row['nb_enfant'], row['ville'],\
                                                                    row['cat_sociopro']))

            conn.commit()
            cursor.close()

    if csv_path2:
        # Lire le fichier CSV avec pandas
            df = pd.read_csv(csv_path2, sep=";")

            # Ajouter les données à la base de données
            cursor = conn.cursor()

            
            for index, row in df.iterrows():
                id_row = Collecte.query.filter_by(id_collecte=int(row['id_collecte'])).first()
                if not id_row:
            
                    cursor.execute("INSERT INTO collecte (id_collecte, id_client) \
                                    VALUES (%s, %s);", (int(row['id_collecte']),int(row['id_client'])))
                                                    

            conn.commit()
            cursor.close()
    """
    if csv_path3:
        # Lire le fichier CSV avec pandas
            df = pd.read_csv(csv_path3, sep=";")

            # Ajouter les données à la base de données
            cursor = conn.cursor()

            
            for index, row in df.iterrows():
                id_row = User.query.filter_by(id_user=int(row['id_user'])).first()
                if not id_row:
    
                    cursor.execute("INSERT INTO user (id_user, username, email, id_fonction) \
                                    VALUES (%s, %s, %s, %s);", (row['id_user'], row['username'],row['email'], row['id_fonction']))
                                                                   

            conn.commit()
            cursor.close()
"""



    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client;")
    data = cursor.fetchall()
    cursor.close()

    columns = ['id_client', 'date_passage', 'nb_enfant', 'ville', 'cat_sociopro']
    df = pd.DataFrame(data, columns=columns)

    # Agrégation par ville
    aggregated_data = df.groupby('ville')['nb_enfant'].sum().reset_index()

    # Créer un graphique avec la bibliothèque plotly
    fig = px.bar(aggregated_data, x='ville', y='nb_enfant', title="Total d'enfants par ville")

    fig.write_html('templates/graphique.html')

    return render_template('index.html', data=data)
"""
    result = db.session.query(Client.ville, Client.nb_enfant, db.func.sum(Produit.prix).label('total_achats')) \
        .join(Collecte, Client.id_client == Collecte.id_client) \
        .join(Produit, Collecte.id_collecte == Produit.id_collecte) \
        .group_by(Client.id_client, Collecte.id_collecte) \
        .limit(10)
"""

#à venir
#@app.route('/login')

if __name__ == '__main__':
    app.run(debug=True)