# config.py
from app.statics.db_set import DB_PARAM

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_PARAM.get('user')}:{DB_PARAM.get('password')}@{DB_PARAM.get('host')}/{DB_PARAM.get('dbname')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  # Mettez à False en production


import os

class Config:
    SECRET_KEY = 'votre_cle_secrete'  # Changez cela par une valeur aléatoire et sécurisée
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_PARAM.get('user')}:{DB_PARAM.get('password')}@{DB_PARAM.get('host')}/{DB_PARAM.get('dbname')}"
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #il y aura l'adresse de la base de donnée de déploiement