import streamlit as st
import requests

API_URL = "http://localhost:8000/doctor"

def main():
    st.title("👨‍⚕️ Doctor Dashboard")
    st.write("Fill out patient condition details to generate possible medications and precautions.")

    with st.form("doctor_form"):
        condition = st.text_area("Enter Patient Condition")
        precautions = st.text_area("Enter Necessary Precautions")
        submit = st.form_submit_button("Generate Medication Plan")

    if submit and condition:
        response = requests.post(API_URL, json={"condition": condition, "precautions": precautions})
        if response.status_code == 200:
            st.success("Medication Plan Generated")
            st.json(response.json())
        else:
            st.error("Error generating medication plan")

if __name__ == "__main__":
    main()
