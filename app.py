import streamlit as st
from streamlit_option_menu import option_menu
from pages import intro_page
from pages.intro_page import run_intro_page
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
            "Menu", ['Apresentação', 'Tabela', 'Informações'], 
            icons = ['plus-circle-fill', 'file-spreadsheet-fill', 'info-circle-fill'],
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
               
