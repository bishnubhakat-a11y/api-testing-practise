"""
Comments Service Module
This class acts as a "Facade" or wrapper for the Comments API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class CommentsService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_comments(self):
        """Fetches all comments from the API."""
        return self.client.get(Routes.COMMENTS)
        
    def get_comment_by_id(self, item_id):
        """Fetches a specific comment by its unique ID."""
        return self.client.get(f"{Routes.COMMENTS}/{item_id}")
        
    def create_comment(self, payload):
        """Sends a POST request to create a new comment using the provided JSON payload."""
        return self.client.post(Routes.COMMENTS, json=payload)
        
    def update_comment(self, item_id, payload):
        """Sends a PUT request to update an existing comment."""
        return self.client.put(f"{Routes.COMMENTS}/{item_id}", json=payload)
        
    def delete_comment(self, item_id):
        """Sends a DELETE request to remove the specified comment."""
        return self.client.delete(f"{Routes.COMMENTS}/{item_id}")

