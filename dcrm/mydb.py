import psycopg2

# Connessione a PostgreSQL
dataBase = psycopg2.connect(
    host='localhost',
    user='matteo',
    password='Matteo2004x',
    database='elderco'
)

# Preparazione di un oggetto cursore
cursorObject = dataBase.cursor()

# Non è necessario creare il database in PostgreSQL, poiché dovrebbe già esistere.

# Chiusura della connessione e del cursore
cursorObject.close()
dataBase.close()