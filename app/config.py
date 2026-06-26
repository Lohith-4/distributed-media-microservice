import os
from dotenv import load_dotenv

load_dotenv()

MEDIA_DIR = os.getenv("MEDIA_DIR", "media")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 10485760))  # 10MB default
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "mp4", "avi", "mov"}
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 8000))