import sqlite3


def create_in_db(dbname , sql): # Change DATA with SQL
    connection = sqlite3.connect(dbname)# create DB and connect
    cursor = connection.cursor() #  initialize
    cursor.execute(sql) # what to do
    connection.commit() # Done!!

def create_db():
    DBname = 'DB.db'
    sql = """ CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        phone TEXT,
        email TEXT );
    """
    create_in_db(DBname, sql)

create_db()



