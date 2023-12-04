import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd

def run_metodos_page():
    st.title("Métodos Exatos: ")
    st.subheader('Introdução')
    st.markdown(""" Este texto será adicionado posteriormente...
""")
    st.subheader("Exemplos utilizados no método das somas ponderadas")
    st.latex(r"max f_1 = x_1 + x_2 \\"
             "max f_2 = x_2")
    st.latex(r"""
    \text{s.a $X$:}\begin{cases}
    x_1 + 2x_2 \leq 6 \\
    x_1  \leq 2 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)   
   
   
   
    st.latex(r"""
    \text{$X$:}\begin{cases}
    x_1 + 2x_2 \leq 6 \\
    x_1  \leq 2 \\
    x_1,x_2 \geq 0
    \end{cases} \Rightarrow
    \text{$Z$:}\begin{cases}
    f_1 + f_2 \leq 6 \\
    f_1 - f_2 \leq 2 \\
    f_1 - f_2 \geq 0 \\
    f_2  \geq 0
    \end{cases}     
    """)
    x1 = [0,3, 4, 2,0]
    x2 = [0,3, 2, 0,0]
    reta_x1 = [3,4]
    reta_x2 = [3,2]
    # Criando o gráfico interativo
    fig = go.Figure()
    """fig.add_annotation(
            x=1,  # Posição x do início da seta
            y=2,  # Posição y do início da seta
            ax=0,  # Comprimento na direção x
            ay=0,  # Comprimento na direção y
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=3,
            arrowcolor='red'
        )"""
    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='Gainsboro', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[4], y=[2], mode='markers', marker=dict(color='DeepSkyBlue', size=10), name='Ponto que Maximiza f<sub>1</sub>'))
    fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='SaddleBrown', width=3), name='Pontos Não-dominados de Z'))
    fig.add_trace(go.Scatter(x=[3], y=[3], mode='markers', marker=dict(color='red', size=10), name='Ponto que Maximiza f<sub>2</sub>'))

    #título
    fig.update_layout(
        title='Espaço Critério',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)
    x1 = [0,0, 2, 2,0]
    x2 = [0,3, 2, 0,0]
    reta_x1 = [3,4]
    reta_x2 = [3,2]
    # Criando o gráfico interativo
    fig = go.Figure()
    """fig.add_annotation(
            x=1,  # Posição x do início da seta
            y=1,  # Posição y do início da seta
            ax=0,  # Comprimento na direção x
            ay=0,  # Comprimento na direção y
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=3,
            arrowcolor='red'
        )"""
    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='Gainsboro', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[2], y=[2], mode='markers', marker=dict(color='DeepSkyBlue', size=10), name='Ponto que Maximiza f<sub>1</sub>'))
   # fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='SaddleBrown', width=3), name='Pontos Não-dominados de Z'))
    fig.add_trace(go.Scatter(x=[0], y=[3], mode='markers', marker=dict(color='red', size=10), name='Ponto que Maximiza f<sub>2</sub>'))

    #título
    fig.update_layout(
        title='Espaço Decisão',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='x<sub>2</sub>')
    )
    st.plotly_chart(fig)
    st.markdown(""" Queremos Resolver o seguinte problema:
""")
    st.latex(r"max \lambda_1 (x_1 + x_2)+ \lambda_2 (x_2)")
    st.latex(r"""
    \text{s.a $X$:}\begin{cases}
    x_1 + 2x_2 \leq 6 \\
    x_1  \leq 2 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)   
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('images/soma_ponderada_exemplo1.PNG',  width=300)

    with col3:
        st.write(' ')


    st.subheader('Problema 2: ')
    st.latex(r"max f_1 = x_1 \\"
             "max f_2 = x_2")
    st.latex(r"""
    \text{s.a $X$:}\begin{cases}
    x_1 + 4x_2 \leq 20 \\
    4x_1 + x_2  \leq 20 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)   
   
   
   
    st.latex(r"""
    \text{$X$:}\begin{cases}
    x_1 + 4x_2 \leq 20 \\
    4x_1 + x_2  \leq 20 \\
    x_1,x_2 \geq 0
    \end{cases} \Rightarrow
    \text{$Z$:}\begin{cases}
    f_1 + 4f_2 \leq 20 \\
    4f_1 + f_2 \leq 20 \\
    f_1,f_2 \geq 0
    \end{cases}     
    """)
    x1 = [0,0, 4, 5,0]
    x2 = [0,5, 4, 0,0]
    reta_x1 = [0,4,5]
    reta_x2 = [5,4,0]
    # Criando o gráfico interativo
    fig = go.Figure()
    """fig.add_annotation(
            x=1,  # Posição x do início da seta
            y=2,  # Posição y do início da seta
            ax=0,  # Comprimento na direção x
            ay=0,  # Comprimento na direção y
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=3,
            arrowcolor='red'
        )"""
    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='Gainsboro', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[5], y=[0], mode='markers', marker=dict(color='DeepSkyBlue', size=10), name='Ponto que Maximiza f<sub>1</sub>'))
    fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='SaddleBrown', width=3), name='Pontos Não-dominados de Z'))
    fig.add_trace(go.Scatter(x=[0], y=[5], mode='markers', marker=dict(color='red', size=10), name='Ponto que Maximiza f<sub>2</sub>'))
    fig.add_trace(go.Scatter(x=[4], y=[4], mode='markers', marker=dict(color='green', size=10), name='Solução intermediária'))

    #título
    fig.update_layout(
        title='Espaço Decisão',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='<sub>2</sub>')
    )
    st.plotly_chart(fig)
    x1 = [0,0, 4, 5,0]
    x2 = [0,5, 4, 0,0]
    reta_x1 = [0,4,5]
    reta_x2 = [5,4,0]
    # Criando o gráfico interativo
    fig = go.Figure()
    """fig.add_annotation(
            x=1,  # Posição x do início da seta
            y=2,  # Posição y do início da seta
            ax=0,  # Comprimento na direção x
            ay=0,  # Comprimento na direção y
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=3,
            arrowcolor='red'
        )"""
    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='Gainsboro', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[5], y=[0], mode='markers', marker=dict(color='DeepSkyBlue', size=10), name='Ponto que Maximiza f<sub>1</sub>'))
    fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='SaddleBrown', width=3), name='Pontos Não-dominados de Z'))
    fig.add_trace(go.Scatter(x=[0], y=[5], mode='markers', marker=dict(color='red', size=10), name='Ponto que Maximiza f<sub>2</sub>'))
    fig.add_trace(go.Scatter(x=[4], y=[4], mode='markers', marker=dict(color='green', size=10), name='Solução intermediária'))

    #título
    fig.update_layout(
        title='Espaço Critério',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)
    st.markdown(""" Queremos Resolver o seguinte problema:
""")
    st.latex(r"max \lambda_1 (x_1)+ \lambda_2 (x_2)")
    st.latex(r"""
    \text{s.a $X$:}\begin{cases}
    x_1 + 4x_2 \leq 20 \\
    4x_1 + x_2  \leq 20 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)   
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image('images/soma_ponderada_exemplo2.PNG',  width=300)

    with col3:
        st.write(' ')        
