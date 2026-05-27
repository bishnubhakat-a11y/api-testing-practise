"""
Posts Test Suite
This file contains Exhaustive Tests (Positive, Negative, Edge, Boundary) for the Posts endpoints.
It uses the `pytest` framework and `allure` for generating beautiful HTML reports.
"""
import allure
import pytest
from src.utils.assertions import assert_status_code, assert_response_time, assert_not_empty, assert_key_exists
from data.payloads.posts_payload import get_new_post_payload, get_update_post_payload

@allure.feature("Posts API - Exhaustive Testing")
@pytest.mark.regression
class TestPostsExhaustive:

    # ==========================================
    # POSITIVE TESTS (The "Happy Path")
    # ==========================================
    @allure.story("Positive: Get all posts")
    @pytest.mark.smoke
    def test_get_posts_positive(self, posts_service):
        """Verify that fetching all posts returns a 200 OK status code."""
        # Act: Call the API
        response = posts_service.get_posts()
        # Assert: Check the status code
        assert_status_code(response, 200)
        assert_response_time(response, 1500)
        assert_not_empty(response.json())

    @allure.story("Positive: Get post by valid ID")
    def test_get_post_by_id_positive(self, posts_service):
        """Verify that fetching a specific post by ID works successfully."""
        response = posts_service.get_post_by_id(1)
        assert_status_code(response, 200)
        assert_response_time(response, 1500)
        assert_key_exists(response.json(), 'id')

    @allure.story("Positive: Create a new post")
    @pytest.mark.smoke
    def test_create_post_positive(self, posts_service):
        """Verify that we can successfully create a new post."""
        # Arrange: Generate a valid mock payload
        payload = get_new_post_payload()
        # Act: Send the POST request
        response = posts_service.create_post(payload)
        # Assert: Expect a 201 Created status
        assert_status_code(response, 201)
        assert_response_time(response, 1500)
        assert_key_exists(response.json(), 'id')

    @allure.story("Positive: Update an existing post")
    def test_update_post_positive(self, posts_service):
        """Verify that we can successfully update an existing post."""
        payload = get_update_post_payload()
        response = posts_service.update_post(1, payload)
        assert_status_code(response, 200)

    @allure.story("Positive: Delete an existing post")
    def test_delete_post_positive(self, posts_service):
        """Verify that we can successfully delete a post."""
        response = posts_service.delete_post(1)
        assert_status_code(response, 200)

    # ==========================================
    # NEGATIVE TESTS (Testing invalid data)
    # ==========================================
    @allure.story("Negative: Get post by non-existent ID")
    def test_get_post_not_found(self, posts_service):
        """Verify that requesting an ID that does not exist returns a 404 Not Found error."""
        response = posts_service.get_post_by_id(999999)
        assert_status_code(response, 404)

    @allure.story("Negative: Create post with invalid data types")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_post_invalid_types(self, posts_service):
        """
        Verify that the API rejects invalid data types (e.g., sending an integer instead of a string).
        We use xfail here because our mock dummy API accepts bad data anyway.
        """
        payload = get_new_post_payload()
        # Intentionally corrupt the payload data
        payload["userId" if "userId" in payload else "title"] = 123456
        response = posts_service.create_post(payload)
        # Expect a 400 Bad Request
        assert_status_code(response, 400)

    # ==========================================
    # EDGE & BOUNDARY TESTS (Testing limits)
    # ==========================================
    @allure.story("Edge: Create post with empty payload")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_post_empty_payload(self, posts_service):
        """
        Verify the API behaves gracefully when given absolutely no data.
        It should safely reject the request with a 400 Bad Request instead of crashing (500 Error).
        """
        response = posts_service.create_post({})
        assert_status_code(response, 400)

    @allure.story("Boundary: post ID at lower bound")
    def test_get_post_id_zero(self, posts_service):
        """
        Verify that ID `0` (the lower boundary before valid IDs start) is correctly rejected as Not Found.
        """
        response = posts_service.get_post_by_id(0)
        assert_status_code(response, 404)

    # ==========================================
    # NESTED RELATIONAL ENDPOINTS
    # ==========================================
    @allure.story("Nested: Get post's comments")
    def test_get_post_comments(self, posts_service):
        response = posts_service.get_post_comments(1)
        assert_status_code(response, 200)
