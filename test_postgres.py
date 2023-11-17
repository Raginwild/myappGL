#test injection de données dans la base de données 
import psycopg2
from tabulate import tabulate
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import pandas as pd

#settings connexion DB PostGres (paramétrés avec pgAdmin4)
db_params = {
    'dbname': 'mgl_db',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

