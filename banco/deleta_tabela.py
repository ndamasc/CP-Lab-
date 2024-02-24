import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187"
)


mycursor = mydb.cursor()

## para deletar uma tabela

sql = "DROP DATABASE cplab"

mycursor.execute(sql)

#sql = "ALTER TABLE producao2 DROP COLUMN qtd_ordens;"
#mycursor.execute(sql)


