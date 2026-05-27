from src.utils.helpers import generate_random_email, generate_random_string

def get_new_user_payload():
    return {
        "name": f"Test User {generate_random_string(5)}",
        "username": f"user_{generate_random_string(5).lower()}",
        "email": generate_random_email()
    }


def get_update_user_payload():
    return {
        "id": 1,
        "name": f"Updated User {generate_random_string(5)}",
        "username": f"updated_{generate_random_string(5).lower()}",
        "email": generate_random_email()
    }

def get_delete_user_payload():
    return {}
