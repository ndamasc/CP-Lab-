import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE cplab_1")