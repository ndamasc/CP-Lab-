import streamlit as st
import pandas as pd
import mysql.connector

planta_ligada = False

html_template1 = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        .container {{
            display: flex;
            align-items: center;
        }}
        .bolinha {{
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: {'green' if planta_ligada else 'red'};
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5); /* Sombra */
            border: 2px solid #ccc; /* Borda cinza */
            margin-right: 10px;
        }}
        .comentario {{
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div id="bolinha" class="bolinha"></div>
        <div class="comentario" id="comentario">{'Planta ligada' if planta_ligada else 'Planta desligada'}</div>
    </div>

</body>
</html>
'''

print(html_template1)


####################### CRUD

def inserir_dados_msg(msg, code_msg):
    mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="colares9187",
        database="teste"
    )
    mycursor = mydb2.cursor()
    sql3 = "INSERT INTO mensagem (msg, code_msg) VALUES (%s, %s)"
    val1 = (msg, code_msg)
    mycursor.execute(sql3, val1)
    mydb2.commit()  # Você esqueceu de commitar a transação
    mydb2.close()

def inserir_dados_planta(Planta_id, plant_name,endpoint, io_opcua_id, plata_status ):
    mydb3 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="colares9187",
        database="teste"
    )
    mycursor = mydb3.cursor()
    sql4 = "INSERT INTO planta (Planta_id, plant_name,endpoint, io_opcua_id, plata_status) VALUES (%s, %s,%s, %s, %s)"
    val2 = (Planta_id, plant_name,endpoint, io_opcua_id, plata_status)
    mycursor.execute(sql4, val2)
    mydb3.commit()  # Você esqueceu de commitar a transação
    mydb3.close()

def deletar_dados_msg(code_msg):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="colares9187",
        database="teste"
    )
    mycursor = mydb.cursor()
    sql = "DELETE FROM mensagem WHERE code_msg = %s"
    val = (code_msg,)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close() 

def atualizar_dados_msg(code_msg, nova_msg):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="colares9187",
        database="teste"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE mensagem SET msg = %s WHERE code_msg = %s"
    val = (nova_msg, code_msg)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

########################### 

def executar_consulta(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="colares9187",
        database="teste"
    )
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    data = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    df = pd.DataFrame(data, columns=columns)
    mydb.close()
    return df


def mostrar_tabela():
   
    sql = "SELECT * FROM producao"
    df = executar_consulta(sql)
    df.set_index(df.columns[0], inplace=True)
    st.write(df)
    
def mostrar_mensagens():
    
    sql3 = "SELECT * FROM mensagem"
    mp = executar_consulta(sql3)
    mp.set_index(mp.columns[0], inplace=True)
    st.write(mp)
    
def atualiza_tabela():
    
    st.subheader("Atualizar Dados")
    code_msg_update = st.text_input("Código da Mensagem para Atualizar:")
    nova_msg = st.text_input("Nova Mensagem:")
    if st.button("Atualizar"):
        atualizar_dados_msg(code_msg_update, nova_msg)
        st.success("Dados atualizados com sucesso!")
        
    
    
    
#def mostra_tabela_io_opcua():
#   
#    sql4 = "SELECT * FROM io_opcua"
#    mp2 = executar_consulta(sql4)
#    def bolinha(status_item):
#        cor = 'green' if status_item == 'Ativo' else 'red'
#        return f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {cor};"></div>'
#    mp2['ON/OFF'] = mp2['status_item'].apply(bolinha)
#    mp2.set_index(mp2.columns[0], inplace=True)
#    
#    st.write(mp2)    

def mostra_tabela_io_opcua():
    sql4 = "SELECT * FROM io_opcua"
    mp2 = executar_consulta(sql4)
    def bolinha(status_item):
        cor = 'green' if status_item == 'Ativo' else 'red'
        return f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {cor};"></div>'

    # Adicionando uma coluna de bolinhas ao DataFrame
    mp2['Bolinha'] = mp2['status_item'].apply(bolinha)

    # Exibindo a tabela com as bolinhas usando st.write
    st.write(mp2.to_html(escape=False), unsafe_allow_html=True)



#def gera_grafico():
#    sql = "SELECT id,  quantidade FROM produtos"
#    df = executar_consulta(sql)
#    st.bar_chart(df.set_index('id'))
#     

def criar_nova_tabela():
    sql5 = "SELECT * FROM producao"
    opcao1 = executar_consulta(sql5)
    opcao1['total'] = opcao1['qtd_produto'] * opcao1['qtd_ordem']
    colunas_selecionadas = ['produção_id', 'tipo_produto', 'total']  # Substitua com os nomes das colunas desejadas
    opcao1 = opcao1[colunas_selecionadas]
    opcao1.set_index(opcao1.columns[0], inplace=True)
    st.write(opcao1)
    st.bar_chart(opcao1.set_index('tipo_produto'))

def mostra_planta():
    sql6 = "SELECT * FROM planta"
    mp3 = executar_consulta(sql6)
    mp3.set_index(mp3.columns[0], inplace=True)
    st.write(mp3)

 
def cadastrar_msg():
    
        st.subheader("Adicionar Dados de mensagem")

        # Campos para inserir nome e idade
        msg = st.text_input("Mensagem")
        code_msg = st.number_input("Código da mensagem", min_value=0, max_value=150, step=1)

        # Botão para inserir os dados
        if st.button("Inserir Dados", key="inserir_msg"):
            if msg and code_msg:
                inserir_dados_msg(msg, code_msg)
                st.success("Dados inseridos com sucesso!")
            else:
                st.error("Por favor, preencha todos os campos.")

def deletar_dados():
    st.subheader("Deletar Dados")
    code_msg_delete = st.text_input("Código da Mensagem para Deletar:")
    if st.button("Deletar"):
        deletar_dados_msg(code_msg_delete)
        st.success("Dados deletados com sucesso!")
    

def cadastrar_planta():
    
        st.title("Adicionar Planta")

        # Campos para inserir nome e idade
        Planta_id = st.text_input("ID planta")
        plant_name = st.text_input("Nome da planta")
        endpoint = st.text_input("Endpoint")
        io_opcua_id  = st.number_input("IO OPCUA ID", min_value=0, max_value=150, step=1)
        plata_status = st.text_input("Status (Ativo/ Inativo)")

        # Botão para inserir os dados
        if st.button("Inserir Dados", key="inserir_planta"):
            if Planta_id and plant_name and endpoint and io_opcua_id and plata_status:
                inserir_dados_planta(Planta_id, plant_name,endpoint, io_opcua_id, plata_status)
                st.success("Dados inseridos com sucesso!")
            else:
                st.error("Por favor, preencha todos os campos.")                  

def pagina_inicial():

    st.image('https://www.festo.com/media/fox/frontend/img/svg/logo_blue.svg', width=400, use_column_width=False)

    #use_column_width=False
    
    st.title("Produção CP Lab")
    ##  para mais um topico separado na aba     st.sidebar.title('Cabeçalho Personalizado')
    st.write(html_template1, unsafe_allow_html=True)
    st.image("https://www.festo.com/media/pim/341/D15000100172341_1056x1024.jpg", caption="CP Lab 400",width=450)
    
    mostrar_tabela()
    #gera_grafico()
    

    
    

def segunda_pagina():
    st.write("Esta é a segunda página.")
    st.title("Produção total")
    criar_nova_tabela()
    st.title("Tabela de IOs")
    mostra_tabela_io_opcua()
    
    
    
def terceira_pagina():
    
    st.title("Mensagens da produção")
    mostrar_mensagens()
    with st.expander("Adicionar dados"):
        #st.write("Aqui estão os detalhes adicionais que podem ser expandidos.")
        cadastrar_msg()
    with st.expander("Deletar dados"):
        deletar_dados()
    with st.expander("Atualizar dados"):
        atualiza_tabela()

    st.title("Planta")
    mostra_planta()
    with st.expander("Cadastrar planta"):
        #st.write("Aqui estão os detalhes adicionais que podem ser expandidos.")
        cadastrar_planta()
    
    
    

def main():
    menu = ["Produção CP Lab", "Histórico","Informações da Planta"]
    escolha = st.sidebar.selectbox("Navegar", menu)

    if escolha == "Produção CP Lab":
        pagina_inicial()
    elif escolha == "Histórico":
        segunda_pagina()
    elif escolha == "Informações da Planta":
        terceira_pagina()
    

if __name__ == "__main__":
    main()




