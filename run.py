# app.py
# fichier back-end de l'application 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model_insert import insert_csv
from datetime import datetime
from app.statics.db_set import DB_PARAM
import pandas as pd
import psycopg2
import plotly.express as px
from flask_bootstrap import Bootstrap
from app.models import db, User, Client, Collecte,Produit  #importation du db depuis le fichier models.py
from config import DevelopmentConfig, ProductionConfig #fichier de configuration de l'application


conn = psycopg2.connect(
    host=DB_PARAM.get('host'),
    database=DB_PARAM.get('dbname'),
    user=DB_PARAM.get('user'),
    password=DB_PARAM.get('password')
)

app = Flask(__name__)
app.config.from_object(ProductionConfig)
bootstrap = Bootstrap(app)

db.init_app(app)

with app.app_context():
    # Importez les modèles pour créer les tables
    db.create_all()

#routes pour l'accès aux différentes pages 
@app.route('/')
def index():
    csv_path='client_table.csv'
    csv_path='collectes_table.csv'

    if csv_path:
        # Lire le fichier CSV avec pandas
            df = pd.read_csv(csv_path, sep=";")

            # Ajouter les données à la base de données
            cursor = conn.cursor()

            
            for index, row in df.iterrows():
                id_row = Client.query.filter_by(id_client=row['id_client']).first()
                if not id_row:
                # Assurez-vous d'adapter ces colonnes en fonction de votre schéma de base de données
                    cursor.execute("INSERT INTO client (id_client, date_passage, nb_enfant, ville, cat_sociopro)\
                                    VALUES (%s, %s, %s, %s, %s);", (row['id_client'], row['date_passage'],row['nb_enfant'], row['ville'],\
                                                                    row['cat_sociopro']))

            conn.commit()
            cursor.close()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client;")
    data = cursor.fetchall()
    cursor.close()

    columns = ['id_client', 'date_passage', 'nb_enfant', 'ville', 'cat_sociopro']
    df = pd.DataFrame(data, columns=columns)

    # Agrégation par ville
    aggregated_data = df.groupby('ville')['nb_enfant'].sum().reset_index()

    # Créer un graphique avec la bibliothèque plotly
    fig = px.bar(aggregated_data, x='ville', y='nb_enfant', title='Total enfant par ville')

    fig.write_html('templates/graphique.html')

    return render_template('index.html', data=data)

#à venir
#@app.route('/login')

if __name__ == '__main__':
    app.run(debug=True)