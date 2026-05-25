"""
Routes Configuration Module
This file centrally manages all of our API endpoint paths.
If an endpoint URL changes in the future, we only have to update it here!
"""
from dataclasses import dataclass

@dataclass
class Routes:
    """
    Dataclass containing constants for all API routes.
    Example usage: Routes.USERS returns '/users'
    """
    USERS = "/users"
    POSTS = "/posts"
    COMMENTS = "/comments"
    ALBUMS = "/albums"
    PHOTOS = "/photos"
    TODOS = "/todos"
