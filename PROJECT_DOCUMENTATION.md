# API Automation Testing Framework Documentation

## 1. Project Overview

This project is a Python-based API automation testing framework for the public JSONPlaceholder API. It uses `pytest` for test execution, `requests` for HTTP communication, `jsonschema` for schema validation, Allure and `pytest-html` for reporting, and Locust for performance testing.

The framework is organized around a layered design:

- `src/api`: low-level HTTP client and route constants.
- `src/services`: resource-specific service classes that expose readable API actions.
- `data/payloads`: reusable request payload factories.
- `data/schemas`: JSON Schema files used to validate API responses.
- `tests`: functional, negative, boundary, nested-resource, and schema validation tests.
- `performance`: Locust-based load test scripts.

The default target API is:

```text
https://jsonplaceholder.typicode.com
```

## 2. Technology Stack

| Area | Tool |
| --- | --- |
| Language | Python |
| Test runner | pytest |
| HTTP client | requests |
| Reporting | allure-pytest, pytest-html |
| Schema validation | jsonschema |
| Configuration | python-dotenv, PyYAML |
| Performance testing | locust |

## 3. Repository Structure

```text
api-testing-framework/
|-- config/
|   |-- config.py
|   `-- settings.yaml
|-- data/
|   |-- payloads/
|   |   |-- albums_payload.py
|   |   |-- comments_payload.py
|   |   |-- photos_payload.py
|   |   |-- posts_payload.py
|   |   |-- todos_payload.py
|   |   `-- users_payload.py
|   `-- schemas/
|       |-- album_schema.json
|       |-- comment_schema.json
|       |-- photo_schema.json
|       |-- post_schema.json
|       |-- todo_schema.json
|       `-- user_schema.json
|-- logs/
|-- performance/
|   |-- load_test.py
|   `-- locustfile.py
|-- reports/
|-- src/
|   |-- api/
|   |   |-- api_client.py
|   |   `-- routes.py
|   |-- services/
|   |   |-- albums_service.py
|   |   |-- comments_service.py
|   |   |-- photos_service.py
|   |   |-- posts_service.py
|   |   |-- todos_service.py
|   |   `-- users_service.py
|   `-- utils/
|       |-- assertions.py
|       |-- helpers.py
|       |-- logger.py
|       `-- validators.py
|-- tests/
|   |-- schema_validations/
|   |-- conftest.py
|   |-- test_albums.py
|   |-- test_comments.py
|   |-- test_photos.py
|   |-- test_posts.py
|   |-- test_todos.py
|   `-- test_users.py
|-- .env
|-- pytest.ini
|-- requirements.txt
|-- run_tests.py
`-- README.md
```

## 4. Configuration

Configuration is loaded from environment variables and YAML settings.

### Environment Variables

`config/config.py` loads `.env` using `python-dotenv` and defines these values:

| Variable | Default | Purpose |
| --- | --- | --- |
| `BASE_URL` | `https://jsonplaceholder.typicode.com` | Base API URL |
| `API_USERNAME` | `bishnu` | Basic auth username |
| `API_PASSWORD` | `123456` | Basic auth password |

The API client attaches these credentials to every request through `requests.Session.auth`. JSONPlaceholder does not require authentication, but the framework is ready for APIs that do.

### YAML Settings

`config/settings.yaml` currently defines per-environment timeout values:

```yaml
environment:
  dev:
    timeout: 10
  prod:
    timeout: 30
```

At the moment, these settings are loaded into `config.SETTINGS` but are not yet applied by `APIClient`.

## 5. Core Architecture

### API Client

`src/api/api_client.py` contains the shared `APIClient`.

Responsibilities:

- Creates a reusable `requests.Session`.
- Applies the base URL from configuration.
- Applies basic authentication and JSON headers.
- Provides generic `request()` handling.
- Provides convenience methods: `get()`, `post()`, `put()`, and `delete()`.
- Logs outgoing requests and response status codes.
- Attaches request and response details to Allure reports.

All service calls ultimately flow through this client.

### Routes

`src/api/routes.py` centralizes endpoint paths:

| Constant | Path |
| --- | --- |
| `Routes.USERS` | `/users` |
| `Routes.POSTS` | `/posts` |
| `Routes.COMMENTS` | `/comments` |
| `Routes.ALBUMS` | `/albums` |
| `Routes.PHOTOS` | `/photos` |
| `Routes.TODOS` | `/todos` |

This avoids hardcoding endpoint strings across tests.

### Service Layer

Each service class wraps API operations for one resource. Tests use these services instead of calling `requests` directly.

| Service | Main Operations |
| --- | --- |
| `UsersService` | Get all, get by ID, create, update, delete, get user's albums, todos, posts |
| `PostsService` | Get all, get by ID, create, update, delete, get post comments |
| `CommentsService` | Get all, get by ID, create, update, delete |
| `AlbumsService` | Get all, get by ID, create, update, delete, get album photos |
| `PhotosService` | Get all, get by ID, create, update, delete |
| `TodosService` | Get all, get by ID, create, update, delete |

This keeps tests readable and makes endpoint changes easier to manage.

## 6. Test Design

The framework includes tests for six JSONPlaceholder resources:

- Users
- Posts
- Comments
- Albums
- Photos
- Todos

The functional test files follow a consistent structure:

- Positive tests for valid reads, creates, updates, and deletes.
- Negative tests for missing IDs.
- Invalid payload tests marked as `xfail` because JSONPlaceholder accepts many invalid requests.
- Edge tests such as empty payload creation.
- Boundary tests such as requesting ID `0`.
- Nested endpoint tests where supported.

Examples of nested endpoint coverage:

| Test Area | Endpoint Pattern |
| --- | --- |
| User albums | `/users/{id}/albums` |
| User todos | `/users/{id}/todos` |
| User posts | `/users/{id}/posts` |
| Post comments | `/posts/{id}/comments` |
| Album photos | `/albums/{id}/photos` |

### Pytest Markers

Markers are configured in `pytest.ini`:

| Marker | Meaning |
| --- | --- |
| `smoke` | Quick critical checks for basic API availability |
| `regression` | Full functional suite coverage |

Most resource test classes are marked as `regression`. List and create tests are commonly marked as `smoke`.

### Fixtures

`tests/conftest.py` creates session-scoped fixtures for all service classes:

- `users_service`
- `posts_service`
- `todos_service`
- `comments_service`
- `albums_service`
- `photos_service`

It also customizes `pytest-html` reports by adding a title, summary heading, execution duration column, and test description column.

## 7. Schema Validation

Schema validation tests live under:

```text
tests/schema_validations/
```

Each schema test:

1. Calls a service method.
2. Asserts the response status code.
3. Parses the JSON response.
4. Validates response objects against JSON Schema files from `data/schemas`.

The schema helper is:

```text
src/utils/validators.py
```

It uses `jsonschema.validate()` and raises an `AssertionError` with a readable validation message when a response does not match the expected schema.

## 8. Test Data and Payloads

Payload factories live in:

```text
data/payloads/
```

Each resource has functions for creating request bodies, such as:

- `get_new_user_payload()`
- `get_update_user_payload()`
- `get_new_post_payload()`
- `get_update_post_payload()`

Payload modules use helper functions from `src/utils/helpers.py` to generate random strings and emails where needed. This reduces duplicate static test data and lowers the chance of accidental conflicts.

## 9. Assertions and Utilities

`src/utils/assertions.py` provides reusable assertion helpers:

| Helper | Purpose |
| --- | --- |
| `assert_status_code(response, expected_code)` | Verifies HTTP status code |
| `assert_response_time(response, max_ms)` | Verifies response time SLA in milliseconds |
| `assert_key_exists(response_json, key)` | Verifies a JSON key exists |
| `assert_key_value(response_json, key, expected_value)` | Verifies a JSON key has an expected value |
| `assert_not_empty(response_json)` | Verifies a JSON list or dict is not empty |

Using these helpers keeps tests concise and standardizes failure messages.

## 10. Reporting

### Allure

`pytest.ini` sets the default pytest options:

```ini
addopts = --alluredir=reports/allure-results -v
```

This means normal pytest runs automatically generate Allure result files in:

```text
reports/allure-results
```

Run tests and serve the Allure report:

```bash
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

The API client attaches request and response details to Allure, which helps debug failing tests.

### Pytest HTML

To generate a standalone HTML report:

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

The custom hooks in `tests/conftest.py` add:

- Report title: `Enterprise API Automation Report`
- Execution summary heading
- Test duration column
- Description column populated from each test docstring

## 11. Performance Testing

Performance scripts live in:

```text
performance/
```

`performance/locustfile.py` defines an `APIUser` class with tasks for:

- `/users`
- `/posts`
- `/albums`
- `/comments`
- `/photos`
- `/todos`

Each simulated user waits between 1 and 3 seconds between requests.

Run Locust with:

```bash
locust -f performance/locustfile.py --host=https://jsonplaceholder.typicode.com
```

Then open:

```text
http://localhost:8089
```

The project also includes `performance/load_test.py`, which can be used as a convenience launcher if configured for the local environment.

## 12. Setup and Execution

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest tests/
```

### Run Smoke Tests

```bash
pytest -m smoke
```

### Run Regression Tests

```bash
pytest -m regression
```

### Run Through the Python Runner

```bash
python run_tests.py
```

`run_tests.py` changes into the project root and executes:

```text
pytest tests/ --alluredir=reports/allure-results -v
```

## 13. How to Add a New API Resource

To add a new API resource, follow the existing pattern:

1. Add a route constant in `src/api/routes.py`.
2. Create a service class in `src/services/`.
3. Add payload factory functions in `data/payloads/` if the resource supports create or update operations.
4. Add a JSON Schema file in `data/schemas/`.
5. Register a service fixture in `tests/conftest.py`.
6. Create functional tests in `tests/`.
7. Create schema validation tests in `tests/schema_validations/`.
8. Add Locust tasks in `performance/locustfile.py` if the endpoint should be performance tested.

Recommended service method naming:

```text
get_<resources>()
get_<resource>_by_id(item_id)
create_<resource>(payload)
update_<resource>(item_id, payload)
delete_<resource>(item_id)
```

## 14. Current Strengths

- Clear separation between client, service, data, schema, and test layers.
- Consistent resource coverage across JSONPlaceholder endpoints.
- Reusable fixtures and assertion helpers.
- Allure request/response attachments improve failure investigation.
- Supports both functional and performance testing.
- Uses `xfail` appropriately for mock API validation gaps.

## 15. Known Limitations and Improvement Opportunities

- `config/settings.yaml` timeout values are loaded but not applied to HTTP requests.
- Basic authentication is always attached, although JSONPlaceholder does not require it.
- Some schema validation files have broader coverage than others; for example, certain resources validate only collection responses.
- The README folder tree contains encoding artifacts and can be cleaned up.
- Negative validation tests depend on JSONPlaceholder behavior, which is intentionally permissive and not representative of strict production APIs.
- The framework does not currently include retry handling, request timeout enforcement, or environment selection logic.
- There is no CI configuration file yet.

## 16. Recommended Next Enhancements

- Apply configured request timeouts in `APIClient.request()`.
- Add an environment selector such as `ENV=dev` or `ENV=prod`.
- Add CI execution using GitHub Actions or another pipeline tool.
- Standardize schema validation so every resource validates both list and single-object responses where applicable.
- Add query parameter tests, such as filtering posts by `userId`.
- Add centralized test data cleanup for real APIs that persist created entities.
- Add logging rotation or cleanup rules for generated logs and reports.

