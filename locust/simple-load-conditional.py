import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    # this task will run 4 times often than the next one
    @task(8)
    def variant_a(self):
        VARIANT_A_TEXT_MARKER = "VariantA"
        r = self.client.get("/")
        if (VARIANT_A_TEXT_MARKER in r.text):
            self.client.get("/en/Data/News/NewsA", verify=False)
            self.client.get("/en/goalitemInstance", verify=False)
            self.client.get("/en/goalitemBrochure", verify=False)
        #else:
        #    self.client.get("/en/Data/News/NewsB", verify=False)
        self.client.cookies.clear()

    @task(2)
    def variant_b(self):
        VARIANT_A_TEXT_MARKER = "VariantB"
        r = self.client.get("/")
        if (VARIANT_A_TEXT_MARKER in r.text):
            self.client.get("/en/Data/News/NewsB", verify=False)
        self.client.cookies.clear()
