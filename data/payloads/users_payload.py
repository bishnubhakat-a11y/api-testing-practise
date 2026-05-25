def get_new_user_payload():
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }


def get_update_user_payload():
    return {
        "id": 1,
        "name": "Updated Test User",
        "username": "updatedtestuser",
        "email": "updated@example.com"
    }

def get_delete_user_payload():
    return {}
