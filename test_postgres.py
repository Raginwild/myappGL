#test injection de données dans la base de données 
import psycopg2
from tabulate import tabulate

#settings connexion DB PostGres (pris depuis pgAdmin 4)
db_params = {
    'dbname': 'mgl_db',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}
