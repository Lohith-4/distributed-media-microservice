import redis
import json

redis_client = redis.Redis(host="172.26.29.124", port=6379, db=0)
def set_job_status(job_id: str, status: str, extra: dict = {}):
    data = {
        "status": status,
        "job_id": job_id,
        **extra
    }
    redis_client.setex(job_id, 3600, json.dumps(data))  # Expires in 1 hour
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