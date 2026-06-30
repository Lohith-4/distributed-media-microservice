import redis
import json
import os

REDIS_HOST = os.getenv("REDIS_URL", "redis://172.26.29.124:6379/0")

redis_client = redis.from_url(REDIS_HOST)

def set_job_status(job_id: str, status: str, extra: dict = {}):
    data = {
        "status": status,
        "job_id": job_id,
        **extra
    }
    redis_client.set(job_id, json.dumps(data), ex=3600)
    return data

def get_job_status(job_id: str):
    data = redis_client.get(job_id)
    if not data:
        return None
    return json.loads(data)

def delete_job(job_id: str):
    redis_client.delete(job_id)
    return True

def list_all_jobs():
    keys = redis_client.keys("*")
    jobs = {}
    for key in keys:
        data = redis_client.get(key)
        if data:
            jobs[key.decode()] = json.loads(data)
    return jobs