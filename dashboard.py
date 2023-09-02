import streamlit as st
import requests
import json

# st.title("Hello World with FastAPI and Streamlit")
# Faites une requête à votre API FastAPI
# response = requests.get("https://tester-api.streamlit.app/hello/")
response = requests.post(url = "https://tester-api.streamlit.app/hello/", data = json.dumps({"msg":'c moi'}))
response.text
# response.raise_for_status()  # Vérifiez si la réponse est valide
# data = response.json()
# st.write("Réponse de l'API FastAPI :")
# st.write(data)

