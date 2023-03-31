import requests
import streamlit as st

API_URL = "https://basic-demo76.herokuapp.com/"

response = requests.get(API_URL)
data = response.json()

st.write(data)