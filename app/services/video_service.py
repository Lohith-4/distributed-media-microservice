import ffmpeg
import os
from pathlib import Path
from app.config import MEDIA_DIR

def get_video_info(filename: str) -> dict:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    probe = ffmpeg.probe(str(file_path))
    video_stream = next(
        (s for s in probe["streams"] if s["codec_type"] == "video"), None
    )
    return {
        "filename": filename,
        "duration": probe["format"].get("duration"),
        "size_bytes": probe["format"].get("size"),
        "width": video_stream.get("width") if video_stream else None,
        "height": video_stream.get("height") if video_stream else None,
        "codec": video_stream.get("codec_name") if video_stream else None,
    }

def extract_thumbnail(filename: str, time: int = 1) -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    output_filename = f"thumb_{Path(filename).stem}.jpg"
    output_path = Path(MEDIA_DIR) / output_filename
    (
        ffmpeg
        .input(str(file_path), ss=time)
        .output(str(output_path), vframes=1)
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )
    return str(output_path)

def transcode_video(filename: str, format: str = "mp4") -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    output_filename = f"transcoded_{Path(filename).stem}.{format}"
    output_path = Path(MEDIA_DIR) / output_filename
    (
        ffmpeg
        .input(str(file_path))
        .output(str(output_path), vcodec="libx264", acodec="aac")
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )
    return str(output_path)

def compress_video(filename: str, crf: int = 28) -> str:
    file_path = Path(MEDIA_DIR) / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found")
    output_filename = f"compressed_{filename}"
    output_path = Path(MEDIA_DIR) / output_filename
    (
        ffmpeg
        .input(str(file_path))
        .output(str(output_path), vcodec="libx264", crf=crf)
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )
    return str(output_path)