import sqlite3


def create_in_db(dbname , sql): # Change DATA with SQL
    connection = sqlite3.connect(dbname)# create DB and connect
    cursor = connection.cursor() #  initialize
    cursor.execute(sql) # what to do
    connection.commit() # Done!!

def main():
    DBname= 'MyfirstDB.db'
    sql = """ CREATE TABLE IF NOT EXISTS users(
        id INT,
        username TEXT,
        password TEXT );
    """
    create_in_db(DBname, sql)
    sql = "INSERT INTO users VALUES (1, 'shalomv', '1q2w3e')"
    create_in_db(DBname, sql)
    sql = "UPDATE users SET username='moshe'  WHERE id=1"
    create_in_db(DBname, sql)




if __name__ == "__main__" :
    main()







