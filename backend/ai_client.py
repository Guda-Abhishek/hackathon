# backend/ai_client.py

def analyse_text(text: str) -> dict:
    """
    Analyze the given text (prescription, patient condition, or pharmacist input)
    and return medications, alternatives, and prescriptions.
    """

    text_lower = text.lower().strip()

    # --- Patient condition-based logic ---
    if "cold" in text_lower:
        return {
            "patient_condition": "Cold",
            "recommended_medications": ["AlegraM"],
            "alternative_medications": ["Montelukast"],
            "prescription_steps": [
                "Take AlegraM once daily after meals",
                "Alternative: Montelukast at night if symptoms persist"
            ]
        }

    elif "fever" in text_lower:
        return {
            "patient_condition": "Fever",
            "recommended_medications": ["Paracetamol"],
            "alternative_medications": ["Dolo650"],
            "prescription_steps": [
                "Take Paracetamol every 6-8 hours as needed",
                "Alternative: Dolo650 after meals if fever is high"
            ]
        }

    # --- Pharmacist substitution-based logic ---
    elif "paracetamol" in text_lower:
        return {
            "medicine_given": "Paracetamol",
            "substitute": "Dolo650",
            "note": "Suggesting equivalent substitute medicine."
        }

    elif "alegram" in text_lower:
        return {
            "medicine_given": "AlegraM",
            "substitute": "Montelukast",
            "note": "Suggesting equivalent substitute medicine."
        }

    # --- Default fallback ---
    return {
        "patient_condition": text,
        "recommended_medications": ["Medicine A", "Medicine B"],
        "alternative_medications": ["Alt Medicine X", "Alt Medicine Y"],
        "prescription_steps": [
            "Take Medicine A twice a day after meals",
            "Take Medicine B once at night"
        ]
    }
