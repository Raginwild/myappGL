
#settings connexion DB PostGres (paramétrés avec pgAdmin4)
DB_PARAM = {
    'dbname': 'mgl_db',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

if __name__=="__main__":
    print(DB_PARAM.get('dbname'))