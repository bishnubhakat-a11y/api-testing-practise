import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestUsersSchema:
    @allure.story("Validate GET /users response schema")
    def test_users_schema_validation(self, users_service):
        response = users_service.get_users()
        assert_status_code(response, 200)
        users = response.json()
        assert isinstance(users, list)
        for user in users:
            validate_schema(user, "user_schema.json")
            
    @allure.story("Validate GET /users/{id} response schema")
    def test_single_user_schema_validation(self, users_service):
        response = users_service.get_user_by_id(1)
        assert_status_code(response, 200)
        validate_schema(response.json(), "user_schema.json")
