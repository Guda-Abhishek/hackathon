# ibm_client.py (renamed purpose: Hugging Face Client, no IBM Watson)

from transformers import pipeline

# Load a Hugging Face generative model (GPT-like model for text generation)
generator = pipeline("text-generation", model="gpt2")

def analyze_medication_interaction(prompt: str) -> str:
    """
    Generate analysis about medication interactions using Hugging Face GPT model.
    """
    try:
        result = generator(prompt, max_length=200, num_return_sequences=1)
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error generating analysis: {str(e)}"
