from src.utils.helpers import generate_random_string

def get_new_post_payload():
    return {
        "title": f"Post Title {generate_random_string(6)}",
        "body": f"Post body content {generate_random_string(15)}",
        "userId": 1
    }



def get_update_post_payload():
    return {
        "id": 1,
        "title": f"Updated Post Title {generate_random_string(6)}",
        "body": f"Updated body content {generate_random_string(15)}",
        "userId": 1
    }

def get_delete_post_payload():
    return {}
