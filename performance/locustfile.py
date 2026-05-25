from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_albums(self):
        self.client.get("/albums")

    @task
    def get_comments(self):
        self.client.get("/comments")

    @task
    def get_photos(self):
        self.client.get("/photos")

    @task
    def get_todos(self):
        self.client.get("/todos")
