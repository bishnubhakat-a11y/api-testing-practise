def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

def assert_response_time(response, max_ms):
    """Asserts that the API responded within max_ms milliseconds."""
    elapsed_ms = response.elapsed.total_seconds() * 1000
    assert elapsed_ms < max_ms, f"Response time {elapsed_ms}ms exceeded the SLA of {max_ms}ms"

def assert_key_exists(response_json, key):
    """Asserts that a specific key exists in the JSON response."""
    assert key in response_json, f"Key '{key}' not found in response JSON: {response_json}"

def assert_key_value(response_json, key, expected_value):
    """Asserts that a specific key holds the exact expected value."""
    assert_key_exists(response_json, key)
    actual_value = response_json[key]
    assert actual_value == expected_value, f"Expected '{key}' to be '{expected_value}', but got '{actual_value}'"

def assert_not_empty(response_json):
    """Asserts that a response list or dict is not empty."""
    assert len(response_json) > 0, "Expected response JSON to not be empty"
