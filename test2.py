import streamlit as st
import pandas as pd
import mysql.connector


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

def mostra_tabela_io_opcua():
   
    sql4 = "SELECT * FROM io_opcua"
    mp2 = executar_consulta(sql4)
    mp2.set_index(mp2.columns[0], inplace=True)
    st.write(mp2)    

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

  

def pagina_inicial():
    st.title("Produção CP Lab")
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
    st.title("Planta")
    mostra_planta()
    

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




