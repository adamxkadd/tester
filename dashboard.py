import streamlit as st
import requests

st.title("Hello World with FastAPI and Streamlit")

try:
    # Faites une requête à votre API FastAPI
    response = requests.get("https://tester-api.streamlit.app/")
    response.raise_for_status()  # Vérifiez si la réponse est valide
    data = response.json()
    st.write("Réponse de l'API FastAPI :")
    st.write(data)
except requests.exceptions.RequestException as e:
    st.error(f"Une erreur s'est produite : {e}")
