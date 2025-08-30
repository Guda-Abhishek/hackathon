from pathlib import Path
import shutil
from fastapi import UploadFile

# Ensure uploads directory exists
UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_upload_file(upload_file: UploadFile) -> str:
    """
    Save an uploaded file to the uploads directory and return the file path.
    """
    # Ensure filename is never None
    filename = upload_file.filename or "uploaded_file"

    # Create full file path
    file_path = UPLOAD_DIR / filename

    # Save the uploaded file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return str(file_path)
