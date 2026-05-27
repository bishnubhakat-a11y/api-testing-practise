from src.utils.helpers import generate_random_email, generate_random_string

def get_new_comment_payload():
    return {
        "postId": 1,
        "name": f"Comment Title {generate_random_string(5)}",
        "email": generate_random_email(),
        "body": f"This is a randomly generated comment body: {generate_random_string(20)}"
    }


def get_update_comment_payload():
    return {
        "id": 1,
        "postId": 1,
        "name": f"Updated Title {generate_random_string(5)}",
        "email": generate_random_email(),
        "body": f"This is a randomly updated comment body: {generate_random_string(20)}"
    }

def get_delete_comment_payload():
    return {}
