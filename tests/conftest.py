import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.users_service import UsersService
from src.services.posts_service import PostsService
from src.services.todos_service import TodosService
from src.services.comments_service import CommentsService
from src.services.albums_service import AlbumsService
from src.services.photos_service import PhotosService

@pytest.fixture(scope="session")
def users_service():
    return UsersService()

@pytest.fixture(scope="session")
def posts_service():
    return PostsService()

@pytest.fixture(scope="session")
def todos_service():
    return TodosService()

@pytest.fixture(scope="session")
def comments_service():
    return CommentsService()

@pytest.fixture(scope="session")
def albums_service():
    return AlbumsService()

@pytest.fixture(scope="session")
def photos_service():
    return PhotosService()
