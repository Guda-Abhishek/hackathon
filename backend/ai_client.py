# backend/ai_client.py
import random

def analyze_text(text: str):
    """
    Analyzes patient condition text and returns:
    - Possible medication suggestions
    - Necessary precautions
    - Alternatives if medications not available
    """
    if not text or text.strip() == "":
        return {"error": "No condition provided"}

    # Mock logic (replace later with IBM Watson / HuggingFace integration)
    conditions = {
        "fever": {
            "medications": ["Paracetamol 500mg", "Ibuprofen"],
            "precautions": ["Stay hydrated", "Take rest", "Monitor temperature"],
            "alternatives": ["Acetaminophen", "Aspirin (not for children)"]
        },
        "cold": {
            "medications": ["Cetirizine", "Antihistamines"],
            "precautions": ["Drink warm fluids", "Avoid cold drinks"],
            "alternatives": ["Loratadine", "Fexofenadine"]
        },
        "headache": {
            "medications": ["Paracetamol", "Ibuprofen"],
            "precautions": ["Rest in dark room", "Avoid loud noise"],
            "alternatives": ["Naproxen", "Aspirin"]
        }
    }

    # Pick based on keywords
    selected = None
    for key, val in conditions.items():
        if key in text.lower():
            selected = val
            break

    if not selected:
        # Generic fallback
        selected = {
            "medications": ["Consult a physician"],
            "precautions": ["Maintain healthy lifestyle"],
            "alternatives": ["None available"]
        }

    return {
        "condition": text,
        "medications": selected["medications"],
        "precautions": selected["precautions"],
        "alternatives": selected["alternatives"]
    }