"""
Todos Service Module
This class acts as a "Facade" or wrapper for the Todos API endpoints.
Instead of writing raw HTTP calls in our test files, our test files will call these simple python methods.
"""
from src.api.api_client import APIClient
from src.api.routes import Routes

class TodosService:
    def __init__(self):
        # Instantiate the core API client
        self.client = APIClient()
        
    def get_todos(self):
        """Fetches all todos from the API."""
        return self.client.get(Routes.TODOS)
        
    def get_todo_by_id(self, item_id):
        """Fetches a specific todo by its unique ID."""
        return self.client.get(f"{Routes.TODOS}/{item_id}")
        
    def create_todo(self, payload):
        """Sends a POST request to create a new todo using the provided JSON payload."""
        return self.client.post(Routes.TODOS, json=payload)
        
    def update_todo(self, item_id, payload):
        """Sends a PUT request to update an existing todo."""
        return self.client.put(f"{Routes.TODOS}/{item_id}", json=payload)
        
    def delete_todo(self, item_id):
        """Sends a DELETE request to remove the specified todo."""
        return self.client.delete(f"{Routes.TODOS}/{item_id}")
