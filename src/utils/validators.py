import json
import os
from jsonschema import validate, ValidationError

def validate_schema(instance, schema_filename):
    schema_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'schemas', schema_filename)
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    try:
        validate(instance=instance, schema=schema)
        return True
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")
