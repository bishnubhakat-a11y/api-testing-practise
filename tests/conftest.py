import pytest
import sys
import os

# Custom HTML Report Title
def pytest_html_report_title(report):
    report.title = "Enterprise API Automation Report"

# Custom HTML Report CSS/Styling
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(['<h2 style="color: #4CAF50;">API Test Execution Summary</h2>'])

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')
    cells.insert(1, '<th>Time (s)</th>')

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')
    cells.insert(1, f'<td>{getattr(report, "duration", "0.00"):.2f}</td>')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__) if item.function.__doc__ else "No description"

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
