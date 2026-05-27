import random
import string
import json
from datetime import datetime, timedelta

def generate_random_string(length=10):
    """Generates a random alphanumeric string of the given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_email():
    """Generates a random, unique email address."""
    prefix = generate_random_string(8).lower()
    return f"{prefix}@automation.com"

def generate_random_phone_number():
    """Generates a random 10-digit phone number string."""
    return str(random.randint(1000000000, 9999999999))

def generate_future_date(days_ahead=1):
    """Returns an ISO-formatted timestamp for future dates."""
    future_date = datetime.now() + timedelta(days=days_ahead)
    return future_date.isoformat()

def read_json_file(file_path):
    """Reads and parses a JSON file into a Python dictionary."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_id_from_response(response):
    """Safely extracts the 'id' field from an API JSON response."""
    try:
        response_json = response.json()
        return response_json.get('id', None)
    except Exception as e:
        print(f"Error extracting id from response: {e}")
        return None
