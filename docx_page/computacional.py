import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
import numpy as np

def run_computacional_page():
    
    st.title("Códigos")

    st.markdown(r"""
Os códigos a seguir foram implementados em Python, com auxílio da biblioteca [PuLP](https://pypi.org/project/PuLP/). 
    Vale ressaltar que toda a teoria estudada na pagina de conceitos gerais está focada na maximização de múltiplas funções objetivas.
    Deste modo, para os algoritmos a seguir, estaremos trabalhando com problemas de maximização. 
        Caso queiramos executar problemas de minimização, devemos nos recordar que:
""", unsafe_allow_html=True)
    
    st.latex(r"""
\begin{align*}
\min f(x) = - \max f(-x)
\end{align*}


""")
    st.markdown(r"### Código do $\varepsilon$-restrito")
    st.markdown(r"""
No código do $\varepsilon$-restrito, temos como entradas as matrizes contendo as desigualdades do tipo "$\leq$", "$\geq$", "$=$" e seus respectivos limitantes dentro dos vetores. Além disso, deve ser informado os coeficientes das funções que deverão ser impostas como restrições, seus respectivos limitantes e também os coeficientes da função que deve ser maximizada. Deste modo, o modelo considerado é da forma:
""", unsafe_allow_html=True)

    st.latex(r"""
\begin{align*}
\max & \, z_i = f_i(x) \\
\text{sujeito a:} & 
\begin{cases}
Ax \leq b \\
Gx \geq g \\
Ex = e \\
f_k(x) \geq \varepsilon_k, & k=1,..., i-1,i+1,...,p \\
x \geq 0
\end{cases}
\end{align*}
""")

    codigo_e_restrito = '''
from pulp import LpProblem, LpMaximize, LpVariable, lpDot, LpStatus
import numpy as np
import matplotlib.pyplot as plt

def e_restrito(n=0, A=0, b=0, G=0, g=0, E=0, e=0, coeficientes_fun_pri=0, num_funcao_restricao=0, matriz_coeficientes_f_aux=0, epsilons=0):
    model = LpProblem(name="large-problem", sense=LpMaximize)
    
    # Variaveis de decisao
    x = [LpVariable(name=f"x{i}", lowBound=0) for i in range(n)]
    
    # Restricoes <=
    if isinstance(A, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
        for i in range(len(A)):
            model += (lpDot(A[i], x) <= b[i], f"restricao_<=_{i}")

    # Restricoes >=
    if isinstance(G, (list, np.ndarray)) and isinstance(g, (list, np.ndarray)):
        for i in range(len(G)):
            model += (lpDot(G[i], x) >= g[i], f"restricao_>=_{i}")

    # Restricoes ==
    if isinstance(E, (list, np.ndarray)) and isinstance(e, (list, np.ndarray)):
        for i in range(len(E)):
            model += (lpDot(E[i], x) == e[i], f"restricao_==_{i}")

    # Funcao Objetivo Principal
    funcao_principal = lpDot(coeficientes_fun_pri, x)
    model += funcao_principal

    # Restricoes epsilon
    if isinstance(matriz_coeficientes_f_aux, (list, np.ndarray)) and isinstance(epsilons, (list, np.ndarray)):
        for i in range(num_funcao_restricao):
            model += (lpDot(matriz_coeficientes_f_aux[i], x) >= epsilons[i], f"restricao_eps_{i}")

    # Resolvendo o problema
    status = model.solve()
    
    # Obtencao da solucao
    sol = np.array([x[i].varValue for i in range(n)])
    coef_f_values = np.vstack((coeficientes_fun_pri,matriz_coeficientes_f_aux))
    
    # Calculando os valores das funcoes objetivas
    value_func_matriz = np.zeros(np.shape(coef_f_values)[0])
    for i in range(np.shape(coef_f_values)[0]):
        value_func_matriz[i] = np.dot(coef_f_values[i], sol)
        
    return sol, status, value_func_matriz
'''
    st.markdown("**Código 1**: código do método do $\\varepsilon$-restrito.")
    st.code(codigo_e_restrito, language='python')

    st.markdown("### Código da Soma Ponderada")
    st.markdown(r"""
No código do método da Soma Ponderada, temos como entradas as mesmas matrizes de restrições do 
    método do $\varepsilon$-restrito. A única diferença é que devemos informar os 
    coeficientes de todas as funções objetivo em uma única matriz, e os valores de $\lambda$ que acompanham cada função 
    . Deste modo, o modelo considerado é da seguinte forma:
""", unsafe_allow_html=True)

    st.latex(r"""
\begin{align*}
\max & \, z = \sum_{k=1}^{p} \lambda_k f_k(x) \\
\text{sujeito a:} & 
\begin{cases}
Ax \leq b \\
Cx \geq d \\
Ex = e \\
x \geq 0
\end{cases}
\end{align*}
""")

    # O código que você forneceu será inserido no componente st.code
    codigo_soma_ponderada = '''
    from pulp import LpProblem, LpMaximize, LpVariable, lpDot, LpStatus
    import numpy as np
    import matplotlib.pyplot as plt

    def soma_ponderada(n, A=0, b=0, C=0, d=0, E=0, e=0, coef_func=0, vetor_lambda=0):
        # Definindo o problema de maximizacao
        model = LpProblem(name="multiobjective-weighted-sum", sense=LpMaximize)

        # Variaveis de decisao
        x = [LpVariable(name=f"x{i}", lowBound=0) for i in range(n)]

        # Restricoes <=
        if isinstance(A, (list, np.ndarray)) and isinstance(b, (list, np.ndarray)):
            for i in range(len(A)):
                model += (lpDot(A[i], x) <= b[i], f"restricao_<=_{i}")

        # Restricoes >=
        if isinstance(C, (list, np.ndarray)) and isinstance(d, (list, np.ndarray)):
            for i in range(len(C)):
                model += (lpDot(C[i], x) >= d[i], f"restricao_>=_{i}")

        # Restricoes ==
        if isinstance(E, (list, np.ndarray)) and isinstance(e, (list, np.ndarray)):
            for i in range(len(E)):
                model += (lpDot(E[i], x) == e[i], f"restricao_==_{i}")

        # Funcao objetivo ponderada
        funcao_principal = lpDot(np.dot(np.transpose(vetor_lambda), coef_func), x)
        model += funcao_principal

        # Resolvendo o problema
        status = model.solve()

        # Obtencao da solucao
        sol = np.array([x[i].varValue for i in range(n)])
        
        # Calculando os valores das funcoes objetivas
        value_func_aux = np.dot(coef_func, sol)
        
        return sol, status, value_func_aux
    '''

    st.code(codigo_soma_ponderada, language='python')
    st.markdown("**Código 2**: código do método da Soma Ponderada.")


    st.subheader("Variação dos Parâmetros - Soma Ponderada")
    st.markdown(r"""
Para analisar as diferentes soluções do método da soma ponderada, desenvolvemos o código `varrer_lambda()`. Esse código foi criado especificamente para problemas bi-objetivo. Inicialmente, definimos o número de passos percorridos em uma malha uniforme de zero a um. Na primeira iteração, temos $\lambda_1 = 0$, o que implica $\lambda_2 = 1$. Nas iterações subsequentes, o valor de $\lambda_1$ é determinado pelo número de divisões da malha uniforme, com $\lambda_2 = 1 - \lambda_1$. Tal abordagem garante pesos distintos e combinações equilibradas para ambos os $\lambda$'s.
""", unsafe_allow_html=True)


    codigo_varrer_lambda = '''
    def varrer_lambda(n_passos):
        solutions = []
        valor_f = []
        lambdas = np.linspace(0,1,n_passos)  
        
        for lambda1 in lambdas:
            #lambda2 = np.random.uniform(0, lambda1)
            lambda2 = 1 - lambda1 
            vetor_lambda = np.array([lambda1, lambda2])
            sol, status,f_values = soma_ponderada(n, A, b, C, d, E, e, coef_func, vetor_lambda)

            if status == 1:
                solutions.append(tuple(np.round(sol, decimals=10)))  
                valor_f.append(tuple(np.round(f_values, decimals=10)))

        # Remover duplicatas
        solutions_distinct = list(set(solutions))
        f_values_distintos = list(set(valor_f))
        return solutions_distinct,f_values_distintos
    '''

    st.code(codigo_varrer_lambda, language='python')
    st.markdown("**Código 3**: código que varia os $\lambda$'s de problemas bi-objetivo.")


    st.subheader(r"Variação dos Parâmetros - $\varepsilon$-restrito")
    st.markdown(r"""
Ademais, o código `percorrer_epsilon()` também é específico para problemas bi-objetivo, porém possui mais parâmetros de entrada. Primeiramente, devemos informar o $\varepsilon$ inicial do problema, o $\varepsilon$ final e a quantidade de passos que devemos percorrer na malha uniforme entre o valor inicial e final. Diferentemente do algoritmo anterior, não temos um $\varepsilon$ "ideal" para todos os tipos de problema. Deste modo, cabe ao tomador de decisões escolher qual seria a tolerância mínima que deve ser respeitada pelo método.
""", unsafe_allow_html=True)

    codigo_percorrer_epsilon = '''
    def percorrer_epsilon(epsilon_range=None):
        solutions = []
        valor_f = []
        
        for epsilon in epsilon_range:
            epsilons = np.full(num_funcao_restricao, epsilon)  
            sol, status,f_val = e_restrito(n, A, b, G, g, E, e, coeficientes_fun_pri, num_funcao_restricao, matriz_coeficientes_f_aux, epsilons)

            if status == 1:  # 1 indica 'Optimal'
                solutions.append(tuple(np.round(sol, decimals=10)))  
                valor_f.append(tuple(np.round(f_val, decimals=10)))
            else:
                pass

        # Remover duplicatas
        solutions_distinct = list(set(solutions))
        valor_f_distinct = list(set(valor_f))
        return solutions_distinct,valor_f_distinct
    '''

    st.code(codigo_percorrer_epsilon, language='python')
    st.markdown("**Código 4**: código que varia o $ \\varepsilon $ de problemas bi-objetivo.",unsafe_allow_html=True)





