# dashboard.py
import streamlit as st
import requests

API_URL = "https://scoe-banque.streamlit.app"  # Mettez l'URL de votre API FastAPI ici

st.title("Tableau de bord Streamlit")

# Créez un formulaire pour saisir des données
st.header("Saisissez des données:")
user_input = st.text_input("Entrez des données:", "Exemple de données")

if st.button("Prédire"):
    data = {"input_data": user_input} 
    response = requests.post(f"{API_URL}/predict/", json=data)
    st.write("Réponse : ") 
    st.write(response)
    st.write("Code de réponse HTTP : ", response.status_code)
    
    # Vérifiez si la réponse a un code de statut 200 (OK)
    if response.status_code == 200:
        try:
            result = response.json()
            st.write("Contenu de la réponse JSON :")
            st.write(result)
        except json.decoder.JSONDecodeError as e:
            st.error("Erreur lors de l'analyse de la réponse JSON.")
    else:
        st.error("Une erreur s'est produite lors de la prédiction. Code de statut HTTP : ", response.status_code)


# # Bouton pour envoyer les données à l'API
# if st.button("Prédire"):
#     data = {"input_data": user_input} 
#     response = requests.post(f"{API_URL}/predict/", json=data)
#     st.write("reponse : ") 
#     st.write(response)
#     st.write(response.status_code)
#     st.write("réponse JSON :")
#     st.write(response.json())

#     if response.status_code == 200:
#         result = response.json()
#         st.success(result["result"])
#     else:
#         st.error("Une erreur s'est produite lors de la prédiction.")
