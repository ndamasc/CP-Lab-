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
    st.title('Tabela do MySQL')
    sql = "SELECT * FROM produtos"
    df = executar_consulta(sql)
    df.set_index(df.columns[0], inplace=True)
    st.write(df)
    

def gera_grafico():
    sql = "SELECT id,  quantidade FROM produtos"
    df = executar_consulta(sql)
    st.bar_chart(df.set_index('id'))
     
def criar_nova_tabela():
    sql5 = "SELECT * FROM produtos"
    opcao1 = executar_consulta(sql5)
    opcao1['total'] = opcao1['quantidade'] * opcao1['qtd_ordens']
    colunas_selecionadas = ['id', 'tipo_produto', 'total']  # Substitua com os nomes das colunas desejadas
    opcao1 = opcao1[colunas_selecionadas]
    opcao1.set_index(opcao1.columns[0], inplace=True)
    st.write(opcao1)
    

def pagina_inicial():
    st.title("Produção CP Lab")
    
    st.write("Bem-vindo à página inicial!")
    mostrar_tabela()
    gera_grafico()

def segunda_pagina():
    st.title("Histórico")
    st.image("https://www.festo.com/media/pim/341/D15000100172341_1056x1024.jpg", caption="CP Lab 400",width=450)
    st.write("Esta é a segunda página.")
    criar_nova_tabela()

def main():
    menu = ["Produção CP Lab", "Histórico"]
    escolha = st.sidebar.selectbox("Navegar", menu)

    if escolha == "Produção CP Lab":
        pagina_inicial()
    elif escolha == "Histórico":
        segunda_pagina()

if __name__ == "__main__":
    main()




