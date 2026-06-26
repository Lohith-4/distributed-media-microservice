from PIL import Image, ImageFilter
from pathlib import Path
from app.config import MEDIA_DIR
import os

def resize_image(filename: str, width: int, height: int) -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    img = Image.open(file_path)
    img = img.resize((width, height))
    output_path = Path(MEDIA_DIR) / f"resized_{filename}"
    img.save(output_path)
    return str(output_path)

def crop_image(filename: str, left: int, top: int, right: int, bottom: int) -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    img = Image.open(file_path)
    img = img.crop((left, top, right, bottom))
    output_path = Path(MEDIA_DIR) / f"cropped_{filename}"
    img.save(output_path)
    return str(output_path)

def compress_image(filename: str, quality: int = 85) -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    img = Image.open(file_path)
    output_path = Path(MEDIA_DIR) / f"compressed_{filename}"
    img.save(output_path, optimize=True, quality=quality)
    return str(output_path)

def get_image_info(filename: str) -> dict:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    img = Image.open(file_path)
    size = os.path.getsize(file_path)
    return {
        "filename": filename,
        "format": img.format,
        "mode": img.mode,
        "width": img.width,
        "height": img.height,
        "size_bytes": size,
        "size_kb": round(size / 1024, 2)
    }