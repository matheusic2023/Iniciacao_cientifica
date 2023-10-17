import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd

def run_conceitos_page():
    st.title("Conceitos Gerais: ")
    st.markdown('Nesta seção serão abordados os principais conceitos da otimização multiobjetivo.')
    st.subheader('Motivação: ')
    st.markdown("""A programação multiobjetivo (POM) pode ser interpretada como uma extensão dos problemas de otimização
                 clássicos trabalhados na graduação, tendo em vista que trabalhamos com a mesma modelagem de restrições
                   e funções objetivos, só que agora há mais de uma função decisão. Todavia, nestes problemas estamos interessados em métodos que possam retornar 
                  possíveis soluções para o problema, de forma a respeitar todas as restrições impostas. """)
    st.markdown("""
        Com isso, por estarmos trabalhando com mais de uma função objetivo, tais funções
          podem ser conflitantes? Por exemplo, pense que uma empresa que produz açúcar deseja maximizar seu lucro
            e minimizar a emissão de CO2 na produção. É possível obter uma solução factível que otimize ambas as
              funções ao mesmo tempo? A resposta é: nem sempre. Basta lembrar que em problemas de Programação Linear
                a maioria das soluções encontradas são vértices de um poliedro convexo. Logo, um vértice que otimiza uma 
                das funções pode não ser o mesmo que otimize a outra. """)

    st.markdown('Deste modo, é necessário discutir novos conceitos para que possamos entender como é encontrado as soluções de um POM.')
    st.subheader('Modelo de um Problema Multiobjetivo: ')
    st.markdown('Considere o vetor $z=f(x)$ formado pelas funções objetivos a serem otimizadas:')
    st.write('')
    st.latex(r"""z = f(x) = \begin{bmatrix} f_1(x) \\ f_2(x) \\ \vdots \\ f_p(x) \end{bmatrix}, \quad \text{onde } f_i(x) = \sum_{j=1}^{n} c_{ij} \cdot x_j
    \quad \forall i = 1, \ldots, p
             """)
    st.markdown("Note que $z$ pode ser escrito em termos de:")
    st.latex(r"""z = f(x) = \begin{bmatrix} f_1(x) \\ f_2(x) \\ \vdots \\ f_p(x) \end{bmatrix}= Cx = \begin{bmatrix}
c_{11} & c_{12} & \cdots & c_{1n} \\
c_{21} & c_{22} & \cdots & c_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
c_{p1} & c_{p2} & \cdots & c_{pn} \\
\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_p \end{bmatrix}
             \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}, \quad \text{onde} \quad c_i \in \mathbb{R}^n \quad \forall i = 1, \ldots, p
    
             """)  
    st.markdown("Onde $C \in \mathbb{R}^{p \\times n}$ é a matriz cuja linha $i$ é formada pelos coeficientes de $f_i(x)$, e $x \in \mathbb{R}^{n}$ é o vetor formado pelas variáveis de decisão.")
    st.write('')
    st.markdown("Por fim, as restrições seguem o mesmo modelo de PL:")
    st.latex(r"""\begin{align*}

\quad & \sum_{j=1}^{n} a_{ij} x_j \leq b_i, \quad i = 1, \ldots, m \\
& x_j \geq 0, \quad j = 1, \ldots, n
\end{align*}
  """)
    st.markdown("Que na forma matricial fica:")
    st.latex(r"""
x \in X = \quad \{x \in \mathbb{R}^n : A x \leq b,  x \geq 0\}



""")
    st.markdown("Deste modo a modelagem geral de um POM é:")
    st.latex(r"""\begin{align*}

\begin{cases}
  max f_1(x) = c_1x\\
  max f_2(x) = c_2x \\
  \dots \\
   max f_p(x) = c_px           
\end{cases}

             \\
             \\             
             
\text{sujeito a:}\begin{cases}
  A x \leq b \\
  x \geq 0\
\end{cases}
\end{align*}
  """)




    st.write('')
   


    st.title('Principais conceitos da Otimização Multiobjetivo:')
    st.markdown(""" Para exemplificar os principais conceitos da Otimização 
Multiobjetivo, vamos lidar com o problema(1) de otimização abaixo:
""")
 
    st.latex(r"max f_1 = 25x_1 + 20x_1 \\"
             "max f_2 = x₁ + 8x₂")
    st.latex(r"""
    \text{sujeito a (Região Factível $X$):}\begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)
    



    st.subheader('Análise do problema:')
    st.markdown('Antes de explorar os conceitos de um POM, vamos entender as características de tal problema:')
    st.markdown("""
  <strong>Região de Factibilidade:</strong> Região formada pelas desigualdades do problema de otimização, que também é denominada Espaço de Decisão; <br> <br> 
<strong>Função de Decisão:</strong> São a(s) função(ões) que queremos maximizar ou minimizar, sujeito às restrições 
                do problema; <br> <br> 
<strong>Variáveis de Decisão:</strong> São as variáveis que modelam o problema de otimização. 
""",unsafe_allow_html=True)
    st.write("Neste exemplo, as restrições de desigualdade formam a seguinte região de factibilidade:")
    x1 = [0,0, 10, 30,40]
    x2 = [0,44, 40, 20,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

    # Adicionando a solução ótima 
    fig.add_trace(go.Scatter(x=[0], y=[44], mode='markers', marker=dict(color='red', size=10), name='Solução Ótima x<sub>-</sub>=(0,44) considerando apenas max f<sub>2</sub>. Com f<sub>2</sub>(x<sub>-</sub>) = 352'))
    fig.add_trace(go.Scatter(x=[30], y=[20], mode='markers', marker=dict(color='blue', size=10), name='Solução Ótima x<sub>+</sub> = (30,20) considerando apenas max f<sub>1</sub>. Com f<sub>1</sub>(x<sub>+</sub>) = 1150'))

    #título
    fig.update_layout(
        title='Região Factível do problema(1)',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='x<sub>2</sub>')
    )
    st.plotly_chart(fig)
    st.markdown('''Como pode-se ver no gráfico acima, temos, para cada uma das funções isoladas, uma solução 
                única que maximiza cada uma destas funções, de forma a respeitar as restrições. Por fim, note que o melhor 
                valor para $f_1$ é 1150 e para $f_2$ é 352. Mas será que existe um vetor $x_* \in X$ que maximize ambas as funções?  
                 
''')
    st.markdown('Para responder tal pergunta, é necessário introduzir um novo conceito.')
    st.subheader('Espaço Critério: ')
    st.markdown("""
    O  **Espaço Critério** $Z = \{z = f(x)\in \mathbb{R}^p : x \in X\}$ é o espaço formado pela aplicação de cada solução($x \in X$) em um vetor 
                $z \in \mathbb{R}^p $. Ou seja, 
                para cada $x \in X$, temos um vetor $z = (z_1,z_2,...,z_p) = f(x) = (f_1(x), f_2(x),...,f_p(x))$.
""")
    st.image('images\espaco_criterio.PNG')
    st.write('Na figura acima temos o Espaço Decisão na esquerda e o Espaço Critério na direita.')
    st.write(' ')
    st.markdown('''**Exemplo do Problema(1):**''')
    st.write(' ')
    st.latex(r"max f_1 = 25x_1 + 20x_1 \\"
             "max f_2 = x₁ + 8x₂")
    st.latex(r"""
    \text{$X$:}\begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)
    st.markdown("""Para encontrar o Espaço Critério do problema(1), devemos obter $x_1$ e $x_2$ em função
                de $f_1$ e $f_2$ e substituir nas desigualdades de $X$:
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
    st.markdown("""Note que em alguns problemas não seria muito simples calcular $x_1,x_2$ em função de $z_1,z_2$.  
                 Agora devemos substituir $x_1,x_2$ nas restrições de $X$:""")
    
    st.latex(r"""
    \text{$X$:}\begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases} \Rightarrow
    \text{$Z$:}\begin{cases}
    7f_1 + 5f_2 \leq 9000 \\
    f_1 - f_2 \leq 960 \\
    11f_1 + 85f_2 \leq 39600 \\
    2f_1 - 5f_2 \geq 0 \\
    25f_2 - f_1 \geq 0
    \end{cases}     
    """)

    st.markdown(""" Com isso, obtemos o Espaço Critério para o problema (1). É evidente que há muito trabalho ao 
                substituir os valores de $x_1,x_2$ nas desigualdades. Todavia, um software que pode facilitar este processo
                é o [Wolfram Mathematica](https://www.citic.unicamp.br/mathematica), disponível para alunos da Unicamp.
""")
    st.write('')
    st.markdown('Veja abaixo o gráfico do Espaço Critério do problema(1): ')

    x1 = [0,880, 1050, 1150,1000,0]
    x2 = [0,352, 330, 190,40,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

    
    #título
    fig.update_layout(
        title='Espaço Critério do problema(1)',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)

    st.markdown("""
Deste modo, temos que qualquer ponto $(f_1,f_2) \\notin Z$ não é correspondende com qualquer $(x_1,x_2) \in X$.
""")
    st.markdown("""
Voltando a pergunta feita anteriormente: existe $(x_1,x_2) \in X$ de modo que possamos maximizar $(f_1, f_2)$  
**Solução:** Basta verificar se o ponto $z = (f_1^*,f_2^*) = (1150,352) \in Z$:
""")
    x1 = [0,880, 1050, 1150,1000,0]
    x2 = [0,352, 330, 190,40,0]

    # Criando o gráfico interativo
    fig = go.Figure()

    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))
    fig.add_trace(go.Scatter(x=[1150], y=[352], mode='markers', marker=dict(color='red', size=10), name='"Solução" que Maximiza f<sub>1</sub> e f<sub>2</sub>'))

    
    #título
    fig.update_layout(
        title='Espaço Critério do problema(1)',
        xaxis=dict(title='f<sub>1</sub>'),
        yaxis=dict(title='f<sub>2</sub>')
    )
    st.plotly_chart(fig)
    st.markdown("""
Note que tal ponto não existe no Espaço Critério, Logo, não há uma representação em $X$ que retorne este
                ponto "ótimo". Portanto, não existe $x=(x_1,x_2) \in X$ que maximize $f_1$ e $f_2$ simultaneamente.

""")
