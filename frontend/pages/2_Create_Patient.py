import streamlit as st
from services.api import post

st.title("Create New Patient")

with st.form("create_patient"):
    pid = st.text_input("Patient ID (e.g. P001)")
    name = st.text_input("Name")
    city = st.text_input("City")
    age = st.number_input("Age", min_value=0, max_value=119)
    gender = st.selectbox("Gender", ["male", "female", "do not say"])
    height = st.number_input("Height (meters)", min_value=0.01)
    weight = st.number_input("Weight (kg)", min_value=0.01)

    submitted = st.form_submit_button("Create")

    if submitted:
        payload = {
            "id": pid,
            "name": name,
            "city": city,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
        }
        res = post("/create/", payload)
        st.success("Patient created successfully")
        st.json(res)
