import mysql.connector

#mysql db connection
dbconnect = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'P@ssw0rd'
)
# cursor object creation
dbcursor=dbconnect.cursor()

#DB creation

dbcursor.execute("CREATE DATABASE CRMDB")

print("CRMDB created!!!")