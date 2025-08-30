import streamlit as st
import requests

st.title("👨‍⚕️ Doctor Dashboard")

st.subheader("Add Patient Condition & Precautions")

# Input fields
condition = st.text_area("Enter Patient Condition")
precautions = st.text_area("Enter Precautions")

if st.button("Submit"):
    if condition.strip() and precautions.strip():
        # Send to backend
        response = requests.post(
            "http://localhost:8000/doctor/add_condition",
            json={"condition": condition, "precautions": precautions}
        )
        if response.status_code == 200:
            result = response.json()
            st.success(result["message"])
            st.write("### Condition:")
            st.info(result["condition"])
            st.write("### Precautions:")
            st.warning(result["precautions"])
        else:
            st.error("❌ Failed to upload. Try again.")
    else:
        st.error("⚠️ Please enter both condition and precautions.")
