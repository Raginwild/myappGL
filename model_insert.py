#chargement de données fictives dans la database
def insert_csv(file,engine):
    df_insert=pd.read_csv('user_test.csv', sep=';')
    print(df_insert)
    df_insert.to_sql('utilisateurs', engine, index=False, if_exists='append')
    print('les lignes ont bien été enregistrées')


# Visualisation des tables avec Pandas
def get_table(engine,table):
    query = f"SELECT * FROM {t};"
    df = pd.read_sql_query(query, engine)
    print(f"\nContenu de la table {t}:\n{df}")
