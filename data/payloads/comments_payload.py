def get_new_comment_payload():
    return {
        "postId": 1,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }


def get_update_comment_payload():
    return {
        "id": 1,
        "postId": 1,
        "name": "updated name",
        "email": "updated@gardner.biz",
        "body": "updated body text"
    }

def get_delete_comment_payload():
    return {}
