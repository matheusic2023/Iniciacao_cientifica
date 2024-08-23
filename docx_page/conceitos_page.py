import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd

def run_conceitos_page():
    st.title("Conceitos Gerais")

    st.markdown("""
    A base teórica para os conceitos apresentados nesta seção foi baseada no livro 
    [Multiobjective Linear and Integer Programming](https://link.springer.com/book/10.1007/978-3-319-28746-1), 
    escrito pelos autores **Carlos Henggeler Antunes, Maria João Alves e João Clímaco**. Além disso, utilizamos os slides do
    [Curso de otimização multiobjetivo](http://paginapessoal.utfpr.edu.br/angeloaliano/curso-de-otimizacao-multiobjetivo), 
    elaborado pelo autor **Angelo Aliano Filho**.
    """, unsafe_allow_html=True)

    st.subheader('Motivação')
    st.markdown("""
    A programação multiobjetivo (POM) pode ser vista como uma extensão dos problemas de otimização clássicos, 
    onde trabalhamos com mais de uma função objetivo. Nesses problemas, buscamos métodos que possam retornar 
    soluções que respeitem todas as restrições impostas. No entanto, como estamos lidando com múltiplas funções 
    objetivo, estas podem ser conflitantes.

    Por exemplo, considere uma empresa que deseja maximizar o lucro e, ao mesmo tempo, minimizar a emissão de CO2 
    na produção. É possível obter uma solução que otimize ambas as funções ao mesmo tempo? Nem sempre. Em problemas 
    de Programação Linear, a maioria das soluções são vértices de um poliedro convexo, e um vértice que otimiza uma função 
    pode não otimizar a outra.
    """)

    st.markdown("""
    Portanto, é necessário discutir novos conceitos para entender como encontrar soluções em um POM.
    """)

    st.subheader('Modelo de um Problema Multiobjetivo')
    st.markdown('Considere o vetor $z=f(x)$ formado pelas funções objetivo a serem otimizadas:')
    st.latex(r"""
    z = f(x) = \begin{bmatrix} f_1(x) \\ f_2(x) \\ \vdots \\ f_p(x) \end{bmatrix}, \quad \text{onde } f_i(x) = \sum_{j=1}^{n} c_{ij} \cdot x_j
    \quad \forall i = 1, \ldots, p
    """)

    st.markdown("Note que $z$ pode ser escrito em termos de:")
    st.latex(r"""
    z = f(x) = Cx = \begin{bmatrix}
    c_{11} & c_{12} & \cdots & c_{1n} \\
    c_{21} & c_{22} & \cdots & c_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    c_{p1} & c_{p2} & \cdots & c_{pn} \\
    \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_p \end{bmatrix}
    \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}, \quad \text{onde} \quad c_i \in \mathbb{R}^n \quad \forall i = 1, \ldots, p
    """)

    st.markdown("Onde $C \in \mathbb{R}^{p \\times n}$ é a matriz cujas linhas são formadas pelos coeficientes de $f_i(x)$, e $x \in \mathbb{R}^{n}$ é o vetor formado pelas variáveis de decisão.")

    st.markdown("Por fim, as restrições seguem o mesmo modelo de PL:")
    st.latex(r"""
    \begin{align*}
    \quad & \sum_{j=1}^{n} a_{ij} x_j \leq b_i, \quad i = 1, \ldots, m \\
    & x_j \geq 0, \quad j = 1, \ldots, n
    \end{align*}
    """)

    st.markdown("Na forma matricial, fica:")
    st.latex(r"""
    x \in X = \quad \{x \in \mathbb{R}^n : A x \leq b,  x \geq 0\}
    """)

    st.markdown("Deste modo, a modelagem geral de um POM é:")
    st.latex(r"""
    \begin{align*}
    \begin{cases}
    \max f_1(x) = c_1x\\
    \max f_2(x) = c_2x \\
    \dots \\
    \max f_p(x) = c_px           
    \end{cases}
    \\
    \\
    \text{sujeito a:}\begin{cases}
    A x \leq b \\
    x \geq 0
    \end{cases}
    \end{align*}
    """)

    st.title('Principais Conceitos da Otimização Multiobjetivo')
    st.markdown("Para exemplificar os principais conceitos da Otimização Multiobjetivo, vamos considerar o problema(1) de otimização abaixo:")

    st.latex(r"max f_1 = 25x_1 + 20x_2 \\"
             "max f_2 = x_1 + 8x_2")
    st.latex(r"""
    \text{sujeito a (Região Factível $X$):}\begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)

    st.subheader('Análise do Problema')
    st.markdown("""
    Antes de explorar os conceitos de um POM, vamos entender as características deste problema:
    
    * **Região de Factibilidade:** Região formada pelas desigualdades do problema de otimização, também denominada Espaço de Decisão.
    * **Função de Decisão:** São as funções que queremos maximizar ou minimizar, sujeito às restrições do problema.
    * **Variáveis de Decisão:** São as variáveis que modelam o problema de otimização.
    """)

    st.write("Neste exemplo, as restrições de desigualdade formam a seguinte região de factibilidade:")
    x1 = [0,0, 10, 30,40]
    x2 = [0,44, 40, 20,0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[0], y=[44], mode='markers', marker=dict(color='red', size=10), name='Solução Ótima (0,44) para max f2 = 352'))
    fig.add_trace(go.Scatter(x=[30], y=[20], mode='markers', marker=dict(color='blue', size=10), name='Solução Ótima (30,20) para max f1 = 1150'))
    fig.update_layout(
        title='Região Factível do problema(1)',
        xaxis=dict(title='x1'),
        yaxis=dict(title='x2')
    )
    st.plotly_chart(fig)

    st.markdown("""
    Como pode-se ver no gráfico acima, temos, para cada uma das funções isoladas, uma solução única que maximiza cada uma delas, respeitando as restrições. Note que o melhor valor para $f_1$ é 1150 e para $f_2$ é 352. Mas será que existe um vetor $x_* \in X$ que maximize ambas as funções?
    """)
    st.markdown("Para responder tal pergunta, é necessário introduzir um novo conceito.")

    st.subheader('Espaço Critério')
    st.markdown("""
    O **Espaço Critério** $Z = \{z = f(x)\in \mathbb{R}^p : x \in X\}$ é o espaço formado pela aplicação de cada solução($x \in X$) em um vetor $z \in \mathbb{R}^p$. Ou seja, para cada $x \in X$, temos um vetor $z = (z_1,z_2,...,z_p) = f(x) = (f_1(x), f_2(x),...,f_p(x))$.
    """)

    st.image('images/espaco_criterio.PNG')
    st.write('Na figura acima, temos o Espaço Decisão à esquerda e o Espaço Critério à direita.')
    st.markdown('**Exemplo do Problema(1):**')
    st.latex(r"max f_1 = 25x_1 + 20x_2 \\"
             "max f_2 = x₁ + 8x₂")
    st.latex(r"""
    \text{$X$:}\begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)

    st.markdown("""
    Para encontrar o Espaço Critério do problema(1), devemos obter $x_1$ e $x_2$ em função de $f_1$ e $f_2$ e substituir nas desigualdades de $X$:
    """)
    st.latex(r"""
    \begin{cases}
    25x_1 + 20x_2 = f_1 \\
    x_1 + 8x_2 = f_2
    \end{cases} \Rightarrow
    \begin{cases}
    x_1 = \frac{2f_1 - 5f_2}{45} \\
    x_2 = \frac{25f_2 - z_1}{180}
    \end{cases}             
    """)
    st.markdown("""
    Agora, substituímos $x_1$ e $x_2$ nas restrições de $X$ para obter o espaço critério $Z$:
    """)
    st.latex(r"""
    \text{$Z$:}\begin{cases}
    7f_1 + 5f_2 \leq 9000 \\
    f_1 - f_2 \leq 960 \\
    11f_1 + 85f_2 \leq 39600 \\
    2f_1 - 5f_2 \geq 0 \\
    25f_2 - f_1 \geq 0
    \end{cases}
    """)

    st.markdown("""
    Com isso, obtemos o Espaço Critério para o problema(1). Observar que este processo pode ser facilitado com o uso de softwares como o [Wolfram Mathematica](https://www.citic.unicamp.br/mathematica).
    """)
    st.markdown('Veja abaixo o gráfico do Espaço Critério do problema(1):')

    x1 = [0,880, 1050, 1150,1000,0]
    x2 = [0,352, 330, 190,40,0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.update_layout(
        title='Espaço Critério do problema(1)',
        xaxis=dict(title='f1'),
        yaxis=dict(title='f2')
    )
    st.plotly_chart(fig)

    st.markdown("""
    Voltando à pergunta anterior: existe $(x_1,x_2) \in X$ de modo que possamos maximizar simultaneamente $f_1$ e $f_2$?  
    **Solução:** Verifique se o ponto $z^* = (f_1^*,f_2^*) = (1150,352) \in Z$:
    """)

    fig.add_trace(go.Scatter(x=[1150], y=[352], mode='markers', marker=dict(color='red', size=10), name='Ponto que Maximiza f1 e f2'))
    fig.update_layout(
        title='Espaço Critério do problema(1)',
        xaxis=dict(title='f1'),
        yaxis=dict(title='f2')
    )
    st.plotly_chart(fig)

    st.markdown("""
    Note que tal ponto não existe no Espaço Critério, logo, não há uma representação em $X$ que retorne este ponto "ótimo". Portanto, não existe $x=(x_1,x_2) \in X$ que maximize $f_1$ e $f_2$ simultaneamente.
    """)

    st.title("Relações de Dominância")
    st.markdown("""
    Antes de introduzirmos os conceitos de soluções eficientes para um Problema de Otimização Multiobjetivo, vamos definir a relação de dominância entre duas soluções.
    """, unsafe_allow_html=True)

    st.markdown("""
    **Dominância entre soluções:** considere duas soluções, $x^*$ e $\\bar{x}$, pertencentes ao espaço decisão $X$. A solução $x^*$ domina $\\bar{x}$ se as seguintes condições são satisfeitas:
    """, unsafe_allow_html=True)

    st.markdown("""
    1. $f_j(x^*) \geq f_j(\\bar{x})$ para todo $j=1, \ldots, p$;
    2. $ f_j(x^*) > f_j(\\bar{x})$ para ao menos um $j$.
    """, unsafe_allow_html=True)

    st.markdown("**Notação:** $x^* \preceq \\bar{x}$.")

    st.markdown("""
    **Definição (Dominância Forte):** A solução $x^*$ domina fortemente a solução $\\bar{x}$ se a seguinte condição é satisfeita:
    """, unsafe_allow_html=True)

    st.latex(r"f_j(x^*) > f_j(\bar{x}), \text{ para } j=1,...,p.")

    st.markdown("""
    **Definição (Dominância Fraca):** A solução $x^*$ domina fracamente a solução $\\bar{x}$ se as seguintes condições são satisfeitas:
    """, unsafe_allow_html=True)

    st.markdown("""
    1. $f_j(x^*) \geq f_j(\\bar{x})$ para todo $j=1, \ldots, p$; 
    2. $f_j(x^*) \\neq f_j(\\bar{x})$ para ao menos um $j$;
    3. $x^*$ não domina fortemente $\\bar{x}$.
    """, unsafe_allow_html=True)

    st.subheader("Soluções Eficientes, Pontos não-dominados e Fronteira de Pareto")

    st.markdown("""
    Um dos principais conceitos de Otimização Multiobjetivo é o de soluções eficientes, pois é por meio deste que vamos compreender quais soluções possuem mais significância para um Problema de Otimização Multiobjetivo.
    """, unsafe_allow_html=True)

    st.markdown("**Definição (Solução Eficiente):** A solução $x^*$ é dita eficiente se, e somente se, não existe nenhum $x$ no espaço de decisão $X$, de modo que $x \preceq x^*$.")

    st.markdown("**Definição (Ponto não-dominado):** O ponto $z(x)=\left(f_1(x), f_2(x), \ldots, f_p(x)\\right) \in Z$ é dito não dominado se, e somente se, $x$ é uma solução eficiente.")
    
    st.markdown("**Exemplo (Dominância entre Pontos)**:")
    
    fig.update_layout(
        title='Espaço Critério',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )

    
    
    x1 = [0,880, 1050, 1150,1000,0]
    x2 = [0,352, 330, 190,40,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=[1], y=[2], mode='markers', marker=dict(color='red', size=10), name='Pontos dominados'))
    fig.add_trace(go.Scatter(x=[2], y=[5], mode='markers', marker=dict(color='red', size=10), showlegend=False,name='Pontos dominados'))
    fig.add_trace(go.Scatter(x=[3], y=[4], mode='markers', marker=dict(color='red', size=10), showlegend=False,name='Pontos dominados'))
    fig.add_trace(go.Scatter(x=[4], y=[3], mode='markers', marker=dict(color='red', size=10), showlegend=False,name='Pontos dominados'))
    fig.add_trace(go.Scatter(x=[5], y=[2], mode='markers', marker=dict(color='red', size=10), showlegend=False,name='Pontos dominados'))
    fig.add_trace(go.Scatter(x=[3], y=[6], mode='markers', marker=dict(color='green', size=10), name='Pontos não-dominados'))
    fig.add_trace(go.Scatter(x=[4], y=[5], mode='markers', marker=dict(color='green', size=10), showlegend=False,name='Pontos não-dominados'))
    fig.add_trace(go.Scatter(x=[5], y=[4], mode='markers', marker=dict(color='green', size=10), showlegend=False,name='Pontos não-dominados'))
    fig.add_trace(go.Scatter(x=[6], y=[3], mode='markers', marker=dict(color='green', size=10), showlegend=False,name='Pontos não-dominados'))
    fig.add_trace(go.Scatter(x=[2], y=[6], mode='markers', marker=dict(color='blue', size=10), name='Pontos fracamente não-dominados'))
    fig.add_trace(go.Scatter(x=[6], y=[2], mode='markers', marker=dict(color='blue', size=10), showlegend=False,name='Pontos fracamente não-dominados'))
    
    
    
    #título
    fig.update_layout(
        title='Relação de Dominância entre Pontos',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)


    st.markdown("**Definição (Conjunto Eficiente):** O conjunto eficiente $X^*$ é formado por todos os elementos de $X$ que não são dominados por outros elementos de $X$. Em outras palavras, $X^*=\left\{x^* \in X: x \\npreceq x^*, \\forall x \in X\\right\}$.")



    st.markdown("**Definição (Fronteira de Pareto):** A fronteira de Pareto, denotada por $Z^*$ é a imagem do conjunto eficiente $X^*$, ou seja, $Z^*=\left\{z^* \in \mathbb{R}^p: z^*=f\left(x^*\\right), \\forall x^* \in X^*\\right\}$.")

    

    st.markdown("""
    A fronteira de Pareto é de extrema importância nos Problemas de Otimização Multiobjetivo, pois fornece as soluções mais adequadas ao problema. No entanto, a decisão final sobre qual solução é a mais apropriada dentro dessa fronteira é uma responsabilidade exclusiva do tomador de decisões. Ele deve considerar cuidadosamente as necessidades e objetivos específicos do problema para fazer a escolha mais adequada.
    """)

    


    st.markdown(r"""
    **Definição (Fronteira de Pareto):** A fronteira de Pareto, denotada por $Z^*$ é a imagem do conjunto eficiente $X^*$, ou seja, $Z^*=\left\{z^* \in \mathbb{R}^p: z^*=f\left(x^*\right), \forall x^* \in X^*\right\}$
    """, unsafe_allow_html=True)

    
    st.markdown(r"""
    A fronteira de Pareto é de extrema importância nos Problemas de Otimização Multiobjetivo, pois fornece as soluções mais adequadas ao problema. No entanto, a decisão final sobre qual solução é a mais apropriada dentro dessa fronteira é uma responsabilidade exclusiva do tomador de decisões. Ele deve considerar cuidadosamente as necessidades e objetivos específicos do problema para fazer a escolha mais adequada.
    """, unsafe_allow_html=True)

    st.markdown(r"""
    **Exemplo (Fronteira de Pareto do Problema(1) ):** Por meio das definições anteriores e das inequações do espaço critério do problema(1), obtemos que a fronteira de Pareto é dada por:
 
    """, unsafe_allow_html=True)
    
    x1 = [0,880, 1050, 1150,1000,0]
    x2 = [0,352, 330, 190,40,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=[880, 1050, 1150], y=[352, 330, 190], mode='lines', line=dict(color='red', width=8), name='Fronteira de Pareto'))

    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[880], y=[352], mode='markers', marker=dict(color='green', size=10), name='"Solução" que Maximiza f<sub>2</sub>'))
    fig.add_trace(go.Scatter(x=[1150], y=[190], mode='markers', marker=dict(color='blue', size=10), name='"Solução" que Maximiza f<sub>1</sub>'))
    fig.add_trace(go.Scatter(x=[1050], y=[330], mode='markers', marker=dict(color='yellow', size=10), name='"Solução" Intermediária'))

    
    #título
    fig.update_layout(
        title='Fronteira de Pareto do Problema(1)',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)
  
  