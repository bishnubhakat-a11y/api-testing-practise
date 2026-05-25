import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestCommentsSchema:
    @allure.story("Validate GET /comments response schema")
    def test_comments_schema_validation(self, comments_service):
        response = comments_service.get_comments()
        assert_status_code(response, 200)
        items = response.json()
        assert isinstance(items, list)
        for item in items:
            validate_schema(item, "comment_schema.json")
            
    @allure.story("Validate GET /comments/{id} response schema")
    def test_single_comment_schema_validation(self, comments_service):
        response = comments_service.get_comment_by_id(1)
        assert_status_code(response, 200)
        validate_schema(response.json(), "comment_schema.json")
