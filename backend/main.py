# backend/main.py
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from ai_client import analyze_text
from file_handler import save_uploaded_file

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Medication Backend Running"}

@app.post("/analyze_text/")
def analyze_condition(condition: str = Form(...)):
    """
    Doctor/Patient condition analysis
    """
    result = analyze_text(condition)
    return result

@app.post("/upload_condition/")
def upload_condition(file: UploadFile):
    """
    Uploads a file containing patient condition
    """
    file_path = save_uploaded_file(file)
    return {"message": "File uploaded successfully", "file_path": file_path}
