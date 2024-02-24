import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="colares9187",
  database="cplab_1"
)


mycursor = mydb.cursor()

#sql = "INSERT INTO ordens_por_id (id, qtd) VALUES (%s, %s)"
#val = (1, 'Full cover', 3)
#mycursor.execute(sql, val)

sql = "INSERT INTO entradas (entrada, estado ) VALUES (%s, %s)"
val = [
  ('BG5', 'ON'),
  ('BG6', 'OFF'),
  ('BG7', 'OFF' ),
  ('BG8', 'ON' ),
]

mycursor.executemany(sql, val)  #para inserir varios dados

mydb.commit()
print(mycursor.rowcount, "record inserted.")

## tabela ordens_por_id:   id_produto | qdt_ordens

## tabela producao:    id_produto  |  tipo_produto | producao

