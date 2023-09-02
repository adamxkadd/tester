import streamlit as st
import requests

st.title("Hello World with FastAPI and Streamlit")

# Faites une requête à votre API FastAPI
response = requests.get("https://votre-url-fastapi/")
data = response.json()

st.write("Réponse de l'API FastAPI :")
st.write(data)
