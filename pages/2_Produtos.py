# ---------------------------------------
# Imports
# ---------------------------------------
import streamlit as st # pip install streamlit
import database as db # local import

# ---------------------------------------
# Fixed
# ---------------------------------------
st.set_page_config(page_title='Lojinha da Perla - Produtos', layout='wide', page_icon=':lipstick:')
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

    itens_df = db.leitura("SELECT * FROM itens;")

    itens_df

    insert_item_form = st.form('insert_item', clear_on_submit=True)
    name = insert_item_form.text_input('Nome').lower()
    cost = insert_item_form.text_input('Custo').lower()
    value = insert_item_form.text_input('Preço').lower()
    quantity = insert_item_form.text_input('Quantidade').lower()
    bar_code = insert_item_form.text_input('Código de barras').lower()

    if insert_item_form.form_submit_button('Cadastrar'):
        db.executar(f"INSERT INTO itens (name, cost, value, quantity, bar_code) VALUES ('{name}', {cost}, {value}, {quantity}, {bar_code});")