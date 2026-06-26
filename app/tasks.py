from app.worker import celery_app
from app.services.cache_service import set_job_status
from PIL import Image
from pathlib import Path
import time

@celery_app.task(bind=True)
def process_media_task(self, job_id: str, filename: str, width: int, height: int):
    try:
        set_job_status(job_id, "processing", {"filename": filename})
        time.sleep(1)  # Simulate processing time
        file_path = Path("media") / filename
        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found")
        img = Image.open(file_path)
        img = img.resize((width, height))
        output_path = Path("media") / f"processed_{filename}"
        img.save(output_path)
        set_job_status(job_id, "completed", {
            "filename": filename,
            "output": f"processed_{filename}"
        })
        return {"status": "completed", "output": f"processed_{filename}"}
    except Exception as e:
        set_job_status(job_id, "failed", {"error": str(e)})
        raise self.retry(exc=e, countdown=5, max_retries=3)