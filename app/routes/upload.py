from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.media_service import save_file, list_files, delete_file
from app.services.cache_service import set_job_status, get_job_status, list_all_jobs
import uuid

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    try:
        set_job_status(job_id, "processing")
        path = save_file(file.file, file.filename)
        set_job_status(job_id, "completed", {"filename": file.filename, "path": path})
        return {
            "message": "File uploaded successfully",
            "job_id": job_id,
            "path": path
        }
    except ValueError as e:
        set_job_status(job_id, "failed", {"error": str(e)})
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/files/")
async def get_files():
    files = list_files()
    return {"files": files}

@router.get("/jobs/")
async def get_all_jobs():
    return list_all_jobs()

@router.get("/jobs/{job_id}")
async def get_job(job_id: str):
    job = get_job_status(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.delete("/files/{filename}")
async def remove_file(filename: str):
    try:
        delete_file(filename)
        return {"message": f"{filename} deleted successfully"}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))