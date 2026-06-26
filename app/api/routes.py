from fastapi import APIRouter
from app.routes import upload, stream, process
from app.routes import video

router = APIRouter()

router.include_router(upload.router, prefix="/media", tags=["Upload"])
router.include_router(stream.router, prefix="/media", tags=["Stream"])
router.include_router(process.router, prefix="/media", tags=["Process"])
router.include_router(video.router, prefix="/media", tags=["Video"])