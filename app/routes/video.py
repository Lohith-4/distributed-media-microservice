from fastapi import APIRouter, HTTPException
from app.services.video_service import get_video_info, extract_thumbnail, transcode_video, compress_video

router = APIRouter()

@router.get("/video/info/{filename}")
async def video_info(filename: str):
    try:
        return get_video_info(filename)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/video/thumbnail/{filename}")
async def thumbnail(filename: str, time: int = 1):
    try:
        output = extract_thumbnail(filename, time)
        return {"message": "Thumbnail extracted", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/video/transcode/{filename}")
async def transcode(filename: str, format: str = "mp4"):
    try:
        output = transcode_video(filename, format)
        return {"message": "Video transcoded", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/video/compress/{filename}")
async def compress(filename: str, crf: int = 28):
    try:
        output = compress_video(filename, crf)
        return {"message": "Video compressed", "output": output}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))