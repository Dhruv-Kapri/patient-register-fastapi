import streamlit as st
from services.api import get, put


st.title("View / Edit Patient")

patient_id = st.text_input("Patient ID", value="P001")

if st.button("Fetch Patient"):
    data = get(f"/patient/{patient_id}")
    st.session_state["patient_data"] = data

if "patient_data" in st.session_state:
    st.subheader("Current Data")
    st.json(st.session_state["patient_data"])

    st.subheader("Update Fields (leave blank to keep unchanged)")
    with st.form("update_patient"):
        name = st.text_input("Name")
        city = st.text_input("City")
        age = st.text_input("Age")
        gender = st.selectbox(
            "Gender", ["", "male", "female", "do not say"])
        height = st.text_input("Height")
        weight = st.text_input("Weight")

        submitted = st.form_submit_button("Update")

        if submitted:
            payload = {}
            if name:
                payload["name"] = name
            if city:
                payload["city"] = city
            if age:
                payload["age"] = int(age)
            if gender:
                payload["gender"] = gender
            if height:
                payload["height"] = float(height)
            if weight:
                payload["weight"] = float(weight)

            res = put(f"/edit/{patient_id}", payload)
            st.success("Patient updated")
            st.json(res)
