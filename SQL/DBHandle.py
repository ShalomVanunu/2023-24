import sqlite3

dbname= "CRM"
def DB_Change(dbname, sql):
    connection = sqlite3.connect(dbname)  # create DB and connect
    cursor = connection.cursor()  # initialize
    cursor.execute(sql)  # what to do
    connection.commit()  # Done!!

def get_data(dbname, sql):
    connection = sqlite3.connect(dbname)  # create DB and connect
    cursor = connection.cursor()  # initialize
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)



def add_user():
    first_name = input("FirstName :")
    last_name = input("LastName :")
    tel_num = input("telNum :")
    email = input("Email :")
    age = int(input("Age :"))
    is_member = bool(input("Member True/false"))
    sql_add = f"INSERT INTO costumers VALUES ('{first_name}','{last_name}','{tel_num}','{email}',{age},{is_member})"
    DB_Change(dbname,sql_add)

def del_user():
    first_name = input("FirstName :")
    email = input("Email :")
    sql_del =f"DELETE FROM costumers WHERE first_name == '{first_name}' AND email == '{email}'"
    DB_Change(dbname,sql_del)


def show_users():
    sql_show = " SELECT * FROM costumers "
    get_data(dbname, sql_show)


sql_create_db = """CREATE TABLE IF NOT EXISTS costumers(
    first_name TEXT ,
	last_name TEXT ,
	tel_num TEXT,
	email TEXT ,
	age INTEGER,
	is_member BOOLEAN);"""

DB_Change(dbname,sql_create_db)




