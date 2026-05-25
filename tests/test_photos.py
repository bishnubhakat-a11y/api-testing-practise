"""
Photos Test Suite
This file contains Exhaustive Tests (Positive, Negative, Edge, Boundary) for the Photos endpoints.
It uses the `pytest` framework and `allure` for generating beautiful HTML reports.
"""
import allure
import pytest
from src.utils.assertions import assert_status_code
from data.payloads.photos_payload import get_new_photo_payload, get_update_photo_payload

@allure.feature("Photos API - Exhaustive Testing")
class TestPhotosExhaustive:

    # ==========================================
    # POSITIVE TESTS (The "Happy Path")
    # ==========================================
    @allure.story("Positive: Get all photos")
    def test_get_photos_positive(self, photos_service):
        """Verify that fetching all photos returns a 200 OK status code."""
        # Act: Call the API
        response = photos_service.get_photos()
        # Assert: Check the status code
        assert_status_code(response, 200)

    @allure.story("Positive: Get photo by valid ID")
    def test_get_photo_by_id_positive(self, photos_service):
        """Verify that fetching a specific photo by ID works successfully."""
        response = photos_service.get_photo_by_id(1)
        assert_status_code(response, 200)

    @allure.story("Positive: Create a new photo")
    def test_create_photo_positive(self, photos_service):
        """Verify that we can successfully create a new photo."""
        # Arrange: Generate a valid mock payload
        payload = get_new_photo_payload()
        # Act: Send the POST request
        response = photos_service.create_photo(payload)
        # Assert: Expect a 201 Created status
        assert_status_code(response, 201)

    @allure.story("Positive: Update an existing photo")
    def test_update_photo_positive(self, photos_service):
        """Verify that we can successfully update an existing photo."""
        payload = get_update_photo_payload()
        response = photos_service.update_photo(1, payload)
        assert_status_code(response, 200)

    @allure.story("Positive: Delete an existing photo")
    def test_delete_photo_positive(self, photos_service):
        """Verify that we can successfully delete a photo."""
        response = photos_service.delete_photo(1)
        assert_status_code(response, 200)

    # ==========================================
    # NEGATIVE TESTS (Testing invalid data)
    # ==========================================
    @allure.story("Negative: Get photo by non-existent ID")
    def test_get_photo_not_found(self, photos_service):
        """Verify that requesting an ID that does not exist returns a 404 Not Found error."""
        response = photos_service.get_photo_by_id(999999)
        assert_status_code(response, 404)

    @allure.story("Negative: Create photo with invalid data types")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_photo_invalid_types(self, photos_service):
        """
        Verify that the API rejects invalid data types (e.g., sending an integer instead of a string).
        We use xfail here because our mock dummy API accepts bad data anyway.
        """
        payload = get_new_photo_payload()
        # Intentionally corrupt the payload data
        key = list(payload.keys())[0]
        payload[key] = 123456
        response = photos_service.create_photo(payload)
        # Expect a 400 Bad Request
        assert_status_code(response, 400)

    # ==========================================
    # EDGE & BOUNDARY TESTS (Testing limits)
    # ==========================================
    @allure.story("Edge: Create photo with empty payload")
    @pytest.mark.xfail(reason="JSONPlaceholder mock API doesn't enforce strict validations")
    def test_create_photo_empty_payload(self, photos_service):
        """
        Verify the API behaves gracefully when given absolutely no data.
        It should safely reject the request with a 400 Bad Request instead of crashing (500 Error).
        """
        response = photos_service.create_photo({})
        assert_status_code(response, 400)

    @allure.story("Boundary: photo ID at lower bound")
    def test_get_photo_id_zero(self, photos_service):
        """
        Verify that ID `0` (the lower boundary before valid IDs start) is correctly rejected as Not Found.
        """
        response = photos_service.get_photo_by_id(0)
        assert_status_code(response, 404)
