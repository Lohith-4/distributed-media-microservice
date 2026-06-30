from fastapi import FastAPI
from app.api.routes import router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Distributed Media Microservice",
    description="Upload, process and stream media files",
    version="1.0.0"
)

# Add Prometheus metrics
Instrumentator().instrument(app).expose(app)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Media Microservice is running!"}