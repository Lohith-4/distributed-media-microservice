from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.services.media_service import get_file_path

router = APIRouter()

@router.get("/stream/{filename}")
async def stream_file(filename: str):
    try:
        file_path = get_file_path(filename)
        return FileResponse(path=file_path, filename=filename)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))