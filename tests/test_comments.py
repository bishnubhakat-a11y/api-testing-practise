"""
Comments Test Suite
This file contains Exhaustive Tests (Positive, Negative, Edge, Boundary) for the Comments endpoints.
It uses the `pytest` framework and `allure` for generating beautiful HTML reports.
"""
import allure
import pytest
from src.utils.assertions import assert_status_code
from data.payloads.comments_payload import get_new_comment_payload, get_update_comment_payload

@allure.feature("Comments API - Exhaustive Testing")
class TestCommentsExhaustive:

    # ==========================================
    # POSITIVE TESTS (The "Happy Path")
    # ==========================================
    @allure.story("Positive: Get all comments")
    def test_get_comments_positive(self, comments_service):
        """Verify that fetching all comments returns a 200 OK status code."""
        # Act: Call the API
        response = comments_service.get_comments()
        # Assert: Check the status code
        assert_status_code(response, 200)

    @allure.story("Positive: Get comment by valid ID")
    def test_get_comment_by_id_positive(self, comments_service):
        """Verify that fetching a specific comment by ID works successfully."""
        response = comments_service.get_comment_by_id(1)
        assert_status_code(response, 200)

    @allure.story("Positive: Create a new comment")
    def test_create_comment_positive(self, comments_service):
        """Verify that we can successfully create a new comment."""
        # Arrange: Generate a valid mock payload
        payload = get_new_comment_payload()
        # Act: Send the POST request
        response = comments_service.create_comment(payload)
        # Assert: Expect a 201 Created status
        assert_status_code(response, 201)

    @allure.story("Positive: Update an existing comment")
    def test_update_comment_positive(self, comments_service):
        """Verify that we can successfully update an existing comment."""
        payload = get_update_comment_payload()
        response = comments_service.update_comment(1, payload)
        assert_status_code(response, 200)

    @allure.story("Positive: Delete an existing comment")
    def test_delete_comment_positive(self, comments_service):
        """Verify that we can successfully delete a comment."""
        response = comments_service.delete_comment(1)
        assert_status_code(response, 200)

    # ==========================================
    # NEGATIVE TESTS (Testing invalid data)
    # ==========================================
    @allure.story("Negative: Get comment by non-existent ID")
    def test_get_comment_not_found(self, comments_service):
        """Verify that requesting an ID that does not exist returns a 404 Not Found error."""
        response = comments_service.get_comment_by_id(999999)
        assert_status_code(response, 404)

    @allure.story("Negative: Create comment with invalid data types")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_comment_invalid_types(self, comments_service):
        """
        Verify that the API rejects invalid data types (e.g., sending an integer instead of a string).
        We use xfail here because our mock dummy API accepts bad data anyway.
        """
        payload = get_new_comment_payload()
        # Intentionally corrupt the payload data
        key = list(payload.keys())[0]
        payload[key] = 123456
        response = comments_service.create_comment(payload)
        # Expect a 400 Bad Request
        assert_status_code(response, 400)

    # ==========================================
    # EDGE & BOUNDARY TESTS (Testing limits)
    # ==========================================
    @allure.story("Edge: Create comment with empty payload")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_comment_empty_payload(self, comments_service):
        """
        Verify the API behaves gracefully when given absolutely no data.
        It should safely reject the request with a 400 Bad Request instead of crashing (500 Error).
        """
        response = comments_service.create_comment({})
        assert_status_code(response, 400)

    @allure.story("Boundary: comment ID at lower bound")
    def test_get_comment_id_zero(self, comments_service):
        """
        Verify that ID `0` (the lower boundary before valid IDs start) is correctly rejected as Not Found.
        """
        response = comments_service.get_comment_by_id(0)
        assert_status_code(response, 404)
