import allure
from src.utils.assertions import assert_status_code
from src.utils.validators import validate_schema

@allure.feature("Schema Validation")
class TestTodosSchema:
    @allure.story("Validate GET /todos response schema")
    def test_todos_schema_validation(self, todos_service):
        response = todos_service.get_todos()
        assert_status_code(response, 200)
        todos = response.json()
        assert len(todos) > 0
        validate_schema(todos[0], "todo_schema.json")
