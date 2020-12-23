import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get("/")

        # Add parameter verify=False if you are using self-signed/invalid certificate 
        # self.client.get("/", verify=False)

        # You can also use hardcoded URL which may be important in scenarios when multisite app is load tested.
        # Second name parametert is important to collect statistic correctly
        # self.client.get("https://sitehostname/", name="https://sitehostname/", verify=False)

    @task
    def view_item(self):
        item_id = random.randint(1, 10000)
        self.client.get(f"/?id={item_id}", name="/?id=somerandomstring")