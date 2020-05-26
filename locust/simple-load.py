from locust import HttpUser, TaskSet, task, between

class UserBehaviour(TaskSet):
    @task(2)
    def index(self):
        self.client.get('/')

    @task(1)
    def profile(self):
        self.client.get('/')

class WebsiteUser(HttpUser):
    task_set = UserBehaviour
    wait_time = between(2, 5)