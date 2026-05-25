def get_new_post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }



def get_update_post_payload():
    return {
        "id": 1,
        "title": "updated foo",
        "body": "updated bar",
        "userId": 1
    }

def get_delete_post_payload():
    return {}
