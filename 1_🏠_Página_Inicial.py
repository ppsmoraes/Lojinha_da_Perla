# ---------------------------------------
# Imports
# ---------------------------------------
import streamlit as st # pip install streamlit
import streamlit_authenticator as stauth # pip install streamlit_authenticator

import database as db # local import

# ---------------------------------------
# Config
# ---------------------------------------
st.set_page_config(page_title='Lojinha da Perla', layout='centered', page_icon=':lipstick:')

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state['authentication_status'] in [None, False]:
    # Page config
    hide_st_style = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .st-emotion-cache-6qob1r {visibility: hidden;}
        .st-emotion-cache-12nf2cl {visibility: hidden;}
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
    st.session_state['authenticator'].login('Lojinha da Perla', 'main')
    if st.session_state['authentication_status'] is False:
        st.error('Username/passwords is incorrect')

# ---------------------------------------
# Page
# ---------------------------------------
elif st.session_state['authentication_status']:
    # Page config
    hide_st_style = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.write(f'Logado como {st.session_state["name"]}')
    st.session_state['authenticator'].logout('Sair', 'sidebar', key='Logout_button')

    # Main page
    st.title('Bem-vindo(a) a Lojinha da Perla')