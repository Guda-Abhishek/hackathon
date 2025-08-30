# frontend/pages/pharmacist.py
import streamlit as st
import requests

st.set_page_config(page_title="Pharmacist Dashboard", layout="wide")

st.title("💊 Pharmacist Dashboard")
st.write("Enter a prescribed medicine and check for alternatives.")

medicine_text = st.text_area("Enter Medicine Name", placeholder="e.g., Paracetamol, AlegraM")

if st.button("Check Substitute"):
    if medicine_text.strip():
        response = requests.post("http://localhost:8000/analyse", json={"text": medicine_text})
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Successfully Processed")
            if "substitute" in result:
                st.write(f"**Medicine Given:** {result['medicine_given']}")
                st.write(f"**Suggested Substitute:** {result['substitute']}")
                st.info(result.get("note", ""))
            else:
                st.write("No substitute found. Full response:")
                st.json(result)
        else:
            st.error("❌ Error in response from backend")
    else:
        st.warning("Please enter a medicine name.")
