"""
Users Service Module
This class acts as a "Facade" or wrapper for the Users API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class UsersService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_users(self):
        """Fetches all users from the API."""
        return self.client.get(Routes.USERS)
        
    def get_user_by_id(self, item_id):
        """Fetches a specific user by its unique ID."""
        return self.client.get(f"{Routes.USERS}/{item_id}")
        
    def create_user(self, payload):
        """Sends a POST request to create a new user using the provided JSON payload."""
        return self.client.post(Routes.USERS, json=payload)
        
    def update_user(self, item_id, payload):
        """Sends a PUT request to update an existing user."""
        return self.client.put(f"{Routes.USERS}/{item_id}", json=payload)
        
    def delete_user(self, item_id):
        """Sends a DELETE request to remove the specified user."""
        return self.client.delete(f"{Routes.USERS}/{item_id}")

    def get_user_albums(self, user_id):
        return self.client.get(f"{Routes.USERS}/{user_id}/albums")
        
    def get_user_todos(self, user_id):
        return self.client.get(f"{Routes.USERS}/{user_id}/todos")
        
    def get_user_posts(self, user_id):
        return self.client.get(f"{Routes.USERS}/{user_id}/posts")

