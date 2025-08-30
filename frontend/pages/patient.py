import streamlit as st
import requests
import os

BACKEND_URL = "http://localhost:8000"  # adjust if deployed

st.title("🧑‍⚕️ Patient Dashboard")

st.write("Upload your medical condition or enter details manually to get medication suggestions.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload your medical report (PDF/TXT)", type=["pdf", "txt"])

condition_text = st.text_area("Or enter your condition here", "")

if st.button("Get Medication"):
    if uploaded_file:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{BACKEND_URL}/patient/upload", files=files)
    elif condition_text:
        response = requests.post(f"{BACKEND_URL}/patient/condition", json={"condition": condition_text})
    else:
        st.warning("Please provide either a condition or upload a file.")
        response = None

    if response and response.status_code == 200:
        data = response.json()
        st.subheader("💊 Suggested Medication")
        st.write(data.get("medication"))

        st.subheader("🔄 Alternative (if medicine not available)")
        st.write(data.get("alternative"))

        # Option to view drug names
        if st.checkbox("Show prescription and alternative drug names"):
            st.subheader("📌 Prescription Drugs")
            st.write(data.get("prescription_drugs"))
            st.subheader("📌 Alternative Drugs")
            st.write(data.get("alternative_drugs"))
    else:
        if response:
            st.error(f"Error: {response.text}")
