from locust import HttpUser, task, between

class MediaServiceUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def get_root(self):
        self.client.get("/")

    @task(2)
    def list_files(self):
        self.client.get("/media/files/")

    @task(1)
    def get_metrics(self):
        self.client.get("/metrics")