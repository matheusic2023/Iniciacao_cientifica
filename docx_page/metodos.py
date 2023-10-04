import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd

def run_metodos_page():
    st.title("Apresentação: ")
    st.subheader('O que é a programação matemática?')
    st.write('Uma das principais áreas de pesquisa na matemática aplicada é a programação matemática. O objeto de estudo dessa área é a otimização de uma função, denominada função objetivo, que pode ser maximizada ou minimizada, de modo que tal função é sujeita a restrições que são representadas por desigualdades.')
    st.subheader('Quais são as principais áreas de estudo da programação matemática na graduação?')