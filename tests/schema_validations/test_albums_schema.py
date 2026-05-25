import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestAlbumsSchema:
    @allure.story("Validate GET /albums response schema")
    def test_albums_schema_validation(self, albums_service):
        response = albums_service.get_albums()
        assert_status_code(response, 200)
        items = response.json()
        assert isinstance(items, list)
        for item in items:
            validate_schema(item, "album_schema.json")
            
    @allure.story("Validate GET /albums/{id} response schema")
    def test_single_album_schema_validation(self, albums_service):
        response = albums_service.get_album_by_id(1)
        assert_status_code(response, 200)
        validate_schema(response.json(), "album_schema.json")
