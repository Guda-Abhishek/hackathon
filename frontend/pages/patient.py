import streamlit as st
import requests

st.title("Patient Dashboard")
st.write("Upload your condition file or type details below to get medication suggestions.")

# -------- File Upload --------
uploaded_file = st.file_uploader("Upload your prescription / condition file", type=["txt", "pdf", "docx"])
if uploaded_file is not None:
    st.success(f"Selected file: {uploaded_file.name}")

    if st.button("Upload File"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post("http://127.0.0.1:8000/patient/upload", files=files)
        if response.status_code == 200:
            st.success("File uploaded successfully!")
            st.json(response.json())
        else:
            st.error("Failed to upload file.")

# -------- Text Area Input --------
condition_text = st.text_area("Or type your condition / prescription here:")

if st.button("Analyze Text"):
    if condition_text.strip() != "":
        response = requests.post("http://127.0.0.1:8000/patient/analyze", data={"text": condition_text})
        if response.status_code == 200:
            st.success("Analysis Completed!")
            st.json(response.json())
        else:
            st.error("Failed to analyze text.")
