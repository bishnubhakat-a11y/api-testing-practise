from src.utils.helpers import generate_random_string

def get_new_album_payload():
    return {
        "userId": 1,
        "title": f"Album Title {generate_random_string(8)}"
    }

def get_update_album_payload():
    return {
        "id": 1,
        "userId": 1,
        "title": f"Updated Album Title {generate_random_string(8)}"
    }

def get_delete_album_payload():
    return {}
