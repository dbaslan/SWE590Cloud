from locust import HttpUser, task, between, HttpLocust, TaskSet
import json

URL = "http://34.118.124.205/"

class WebsiteTasks(TaskSet):
    
    @task
    def index(self):
        self.client.get(URL)

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 10
    max_wait = 100