import plotly.graph_objects as go
"""
    # Criando as coordenadas para o gráfico
    x1 = [0, 0, 10, 30,40,0]
    x2 = [0, 44, 40, 20,0,0]

    # Coordenadas do segmento de reta
    #reta_x1 = [0, 10]
    #reta_x2 = [44, 40]

    # Criando o gráfico interativo
    fig = go.Figure()
    #name='x<sub>1</sub> + x<sub>2</sub> ≤ 2'
    # Adicionando a região
    fig.add_trace(go.Scatter(x=x1, y=x2, fill='toself', fillcolor='rgb(169,169,169)', line=dict(color='rgb(92, 92, 92)'), name='Região Factível'))

    # Adicionando a solução ótima (0,0)
    fig.add_trace(go.Scatter(x=[0], y=[44], mode='markers', marker=dict(color='red', size=10), name='Solução Ótima (0,44) para f<sub>1</sub>'))
    fig.add_trace(go.Scatter(x=[10], y=[40], mode='markers', marker=dict(color='blue', size=10), name='Solução Ótima (10,40) para f<sub>2</sub>'))

    # Adicionando o segmento de reta
    #fig.add_trace(go.Scatter(x=reta_x1, y=reta_x2, mode='lines', line=dict(color='blue', width=3), name='Segmento (0,2) até (2,0)'))

    #título
    fig.update_layout(
        title='Região Factível do problema (1)',
        xaxis=dict(title='x<sub>1</sub>'),
        yaxis=dict(title='x<sub>2</sub>')
    )

    #gráfico no Streamlit
    st.plotly_chart(fig)"""