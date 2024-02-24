import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187",
  database="cplab_1"
)

mycursor = mydb.cursor()

## para ver todos os dados da tabela
mycursor.execute("SELECT *  FROM entradas")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


## duas tabelas :   ordens_por_id  e producao