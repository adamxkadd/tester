import streamlit as st
import requests
import json

# Utilisez le bon endpoint URL
url = "https://tester-api.streamlit.app/hello"

# Utilisez le bon format de données pour la requête
data = json.dumps({"msg": "c moi"})

# Spécifiez le type de contenu JSON dans l'en-tête
headers = {'Content-Type': 'application/json'}

response = requests.post(url=url, data=data, headers=headers)

# Affichez la réponse
st.write(response.text)
