import sqlite3

def create_in_db(dbname , sql): # Change DATA with SQL
    connection = sqlite3.connect(dbname)# create DB and connect
    cursor = connection.cursor() #  initialize
    cursor.execute(sql) # what to do
    connection.commit() # Done!!

DBname = 'deal.db'
sql =""" CREATE TABLE IF NOT EXISTS Deal(
    firstname TEXT,
    lastname TEXT,
    telnum INT,
    email TEXT,
    age INT
    ismember BOOL); """
create_in_db(DBname, sql)

choice = input("please enter the number of action you would like to commit: 1. Add New Customer"
               "2. Delete Customer 3. Show All Customer" )
if choice == "1":
    firstname, lastname, email, ismember = input("please enter first name, last name,"
                                                              " email,  and is he a member?")
    telnum, age = int(input("enter telephone number and age please"))

    sql = """INSERT INTO DBname
          VALUES(firstname, lastname, telnum, email, age, ismember);"""
    create_in_db(DBname, sql)

if choice == "2":
    firstname, email = input("please enter a name and email you would like to delete")
    sql= """ DELETE FROM DBname
    WHERE firstname= firstname and email= email"""
    create_in_db(DBname, sql)

if choice == "3":
    sql = "SELECT * FROM DBname"
    create_in_db(DBname, sql)