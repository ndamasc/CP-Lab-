import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187",
  database="cplab"
)


mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE producao ADD COLUMN qtd_ordens INT")
