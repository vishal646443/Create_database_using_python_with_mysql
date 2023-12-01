import mysql.connector
datab=mysql.connector.connect(
    host="localhost",
    user="root",#change according to your settings
    password="UnionSoftware7127"#change according to your settings
)
mycursor=datab.cursor()
mycursor.execute("CREATE DATABASE NewDatabase")
