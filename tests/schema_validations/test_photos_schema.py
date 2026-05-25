import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestPhotosSchema:
    @allure.story("Validate GET /photos response schema")
    def test_photos_schema_validation(self, photos_service):
        response = photos_service.get_photos()
        assert_status_code(response, 200)
        items = response.json()
        assert isinstance(items, list)
        for item in items:
            validate_schema(item, "photo_schema.json")
            
    @allure.story("Validate GET /photos/{id} response schema")
    def test_single_photo_schema_validation(self, photos_service):
        response = photos_service.get_photo_by_id(1)
        assert_status_code(response, 200)
        validate_schema(response.json(), "photo_schema.json")
