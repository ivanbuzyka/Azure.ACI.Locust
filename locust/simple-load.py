from locust import HttpLocust, TaskSet, task, between

class UserBehaviour(TaskSet):
    @task(2)
    def index(self):
        self.client.get('/')

    @task(1)
    def profile(self):
        self.client.get('/')

class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(2, 5)