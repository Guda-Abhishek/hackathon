# backend/filehandler.py
import os
from fastapi import UploadFile

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file: UploadFile) -> str:
    """
    Saves uploaded file into backend/uploads folder
    Returns file path
    """
    if not file.filename:  # Ensure filename is not None
        raise ValueError("Uploaded file must have a valid filename")

    file_location = os.path.join(UPLOAD_DIR, str(file.filename))

    try:
        with open(file_location, "wb+") as f:
            f.write(file.file.read())
        return file_location
    except Exception as e:
        raise Exception(f"File saving failed: {str(e)}")
