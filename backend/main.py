from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from backend.file_handler import save_upload_file
from backend.ai_client import analyse_text
from pydantic import BaseModel
app = FastAPI()

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Medication Backend is running"}

# --------------------- Patient ---------------------
@app.post("/patient/upload")
async def patient_upload(file: UploadFile = File(...)):
    file_path = save_upload_file(file)
    return {"message": "File uploaded successfully", "file_path": file_path}

@app.post("/patient/analyze")
async def patient_text_analysis(text: str = Form(...)):
    result = analyse_text(text)
    return {"analysis": result}

# ---------------- Doctor Routes ----------------
class DoctorInput(BaseModel):
    condition: str
    precautions: str

@app.post("/doctor/add_condition")
async def add_condition(data: DoctorInput):
    return {
        "message": "Successfully uploaded",
        "condition": data.condition,
        "precautions": data.precautions
    }
# ---------------- Pharmacist Routes ----------------
@app.post("/pharmacist")
async def pharmacist_submit(
    prescription: str = Form(...),
    alternative: str = Form(...)
):
    response = {
        "prescription": prescription,
        "alternative": alternative,
        "status": "Pharmacist entry submitted successfully"
    }
    return response