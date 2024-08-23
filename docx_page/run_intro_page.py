import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
def run_intro_page():
    def region_plot(x1,x2,vetor_pontos,titulo):
        

        # Coordenadas do segmento de reta
        #reta_x1 = [0, 10]
        #reta_x2 = [44, 40]

        # Criando o gráfico interativo
        fig = go.Figure()
        #name='x<sub>1</sub> + x<sub>2</sub> ≤ 2'
        # Adicionando a região
        fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

        # Adicionando os pontos das soluções
        fig.add_trace(go.Scatter(x=[vetor_pontos[0]], y=[vetor_pontos[1]], mode='markers', marker=dict(color='red', size=10), name=f'Solução Ótima ({vetor_pontos[0]},{vetor_pontos[1]}) para f<sub>1</sub>'))
        fig.add_trace(go.Scatter(x=[vetor_pontos[2]], y=[vetor_pontos[3]], mode='markers', marker=dict(color='blue', size=10),name=f'Solução Ótima ({vetor_pontos[2]},{vetor_pontos[3]}) para f<sub>2</sub>'))

        # Adicionando o segmento de reta
        #fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='blue', width=3), name='Segmento (0,2) até (2,0)'))

        #título
        fig.update_layout(
            title=titulo,
            xaxis=dict(title='x<sub>1</sub>'),
            yaxis=dict(title='x<sub>2</sub>')
        )

        #gráfico no Streamlit
        return st.plotly_chart(fig)
    st.title("Introdução: ")
    st.subheader('O que é a programação matemática?')
    st.write('Uma das principais áreas de pesquisa na matemática aplicada é a programação matemática. O objeto de estudo dessa área é a otimização de uma função, denominada função objetivo, que pode ser maximizada ou minimizada, de modo que tal função é sujeita a restrições que são representadas por desigualdades.')
    st.subheader('Quais são as principais áreas de estudo da programação matemática na graduação?')
    st.markdown("<strong>Programação Linear:</strong> Estudo para a otimização de funções lineares sujeito a restrições lineares. "
                "Neste ramo as principais aplicações são relacionadas a problemas de transporte, designação, indústria e afins."
                " Além disso, os problemas lineares podem ser resolvidos de forma eficiente por meio de métodos exatos como o [Simplex](https://pt.wikipedia.org/wiki/Algoritmo_simplex).", unsafe_allow_html=True)
    st.markdown("<strong>Programação Não-Linear:</strong> Estudo para a otimização de funções sujeito a restrições lineares e não lineares. Diferente da Programação Linear, os problemas não lineares são mais complexos para serem resolvidos, de modo que há diversos métodos numéricos para a solução de problemas específicos: método de Newton, Gradiente descendente, entre outros. Todavia, esta área possui diversas aplicações em problemas de física, engenharia, machine learning e afins.", unsafe_allow_html=True)
    st.markdown(
    "<strong>Programação Inteira:</strong> Neste ramo, o interesse de estudo é relacionado a métodos para obter "
    "soluções inteiras para um problema de otimização. Um dos mais famosos métodos de PI é o "
    "[*Branch and Bound*](https://pt.wikipedia.org/wiki/Ramificar_e_limitar) para problemas lineares.",
    unsafe_allow_html=True)
    st.title('Introdução à otimização multiobjetivo:')
    st.subheader('O que é a otimização multiobjetivo?')
    st.markdown('O que difere esta área daquelas citadas acima é justamente a necessidade de otimizar diversas funções objetivos,'
                 'lineares ou não lineares (o foco deste trabalho é sobre as funções lineares), sujeito a restrições. '
                 'Além disso, neste tipo de problemas não temos apenas uma solução única, mas sim um conjunto de soluções denominada '
                 'soluções de pareto.')
    st.subheader('Modelagem de um problema de otimização multiobjetivo (POM):')
    st.write('Uma empresa de brinquedos trabalha com dois tipos de produtos: avião e carrinho.'
              'A fabricação de cada um destes brinquedos é formada por meio de três etapas - corte das peças, '
              'montagem e pintura. Para cada unidade do avião, é necessário 1 hora de corte, 2 horas de montagem '
              'e 2 horas de pintura. Para cada unidade do carrinho, é preciso de 1 hora de corte, 1 hora de montagem e '
              '5 horas de pintura. Além disso, tal empresa tem disponível a cada duas semanas 50 horas de corte, 80 horas'
              ' de montagem e 220 horas de pintura. Por fim, cada unidade do avião é vendida por R\$25,00, o carrinho por R$20,00 e há uma demanda de no minimo 25 unidades.')
    # 1) Variáveis de Decisão
    st.header("1) Variáveis de Decisão:")
    st.write("x₁ : Quantidade de aviões produzidos")
    st.write("x₂ : Quantidade de carrinhos produzidos")
    st.write("queremos maximizar o lucro, ou seja:")
    st.latex(r"max f_1(x) = 25x_1 + 20x_2")

    # 2) Restrições
    st.header("2) Restrições:")

    # Corte
    st.subheader("Corte:")
    st.latex(r"x_1 + x_2 \leq 50 \quad \text{(Tempo máximo de 50 horas a cada duas semanas)}")
    
    # Montagem
    st.subheader("Montagem:")
    st.latex(r"2x_1 + x_2 \leq 80 \quad \text{(Tempo máximo de 80 horas a cada duas semanas)}")

    # Pintura
    st.subheader("Pintura:")
    st.latex(r"2x_1 + 5x_2 \leq 220 \quad \text{(Tempo máximo de 220 horas a cada duas semanas)}")

    # Demanda
    st.subheader("Demanda:")
    st.latex(r"x_1 + x_2 \geq 25 \quad \text{(Produção de no minimo 25 unidades)}")

    st.markdown('')
    st.header("3) Problema de Otimização:")
    st.latex(r"max f_1 = 25x₁ + 20x₂")

    # Sujeito a
    st.latex(r"""
    \begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1 + x_2 \geq 25 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)

    # Criando as coordenadas para o gráfico
    x1 = [25,0, 0, 10, 30,40,25]
    x2 = [0, 25,44, 40, 20,0,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

    # Adicionando a solução ótima 
    fig.add_trace(go.Scatter(x=[30], y=[20], mode='markers', marker=dict(color='blue', size=10), name='Solução Ótima (30,20) para f<sub>1</sub>'))

    #título
    fig.update_layout(
        title='Região Factível do problema f<sub>1</sub>',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='x<sub>2</sub>')
    )

    #gráfico no Streamlit
    st.plotly_chart(fig)
    
    st.write("Suponha que agora o custo de empacotamento do avião é R\$1,00 e do carrinho R\$8,00. A empresa deseja "
             "minimizar o custo de empacotamento, ou seja, a seguinte função:")
    st.latex(r"min f_2 = x₁ + 8x₂")
    st.write('Se fossemos minimizar apenas esta função por algum método exato, como o método gráfico, vamos obter:')
    
    # Criando as coordenadas para o gráfico
    x1 = [25,0, 0, 10, 30,40,25]
    x2 = [0, 25,44, 40, 20,0,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

    # Adicionando a solução ótima 
    fig.add_trace(go.Scatter(x=[25], y=[0], mode='markers', marker=dict(color='red', size=10), name='Solução Ótima (25,0) para f<sub>2</sub>'))

    #título
    fig.update_layout(
        title='Região Factível do problema com f<sub>2</sub>',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='x<sub>2</sub>')
    )
    st.plotly_chart(fig)


    st.header('4) Discussão:')
    st.markdown('Sem entrar nos detalhes de como é resolvido um POM, percebemos que possíveis "soluções ótimas" para'
                ' este exemplo são justamente as soluções ótimas para cada um dos problemas resolvidos graficamente acima.'
                'Isso decorre do fato de que ambos os pontos, (30,20) e (25,0), respeitam todas as restrições do problema,'
                'tendo em vista que pertencem a região factível.')



    '''
    # Título
    st.title("Problema de Otimização")

    # 1) Variáveis de Decisão
    st.header("1) Variáveis de Decisão:")
    st.write("x₁ : Quantidade em toneladas de açúcar por semana no centro 1")
    st.write("x₂ : Quantidade em toneladas de açúcar por semana no centro 2")

    # 2) Restrições
    st.header("2) Restrições:")

    # Colheita
    st.subheader("Colheita:")
    st.write("É necessário 1 hora de colheita para cada tonelada de açúcar no centro 1, e 1 hora e meia para o centro 2.")
    st.latex(r"x_1 + 1.5x_2 \leq 42 \quad \text{(Tempo máximo de 42 horas por semana)}")

    # Maquinário
    st.subheader("Maquinário:")
    st.write("São necessárias 2 horas para produzir uma tonelada de açúcar no centro 1 e 3 horas para o centro 2.")
    st.latex(r"2x_1 + 3x_2 \leq 38 \quad \text{(Tempo máximo de 38 horas por semana)}")

    # Demanda
    st.subheader("Demanda:")
    st.latex(r"x_1 + x_2 \geq 12 \quad \text{(Produção semanal mínima de 12 toneladas)}")

    # Lucro
    st.write("Lucro: R$ 150,00 para cada tonelada do centro 1 e R$ 300,00 para o centro 2")

    # Emissão de CO2
    st.write("Emissão de CO2: A unidade é em % de emissão por tonelada produzida.")
    st.write("Centro 1 emite 18% e o centro 2, 35%.")

    # Problema de Otimização
    st.header("Problema de Otimização:")
    st.write("Maximizar f₁ = 150x₁ + 300x₂")
    st.write("Minimizar f₂ = 0.18x₁ + 0.35x₂")

    # Sujeito a
    st.latex(r"""
    \begin{cases}
    x_1 + 1.5x_2 \leq 42 \\
    2x_1 + 3x_2 \leq 38 \\
    x_1 + x_2 \geq 12 \\
    x_j \geq 0
    \end{cases}
    """)

    # Soluções Ótimas
    st.write("Utilizando o Solver iMOLPe, chegamos nas seguintes soluções ótimas:")
    st.latex(r"""
    \mathbf{x} = \begin{bmatrix}
    x_1  \\
    x_2  \\
    \end{bmatrix} = 
    \begin{bmatrix}
    12  \\
    0  \\
    \end{bmatrix}
    """)
    st.latex(r"""
    \mathbf{f} = \begin{bmatrix}
    f_1  \\
    f_2  \\
    \end{bmatrix} = 
    \begin{bmatrix}
    1800  \\
    2.16  \\
    \end{bmatrix}
    """)

    # Observações
    st.write("Veja que esta solução é a que minimiza a emissão de CO2, de modo a produzir 2,16 toneladas por semana.")
    st.write("Por outro lado, temos que a outra solução ótima, que maximiza o lucro é:")
    st.latex(r"""
    \mathbf{x} = \begin{bmatrix}
    x_1  \\
    x_2  \\
    \end{bmatrix} = 
    \begin{bmatrix}
    0  \\
    \frac{38}{3}  \\
    \end{bmatrix}
    """)
    st.latex(r"""
    \mathbf{f} = \begin{bmatrix}
    f_1  \\
    f_2  \\
    \end{bmatrix} = 
    \begin{bmatrix}
    3800  \\
    4.43  \\
    \end{bmatrix}
    """)

    # Conclusão
    st.write("Note que agora temos um lucro de R$ 3800,00, mas a emissão de CO2 mais do que dobrou.")
    st.write("Com isso, percebe-se que podemos obter diversas soluções para um POM, sendo que cada uma delas pode retornar um valor melhor para cada uma das funções, podendo penalizar as demais.")

    '''
    
    
    #st.write('Considere uma empresa que atua na produção de açúcar, tal companhia possui dois centros de plantio da cana. De modo que cada um dos centros possui  características únicas, tais como: disponibilidade de mão de obra, tempos de operação do maquinário, além de gerar lucros e níveis de emissão de dióxido de carbono (CO2) diferentes.')
    
    
   



