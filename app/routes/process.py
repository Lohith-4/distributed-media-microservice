from fastapi import APIRouter, HTTPException
from app.services.cache_service import set_job_status, get_job_status
from app.services.image_service import resize_image, crop_image, compress_image, get_image_info
from app.tasks import process_media_task
import uuid

router = APIRouter()

@router.post("/process/{filename}")
async def process_image(filename: str, width: int = 800, height: int = 600):
    job_id = str(uuid.uuid4())
    set_job_status(job_id, "pending", {"filename": filename})
    process_media_task.delay(job_id, filename, width, height)
    return {
        "message": "Processing started",
        "job_id": job_id,
        "status": "pending"
    }

@router.post("/resize/{filename}")
async def resize(filename: str, width: int = 800, height: int = 600):
    try:
        output = resize_image(filename, width, height)
        return {"message": "Image resized", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/crop/{filename}")
async def crop(filename: str, left: int = 0, top: int = 0, right: int = 100, bottom: int = 100):
    try:
        output = crop_image(filename, left, top, right, bottom)
        return {"message": "Image cropped", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/compress/{filename}")
async def compress(filename: str, quality: int = 85):
    try:
        output = compress_image(filename, quality)
        return {"message": "Image compressed", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/info/{filename}")
async def image_info(filename: str):
    try:
        info = get_image_info(filename)
        return info
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/process/status/{job_id}")
async def get_process_status(job_id: str):
    job = get_job_status(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job