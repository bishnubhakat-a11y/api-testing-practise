from src.utils.helpers import generate_random_string

def get_new_photo_payload():
    return {
        "albumId": 1,
        "title": f"Photo Title {generate_random_string(10)}",
        "url": f"https://via.placeholder.com/600/{generate_random_string(6)}",
        "thumbnailUrl": f"https://via.placeholder.com/150/{generate_random_string(6)}"
    }


def get_update_photo_payload():
    return {
        "id": 1,
        "albumId": 1,
        "title": f"Updated Photo Title {generate_random_string(10)}",
        "url": f"https://via.placeholder.com/600/{generate_random_string(6)}",
        "thumbnailUrl": f"https://via.placeholder.com/150/{generate_random_string(6)}"
    }

def get_delete_photo_payload():
    return {}
