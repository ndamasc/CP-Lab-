import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187",
  database="cplab"
)

mycursor = mydb.cursor()

sql = "UPDATE producao2 SET producao = 20 WHERE id_produto = 2"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")


#colunas   (id_produto  |  tipo_produto | producao)