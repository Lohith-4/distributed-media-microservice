import os
import shutil
from pathlib import Path
from app.config import MEDIA_DIR, ALLOWED_EXTENSIONS

def save_file(file, filename: str) -> str:
    os.makedirs(MEDIA_DIR, exist_ok=True)
    ext = filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"File type .{ext} not allowed")
    file_path = Path(MEDIA_DIR) / filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    return str(file_path)

def get_file_path(filename: str) -> Path:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    return file_path

def list_files() -> list:
    os.makedirs(MEDIA_DIR, exist_ok=True)
    return os.listdir(MEDIA_DIR)

def delete_file(filename: str) -> bool:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    os.remove(file_path)
    return True