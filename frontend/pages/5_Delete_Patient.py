import streamlit as st
from services.api import delete

st.title("Delete Patient")

patient_id = st.text_input("Patient ID to delete")

if st.button("Delete"):
    res = delete(f"/delete/{patient_id}")
    st.warning("Patient deleted")
    st.json(res)
