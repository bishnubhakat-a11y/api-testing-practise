"""
Todos Test Suite
This file contains Exhaustive Tests (Positive, Negative, Edge, Boundary) for the Todos endpoints.
It uses the `pytest` framework and `allure` for generating beautiful HTML reports.
"""
import allure
import pytest
from src.utils.assertions import assert_status_code, assert_response_time, assert_not_empty, assert_key_exists
from data.payloads.todos_payload import get_new_todo_payload, get_update_todo_payload

@allure.feature("Todos API - Exhaustive Testing")
@pytest.mark.regression
class TestTodosExhaustive:

    # ==========================================
    # POSITIVE TESTS (The "Happy Path")
    # ==========================================
    @allure.story("Positive: Get all todos")
    @pytest.mark.smoke
    def test_get_todos_positive(self, todos_service):
        """Verify that fetching all todos returns a 200 OK status code."""
        # Act: Call the API
        response = todos_service.get_todos()
        # Assert: Check the status code
        assert_status_code(response, 200)
        assert_response_time(response, 1500)
        assert_not_empty(response.json())

    @allure.story("Positive: Get todo by valid ID")
    def test_get_todo_by_id_positive(self, todos_service):
        """Verify that fetching a specific todo by ID works successfully."""
        response = todos_service.get_todo_by_id(1)
        assert_status_code(response, 200)
        assert_response_time(response, 1500)
        assert_key_exists(response.json(), 'id')

    @allure.story("Positive: Create a new todo")
    @pytest.mark.smoke
    def test_create_todo_positive(self, todos_service):
        """Verify that we can successfully create a new todo."""
        # Arrange: Generate a valid mock payload
        payload = get_new_todo_payload()
        # Act: Send the POST request
        response = todos_service.create_todo(payload)
        # Assert: Expect a 201 Created status
        assert_status_code(response, 201)
        assert_response_time(response, 1500)
        assert_key_exists(response.json(), 'id')

    @allure.story("Positive: Update an existing todo")
    def test_update_todo_positive(self, todos_service):
        """Verify that we can successfully update an existing todo."""
        payload = get_update_todo_payload()
        response = todos_service.update_todo(1, payload)
        assert_status_code(response, 200)

    @allure.story("Positive: Delete an existing todo")
    def test_delete_todo_positive(self, todos_service):
        """Verify that we can successfully delete a todo."""
        response = todos_service.delete_todo(1)
        assert_status_code(response, 200)

    # ==========================================
    # NEGATIVE TESTS (Testing invalid data)
    # ==========================================
    @allure.story("Negative: Get todo by non-existent ID")
    def test_get_todo_not_found(self, todos_service):
        """Verify that requesting an ID that does not exist returns a 404 Not Found error."""
        response = todos_service.get_todo_by_id(999999)
        assert_status_code(response, 404)

    @allure.story("Negative: Create todo with invalid data types")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_todo_invalid_types(self, todos_service):
        """
        Verify that the API rejects invalid data types (e.g., sending an integer instead of a string).
        We use xfail here because our mock dummy API accepts bad data anyway.
        """
        payload = get_new_todo_payload()
        # Intentionally corrupt the payload data
        payload["userId" if "userId" in payload else "title"] = 123456
        response = todos_service.create_todo(payload)
        # Expect a 400 Bad Request
        assert_status_code(response, 400)

    # ==========================================
    # EDGE & BOUNDARY TESTS (Testing limits)
    # ==========================================
    @allure.story("Edge: Create todo with empty payload")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_todo_empty_payload(self, todos_service):
        """
        Verify the API behaves gracefully when given absolutely no data.
        It should safely reject the request with a 400 Bad Request instead of crashing (500 Error).
        """
        response = todos_service.create_todo({})
        assert_status_code(response, 400)

    @allure.story("Boundary: todo ID at lower bound")
    def test_get_todo_id_zero(self, todos_service):
        """
        Verify that ID `0` (the lower boundary before valid IDs start) is correctly rejected as Not Found.
        """
        response = todos_service.get_todo_by_id(0)
        assert_status_code(response, 404)
