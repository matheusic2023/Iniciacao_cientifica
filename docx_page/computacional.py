import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import plotly.graph_objects as go
from io import BytesIO
import base64
import pandas as pd
import numpy as np

def run_computacional_page():
    
    st.latex(r"""
        \begin{align*}
        \min & \, f_1(x) = 3x_1+3.52x_2+2.3x_3+0.6x_4+x_5+x_6 \\
        \max & \, f_2(x) = 12x_1+19.4x_2+21.5x_3+7.2x_4+3.5x_5+22.2x_6\\
        \text{s.a} & 
        \begin{cases}
        0.6x_1 + 0x_2 +0x_3+78.4x_4+ 36x_5 +60x_6 \leq 68 \\
        4x_1 + 2.7x_2 + 1.1x_3+ 0.1x_4+0.5x_5 +0.3x_6 \leq 10 \\
        120x_1 + 48.6x_2 + 56.1x_3+ 0.6x_4+ 0x_5+ 9.8x_6 \leq 2000 \\
        0.12x_1 + 0x_2 + 0x_3+ 4.7x_4+ 3x_5+ 33.8x_6 \leq 36 \\
        92x_1 + 136.6x_2 + 119.2x_3+ 358.1x_4+ 167x_5+ 331.4x_6 \leq 2000 \\
        x_1,x_2,x_3,x_4,x_5,x_6 \geq 0
        \end{cases}
        \end{align*}
    """)
    st.subheader("Teste com $\epsilon-$restrito:")
    st.latex(r"""
        \begin{align*}
        \max & \, f_1(x) = -3x_1 - 3.52x_2 -2.3x_3 -0.6x_4 -x_5 -x_6 \\
        
        \text{s.a} & 
        \begin{cases}
        0.6x_1 + 0x_2 +0x_3+78.4x_4+ 36x_5 +60x_6 \leq 68 \\
        4x_1 + 2.7x_2 + 1.1x_3+ 0.1x_4+0.5x_5 +0.3x_6 \leq 10 \\
        120x_1 + 48.6x_2 + 56.1x_3+ 0.6x_4+ 0x_5+ 9.8x_6 \leq 2000 \\
        0.12x_1 + 0x_2 + 0x_3+ 4.7x_4+ 3x_5+ 33.8x_6 \leq 36 \\
        92x_1 + 136.6x_2 + 119.2x_3+ 358.1x_4+ 167x_5+ 331.4x_6 \leq 2000 \\
        12x_1+19.4x_2+21.5x_3+7.2x_4+3.5x_5+22.2x_6 \geq \epsilon \\
        x_1,x_2,x_3,x_4,x_5,x_6 \geq 0
        \end{cases}
        \end{align*}
    """)