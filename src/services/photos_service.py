"""
Photos Service Module
This class acts as a "Facade" or wrapper for the Photos API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class PhotosService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_photos(self):
        """Fetches all photos from the API."""
        return self.client.get(Routes.PHOTOS)
        
    def get_photo_by_id(self, item_id):
        """Fetches a specific photo by its unique ID."""
        return self.client.get(f"{Routes.PHOTOS}/{item_id}")
        
    def create_photo(self, payload):
        """Sends a POST request to create a new photo using the provided JSON payload."""
        return self.client.post(Routes.PHOTOS, json=payload)
        
    def update_photo(self, item_id, payload):
        """Sends a PUT request to update an existing photo."""
        return self.client.put(f"{Routes.PHOTOS}/{item_id}", json=payload)
        
    def delete_photo(self, item_id):
        """Sends a DELETE request to remove the specified photo."""
        return self.client.delete(f"{Routes.PHOTOS}/{item_id}")

