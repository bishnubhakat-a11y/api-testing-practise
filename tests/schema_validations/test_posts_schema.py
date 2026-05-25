import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestPostsSchema:
    @allure.story("Validate GET /posts response schema")
    def test_posts_schema_validation(self, posts_service):
        response = posts_service.get_posts()
        assert_status_code(response, 200)
        posts = response.json()
        assert len(posts) > 0
        validate_schema(posts[0], "post_schema.json")
