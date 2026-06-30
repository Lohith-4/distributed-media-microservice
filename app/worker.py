from celery import Celery
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@172.26.29.124:5672//")
REDIS_URL = os.getenv("REDIS_URL", "redis://172.26.29.124:6379/0")

celery_app = Celery(
    "media_worker",
    broker=RABBITMQ_URL,
    backend=REDIS_URL,
    include=["app.tasks"]
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_always_eager=False,
)