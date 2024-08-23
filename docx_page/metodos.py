import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd

def run_metodos_page():
    st.title("Métodos Exatos: ")
    st.subheader('Introdução:')
    st.markdown(""" Na **otimização multiobjetivo**, uma das principais abordagens para obter soluções não dominadas e eficientes é 
                por meio da **técnica escalarização**. Essa técnica visa transformar um problema multiobjetivo em um problema de otimização 
                mono-objetivo.   <br> 
                <br>
                Neste trabalho, serão apresentados dois métodos comuns de escalarização:
                <br>
                <ol>
                 <li> **Método da Soma Ponderada**: Nesse método, as funções objetivas são ponderadas
                      por coeficientes específicos. A combinação linear dessas funções resulta em uma única função objetivo, que é então otimizada;
                 <li>**Método do $\epsilon$-Restrito (ou $\epsilon$-Constraint)**: Aqui, uma das funções objetivas é otimizada, 
                      enquanto as demais são tratadas como restrições. O tomador de decisão especifica o limiar que deve ser respeitado nas restrições para cada uma das funções restantes.
            <br>
            <br>
            

""",unsafe_allow_html=True)
    st.markdown(""" A base teórica para os métodos apresentados neste trabalho foi baseada no livro 
                 [Multiobjective Linear and Integer Programming](https://link.springer.com/book/10.1007/978-3-319-28746-1), 
                escrito pelos autores **Carlos Henggeler Antunes, Maria João Alves e João Clímaco**. 
                Além disso, utilizamos os slides do
                 [Curso de otimização multiobjetivo](http://paginapessoal.utfpr.edu.br/angeloaliano/curso-de-otimizacao-multiobjetivo), elaborado pelo autor **Angelo Aliano Filho**.
  """,unsafe_allow_html=True)
    st.subheader("Método do $\epsilon$-restrito:")
    st.markdown(""" **Definição**: <br>
                                    <ul>
                                        <li>em um Problema de Otimização Multi-objetivo (POM) com p funções objetivas $(f_1(x), f_2(x), …, f_p(x))$, 
                selecionamos uma dessas funções (digamos $f_i(x)$) para otimização.
                                        <li>as outras funções, $f_j(x)$ com $(j \\neq i)$, são consideradas restrições no novo problema mono-objetivo,
                 onde $f_j(x) \geq e_j$ é a forma como $f_j$ é restringida a um valor específico.
                            
""",unsafe_allow_html=True)
    st.markdown(""" **Teorema 1**: <br>
                se $x^*$ é a solução do seguinte problema mono-objetivo
""",unsafe_allow_html=True)

   
    st.latex(r"""
        \begin{align*}
        \max & \, f_i(x) \\
        \text{s.a} & 
        \begin{cases}
        x \in X \\
        f_k(x) \geq e_k, & k=1,..., i-1,i+1,...,p
        \end{cases}
        \end{align*}
    """)

    st.markdown(""" então $x^*$ é uma solução fracamente eficiente para o problema multiobjetivo original.
""",unsafe_allow_html=True)

    st.markdown(""" **Exemplo 1**: <br>
                Considere o seguinte problema bi-objetivo


""",unsafe_allow_html=True)
    st.latex(r"""
        \begin{align*}
        \max & \, f_1(x) = x_1+x_2 \\
        \max & \, f_2(x) = x_2 - x_1 \\
        \text{s.a} & 
        \begin{cases}
        x_1 + 4x_2 \leq 20 \\
        2x_1 + x_2 \leq 12 \\
        x_1  \leq 5 \\
        x_1,x_2 \geq 0
        \end{cases}
        \end{align*}
    """)
    st.markdown(""" Tome a função $f_2(x)$ como restrição e a função $f_1(x)$ como função objetivo:
""",unsafe_allow_html=True)
    st.latex(r"""
        \begin{align*}
        \max & \, f_1(x) = x_1+x_2 \\
        \text{s.a} & 
        \begin{cases}
        x_1 + 4x_2 \leq 20 \\
        2x_1 + x_2 \leq 12 \\
        x_1  \leq 5 \\
        x_1,x_2 \geq 0 \\
        x_2 - x_1 \geq \epsilon
             
        \end{cases}
        \end{align*}
    """)
    st.markdown(""" Temos por meio da figura abaixo as soluções obtidas por meio das variações dos $\epsilon$'s
""",unsafe_allow_html=True)
    if st.checkbox("Variação dos $\epsilon$'s:  ", False):
        st.image('images/e_restritogif.gif')
    st.markdown("""Com isso, percebe-se que tal método é de fácil implementação e retorna soluções de pareto. 
                No entanto, ao introduzir novas restrições no problema, a estrutura original do poliedro é 
                alterada e pode ocorrer que a região factível se torne vazia em determinados casos. No exemplo da 
                figura acima, se aumentarmos o valor de $\epsilon$ para mais de 5, o problema se tornará infactível.

""",unsafe_allow_html=True)
    st.subheader("Método da Soma Ponderada:")
    st.markdown("""Um dos procedimentos mais utilizados em um POM é o método da soma ponderada.
Tal método se baseia em resolver um problema mono-objetivo, cuja função objetivo é uma soma ponderada das $p$
funções originais. Com isso, para cada função $f_k$, associamos um peso $\lambda_k \geq 0$.

""",unsafe_allow_html=True)
    st.markdown(""" **Definição 2**: <br>
                dado $\lambda_k \geq 0$, com $k=1,...,p$, temos que o método da soma ponderada
                reduz o POM para o seguinte problema mono-objetivo:            
""",unsafe_allow_html=True)
    st.latex(r"""
        \begin{align*}
        \max & \, z = \sum_{k=1}^{p} \lambda_k f_k(x) \\
        \text{s.a} & 
        \begin{cases}
        x \in \mathcal{X}
        \end{cases}
        \end{align*}
    """)
    st.markdown(""" **Teorema 2**: <br>
                dado que $\lambda_k > 0$ e $\sum_{k=1}^{p} \lambda_k = 1$. Se $x^*$ é a solução do seguinte problema mono-objetivo
""",unsafe_allow_html=True)

   
    st.latex(r"""
        \begin{align*}
        \max & \, z = \sum_{k=1}^{p} \lambda_k f_k(x) \\
        \text{s.a} & 
        \begin{cases}
        x \in \mathcal{X}
        \end{cases}
        \end{align*}
    """)
    st.markdown(""" então $x^*$ é uma solução fracamente eficiente para o problema multiobjetivo original.
""",unsafe_allow_html=True)
    
    





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


    