import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

dados = [
    {'Data': '2022-01-01', 'Producao': [10, 12, 12, 17, 20, 25, 28, 32, 35, 36, 39, 41]},
    {'Data': '2022-01-02', 'Producao': [12, 23, 32, 42, 49, 55, 60, 66, 71, 79, 80, 82]},
    {'Data': '2022-01-03', 'Producao': [17, 28, 35, 43, 52, 59, 63, 71, 75, 78, 25, 41]},
]

# Criar DataFrame
df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])

status_var = False
erro = True


def colored_dot(status, size=55):
    colors = {
        "green": "green",
        "red": "red",
        "yellow": "yellow"
    }
    color = colors.get(status, "grey")  # Se o status não for "green", "red" ou "yellow", assume "gray"
    
    dot_style = (
        f'background-color: {color}; '
        f'border-radius: 50%; '
        f'width: {size}px; '
        f'height: {size}px; '
        f'border: 2px solid white; '  # Adiciona uma borda branca
        f'box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);'  # Adiciona uma sombra
    )

    dot = f'<div style="{dot_style}"></div>'
    return dot

def main():
   
    st.title('Produção CP Lab 406-1') # Título

    #st.markdown("## Planta CP Lab 406-1")
    
    st.markdown('<h3 style="margin-bottom:20px;">Estado da planta </h3>', unsafe_allow_html=True)

    if erro == True:
        st.write(
                f'<div style="display: flex; align-items: center;">'
                f'{colored_dot("red")} '
                f'<span style="margin-left: 80px;font-size: 20px;">{"ERRO!!!"}</span>'
                f'</div>',
                unsafe_allow_html=True
            )

    else:
        if status_var == True:
            st.write(
                f'<div style="display: flex; align-items: center;">'
                f'{colored_dot("green")} '
                f'<span style="margin-left: 80px;font-size: 20px;">{"Produção em andamento"}</span>'
                f'</div>',
                unsafe_allow_html=True
            )

        else:
            st.write(
                f'<div style="display: flex; align-items: center;">'
                f'{colored_dot("yellow")} '
                f'<span style="margin-left: 80px; font-size: 20px;">{"Não há produção"}</span>'
                f'</div>',
                unsafe_allow_html=True
            )
    #st.image('https://ip.festo-didactic.com/InfoPortal/CPFactoryLab/data/CP-L-406-1/img/image.md.jpg', width=400)
    
    st.markdown('<style>div.stImage img { margin-top: 100px; }</style>', unsafe_allow_html=True)
    st.image('https://ip.festo-didactic.com/InfoPortal/CPFactoryLab/data/CP-L-406-1/img/image.md.jpg', width=400)


        # Tabela de Dados
    st.markdown('<h3 style="margin-bottom:20px;">Ordens realizadas por dia</h3>', unsafe_allow_html=True)
    st.dataframe(df)

    
    #st.subheader('Produção ao longo do tempo')
    st.markdown('<h3 style="margin-bottom:20px;">Produção ao longo do tempo</h3>', unsafe_allow_html=True)


    all_data = [item for sublist in df['Producao'].tolist() for item in sublist]

    # Criar o gráfico de linha
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(1, len(all_data) + 1), all_data, marker='o', linestyle='-', color='b')

    ax.set_xlabel('Amostras')
    ax.set_ylabel('Ordens')
    ax.set_title('Quantidade de Ordens produzidas')
    st.pyplot(fig)


    media_producao = round(df['Producao'].apply(lambda x: pd.Series(x).mean()).mean(), 2)
    max_producao = df['Producao'].apply(lambda x: pd.Series(x).max()).max()
    min_producao = df['Producao'].apply(lambda x: pd.Series(x).min()).min()


    # Estatísticas Simples
    st.markdown('<h3 style="margin-bottom:20px;">Métricas </h3>', unsafe_allow_html=True)
    st.text(f"Média de Produção: {media_producao}")
    st.text(f"Máximo de Produção: {max_producao}")
    st.text(f"Mínimo de Produção: {min_producao}")

if __name__ == "__main__":
    main()