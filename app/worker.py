from celery import Celery

celery_app = Celery(
    "media_worker",
    broker="amqp://guest:guest@172.26.29.124:5672//",
    backend="redis://172.26.29.124:6379/0",
    include=["app.tasks"]
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_always_eager=False,
)