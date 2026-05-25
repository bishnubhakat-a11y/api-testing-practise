"""
Posts Service Module
This class acts as a "Facade" or wrapper for the Posts API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class PostsService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_posts(self):
        """Fetches all posts from the API."""
        return self.client.get(Routes.POSTS)
        
    def get_post_by_id(self, item_id):
        """Fetches a specific post by its unique ID."""
        return self.client.get(f"{Routes.POSTS}/{item_id}")
        
    def create_post(self, payload):
        """Sends a POST request to create a new post using the provided JSON payload."""
        return self.client.post(Routes.POSTS, json=payload)
        
    def update_post(self, item_id, payload):
        """Sends a PUT request to update an existing post."""
        return self.client.put(f"{Routes.POSTS}/{item_id}", json=payload)
        
    def delete_post(self, item_id):
        """Sends a DELETE request to remove the specified post."""
        return self.client.delete(f"{Routes.POSTS}/{item_id}")

    def get_post_comments(self, post_id):
        return self.client.get(f"{Routes.POSTS}/{post_id}/comments")

