import streamlit as st
from services.api import get

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Patient Registry",
    layout="wide"
)

# ---------------- HOME ----------------
st.title("Patient Registry")
st.caption("FastAPI + Streamlit")

st.subheader("Backend status")

col1, col2 = st.columns(2)

with col1:
    st.write("**GET /**")
    st.json(get("/"))

with col2:
    st.write("**GET /about/**")
    st.json(get("/about/"))
