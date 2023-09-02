import streamlit as st
import requests

response = requests.get("https://tester-api.streamlit.app/")
data = response.json()

st.write("Réponse de l'API FastAPI :")
st.write(data)
