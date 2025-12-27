import streamlit as st
from services.api import get

st.title("Sort Patients")

sort_by = st.selectbox("Sort by", ["height", "weight", "bmi"])
order = st.radio("Order", ["asc", "desc"])

if st.button("Sort"):
    data = get("/sort/", params={"sort_by": sort_by, "order": order})
    st.json(data)
