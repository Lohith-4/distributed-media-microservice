import pytest
from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Media Microservice is running!"}

def test_upload_file():
    file_content = b"fake image content"
    response = client.post(
        "/media/upload/",
        files={"file": ("test.jpg", io.BytesIO(file_content), "image/jpeg")}
    )
    assert response.status_code == 200
    assert "job_id" in response.json()
    assert response.json()["message"] == "File uploaded successfully"

def test_list_files():
    response = client.get("/media/files/")
    assert response.status_code == 200
    assert "files" in response.json()

def test_stream_nonexistent_file():
    response = client.get("/media/stream/nonexistent.jpg")
    assert response.status_code == 404

def test_delete_nonexistent_file():
    response = client.delete("/media/files/nonexistent.jpg")
    assert response.status_code == 404

def test_image_info_nonexistent():
    response = client.get("/media/info/nonexistent.jpg")
    assert response.status_code == 404

def test_process_status_nonexistent():
    response = client.get("/media/process/status/fake-job-id")
    assert response.status_code == 404
    