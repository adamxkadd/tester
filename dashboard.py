import streamlit as st
import requests
import json

url = "https://tester-api.streamlit.app/hello"
data = json.dumps({"msg": "c moi"})
headers = {'Content-Type': 'application/json'}
response = requests.post(url=url, data=data, headers=headers)

# Affiche les données envoyées dans la requête
st.write("Contenu de data:")
st.write(data)

# Vérifie si la requête a réussi
if response.status_code == 200:
    st.write("Réponse de l'API:")
   # st.write(response.text)
    st.write(response.json())
else:
    st.write("La requête a échoué avec le code de statut:", response.status_code)

