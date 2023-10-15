# ---------------------------------------
# Imports
# ---------------------------------------
import streamlit as st # pip install streamlit
import database as db # local import

# ---------------------------------------
# Fixed
# ---------------------------------------
st.set_page_config(page_title='Lojinha da Perla - Alterar Senha', layout='centered', page_icon=':lipstick:')
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

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
            db.change_password(
                st.session_state['username'],
                st.session_state['authenticator'].credentials['usernames'][st.session_state['username']]['password']
            )
            st.success('Senha modificada com sucesso')
    except Exception as e:
        st.error(e)