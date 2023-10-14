# ---------------------------------------
# Imports
# ---------------------------------------
import streamlit as st # pip install streamlit
import streamlit_authenticator as stauth # pip install streamlit_authenticator

import database as db # local import

# ---------------------------------------
# Config
# ---------------------------------------
# Page config
st.set_page_config(page_title='Lojinha da Perla', layout='wide', page_icon=':lipstick:')
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Cookies
cookie_df = db.leitura("SELECT * FROM cookie")
for row in cookie_df.values:
    cookie = {
        'key': row[0],
        'expiry_days': row[1],
        'name': row[1]
    }

# Users
user_df = db.leitura("SELECT * FROM users")
usernames = dict()
for row in user_df.values:
    usernames[row[0]] = {
        'email': row[1],
        'name': row[2],
        'password': row[3]
    }

# Config as dict
config = {
    'cookie': cookie,
    'credentials': {'usernames': usernames},
    'preauthorized': {'emails': []}
}

# ---------------------------------------
# User authentication
# ---------------------------------------
st.session_state['authenticator'] = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
st.session_state['authenticator'].login('Login', 'main')

# ---------------------------------------
# Page
# ---------------------------------------
if st.session_state['authentication_status'] is False:
    st.error('Username/passwords is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
elif st.session_state['authentication_status']:

    # Sidebar
    # --------------------
    st.sidebar.write(f'Logado como {st.session_state["name"]}')
    st.session_state['authenticator'].logout('Sair', 'sidebar', key='Logout_button')

    # Main page
    # --------------------
    st.title('Bem-vindo(a) a Lojinha da Perla')