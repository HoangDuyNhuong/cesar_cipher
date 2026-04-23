# frontend.py

import streamlit as st
from backend import cesar_cipher, cesar_uncipher

# Configuration de la page
st.set_page_config(
    page_title="Chiffrement de César",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Grand intello Hakim")
st.write("Une application simple pour chiffrer et déchiffrer des messages.")

# Choix de l'action
action = st.radio(
    "Choisissez une action :",
    ("Chiffrer", "Déchiffrer")
)

# Entrée utilisateur
message = st.text_area("Entrez votre message :")

key = st.number_input(
    "Clé de chiffrement :",
    value=3,
    step=1
)

# Bouton d'exécution
if st.button("Exécuter"):
    if message.strip() == "":
        st.warning("Veuillez entrer un message.")
    else:
        if action == "Chiffrer":
            result = cesar_cipher(message, key)
            st.success("Message chiffré :")
            st.code(result)
        else:
            result = cesar_uncipher(message, key)
            st.success("Message déchiffré :")
            st.code(result)

# Footer
st.markdown("---")
st.caption("Projet Streamlit - Chiffrement de César")