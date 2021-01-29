import streamlit as st
import pandas as pd
import base64
import altair as alt
import numpy as np

from PIL import Image

st.title('As 10 melhores campanhas do Campeonato Brasileiro de Futebol')

img = Image.open('images/soccer-logo.jpg')
st.image(img, use_column_width=True)

st.header('Era dos pontos corridos')
st.subheader('Na era dos postos corridos, o time brasileiro com melhor aproveitamento é o Clube de Regatas do Flamengo.')

# Web scraping of Wikipedia data
#
@st.cache #(https://docs.streamlit.io/en/latest/caching.html)
def load_data():
    url = 'https://pt.wikipedia.org/wiki/Resultados_e_estat%C3%ADsticas_do_Campeonato_Brasileiro_de_Futebol#Em_sistemas_mistos'
    html = pd.read_html(url, header = 0)
    df = html[27]
    return df

df = load_data()
df.columns = ['Classificação', 'Clube', 'Ano', 'Jogos', 'Vitorias', 'Empates', 'Derrotas', 'Aproveitamento' ]
df
