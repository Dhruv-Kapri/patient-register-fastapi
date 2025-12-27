import streamlit as st
from services.api import get

st.title("All Patients")
data = get("/view/")
st.json(data)
