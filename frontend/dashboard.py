import streamlit as st

st.set_page_config(page_title="AI Medication System", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Doctor", "Patient", "Pharmacist"])

if page == "Home":
    st.switch_page("pages/Home.py")
elif page == "Doctor":
    st.switch_page("pages/Doctor.py")
elif page == "Patient":
    st.switch_page("pages/Patient.py")
elif page == "Pharmacist":
    st.switch_page("pages/Pharmacist.py")
