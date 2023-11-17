#chargement de données fictives dans la database

def get_csv(file):
    df_insert=pd.read_csv('user_test.csv', sep=';')

def insert_csv(file,engine):
    df_insert=get_csv(file)
    df_insert.to_sql('utilisateurs', engine, index=False, if_exists='append')
    print('les lignes ont bien été enregistrées')


# Visualisation des tables avec Pandas
def get_table(engine,table):
    query = f"SELECT * FROM {t};"
    df = pd.read_sql_query(query, engine)
    print(f"\nContenu de la table {t}:\n{df}")
