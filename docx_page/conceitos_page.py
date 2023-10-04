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

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.latex(r"max f_1 = 25x_1 + 20x_1 \\"
             "max f_2 = x₁ + 8x₂")
    st.latex(r"""
    \begin{cases}
    x_1 + x_2 \leq 50 \\
    2x_1 + x_2 \leq 80 \\
    2x_1 + 5x_2 \leq 220 \\
    x_1,x_2 \geq 0
    \end{cases}
    """)




    st.write('Uma das principais áreas de pesquisa na matemática aplicada é a programação matemática. O objeto de estudo dessa área é a otimização de uma função, denominada função objetivo, que pode ser maximizada ou minimizada, de modo que tal função é sujeita a restrições que são representadas por desigualdades.')
    st.subheader('Quais são as principais áreas de estudo da programação matemática na graduação?')