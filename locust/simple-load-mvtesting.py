import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def website_home(self):
        self.client.get("/")

    @task
    def website_components(self):
        self.client.get("/features/components")
    
    @task
    def website_partialdesigns(self):
        self.client.get("/features/partial-designs")
        # remove cookies to make sure next user won't share them
        
        self.client.cookies.clear()