# dashboard.py
import streamlit as st
import requests

API_URL = "https://scoe-banque.streamlit.app"  # Mettez l'URL de votre API FastAPI ici

st.title("Tableau de bord Streamlit")

# Créez un formulaire pour saisir des données
st.header("Saisissez des données:")
user_input = st.text_input("Entrez des données:", "Exemple de données")
    
# Bouton pour envoyer les données à l'API
if st.button("Prédire"):
    data = {"input_data": user_input} 
    response = requests.post(f"{API_URL}/predict/", json=data)
    st.write("reponse : ") 
    st.write(response)
    st.write(response.status_code)
    st.write("réponse JSON :")
    st.write(response.json())

#     if response.status_code == 200:
#         result = response.json()
#         st.success(result["result"])
#     else:
#         st.error("Une erreur s'est produite lors de la prédiction.")
