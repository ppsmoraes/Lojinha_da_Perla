# ---------------------------------------
# Imports
# ---------------------------------------
import yaml # Native python module
from yaml.loader import SafeLoader # Native python module

import streamlit as st # pip install streamlit
import streamlit_authenticator as stauth # pip install streamlit_authenticator

# ---------------------------------------
# Fixed
# ---------------------------------------
st.set_page_config(page_title='Lojinha da Perla', layout='wide', page_icon=':lipstick:')
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---------------------------------------
# Login
# ---------------------------------------
# Load hashed passwords
with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=SafeLoader)

# ---------------------------------------
# Page
# ---------------------------------------
if st.session_state['authentication_status']:

    # Sidebar
    # --------------------
    st.sidebar.write(f'Logado como {st.session_state["name"]}')
    st.session_state['authenticator'].logout('Sair', 'sidebar', key='Logout_button')

    # Main page
    # --------------------
    try:
        if st.session_state['authenticator'].reset_password(st.session_state['username'], 'Alterar senha', 'main'):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)