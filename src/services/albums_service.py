"""
Albums Service Module
This class acts as a "Facade" or wrapper for the Albums API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class AlbumsService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_albums(self):
        """Fetches all albums from the API."""
        return self.client.get(Routes.ALBUMS)
        
    def get_album_by_id(self, item_id):
        """Fetches a specific album by its unique ID."""
        return self.client.get(f"{Routes.ALBUMS}/{item_id}")
        
    def create_album(self, payload):
        """Sends a POST request to create a new album using the provided JSON payload."""
        return self.client.post(Routes.ALBUMS, json=payload)
        
    def update_album(self, item_id, payload):
        """Sends a PUT request to update an existing album."""
        return self.client.put(f"{Routes.ALBUMS}/{item_id}", json=payload)
        
    def delete_album(self, item_id):
        """Sends a DELETE request to remove the specified album."""
        return self.client.delete(f"{Routes.ALBUMS}/{item_id}")

    def get_album_photos(self, album_id):
        return self.client.get(f"{Routes.ALBUMS}/{album_id}/photos")

