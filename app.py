import streamlit as st
from streamlit_option_menu import option_menu
from docx import Document
from docx_page import run_intro_page
from docx_page.run_intro_page import run_intro_page

from docx_page import conceitos_page
from docx_page.conceitos_page import run_conceitos_page

from docx_page import metodos
from docx_page.metodos import run_metodos_page

from docx_page import computacional
from docx_page.computacional import run_computacional_page
# Website's general configurations

st.set_page_config(
     page_icon = "images/logoimecc.png",
     page_title = "Projeto de IC",
     layout = "wide",
     initial_sidebar_state = "expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #D3D3D3;
    }
</style>
""", unsafe_allow_html=True)
    # Sidebar
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.image("images/logoimecc.png", use_column_width = 'auto')





with st.sidebar:
        page = option_menu(
            "Menu", ['Apresentação', 'Conceitos Gerais','Métodos Exatos', 'Implementação Computacional','Informações'], 
            icons = ['plus-circle-fill', 'book-fill','graph-up-arrow', 'pc-display-horizontal','info-circle-fill'],
            menu_icon = "house",
            styles = {
                "container": {"padding": "0!important", "background-color": "#D3D3D3"},                   
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#a9d4de"},
                "nav-link-selected": {"font-size": "15px", "font-weight": "normal"},
            }
        )
        
#Páginas do Projeto
if page=='Apresentação':
        run_intro_page()
elif page=='Conceitos Gerais':
        run_conceitos_page()  
elif page=='Métodos Exatos':
        run_metodos_page()               
elif page=='Implementação Computacional':
        run_computacional_page()               
