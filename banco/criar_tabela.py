import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187",
  database="cplab_1"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE entradas (entrada VARCHAR(255) NOT NULL PRIMARY KEY , estado VARCHAR(255) NOT NULL )")


#mycursor.execute("CREATE TABLE ordens_por_id (id_produto INT NOT NULL PRIMARY KEY, qtd_ordens INT)")
print(mycursor.rowcount, "record(s) inserted")