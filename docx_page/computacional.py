import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
import numpy as np

def run_computacional_page():
    def main():
        st.title('Teste para montar expressão linear')

        num_variaveis = st.number_input('Número de variáveis:', min_value=1, max_value=10, value=1, step=1)

        coeficientes = []
        for i in range(num_variaveis):
            coeficiente = st.number_input(f'Coeficiente para x{i+1}:', value=1.0)
            coeficientes.append(coeficiente)

        expressao = criar_expressao_linear(coeficientes)
        st.write(f'A expressão linear é: {expressao}')

    def criar_expressao_linear(coeficientes):
        expressao = ''
        for i, coeficiente in enumerate(coeficientes):
            expressao += f'{coeficiente}*x{i+1} + ' if i < len(coeficientes) - 1 else f'{coeficiente}*x{i+1}'
        return expressao
    main()
