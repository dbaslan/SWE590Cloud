from locust import HttpUser, task

URL = "http://34.118.124.205/"

class WebUser(HttpUser):
    @task
    def load_page(self):
        self.client.get(URL)