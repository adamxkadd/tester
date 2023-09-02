import streamlit as st
import requests
import json

url = "https://tester-api.streamlit.app/hello"
data = json.dumps({"msg": "c moi"})
headers = {'Content-Type': 'application/json'}
response = requests.post(url=url, data=data, headers=headers)
st.write("affiche data")
st.write(data.text)
st.write("affiche reponse")
st.write(response.text)
