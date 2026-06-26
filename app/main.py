from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Distributed Media Microservice",
    description="Upload, process and stream media files",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Media Microservice is running!"}    