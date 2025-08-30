import streamlit as st
import requests

API_URL = "http://localhost:8000/pharmacist"

def main():
    st.title("💊 Pharmacist Dashboard")
    st.write("Check prescribed medications and suggest alternatives if not available.")

    with st.form("pharmacist_form"):
        condition = st.text_area("Enter Patient Condition or Prescription")
        submit = st.form_submit_button("Get Alternatives")

    if submit and condition:
        response = requests.post(API_URL, json={"condition": condition})
        if response.status_code == 200:
            st.success("Pharmacist Recommendations")
            st.json(response.json())
        else:
            st.error("Error fetching pharmacist recommendations")

if __name__ == "__main__":
    main()
