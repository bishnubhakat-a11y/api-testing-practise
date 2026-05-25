def get_new_todo_payload():
    return {
        "title": "learn API automation",
        "completed": False,
        "userId": 1
    }



def get_update_todo_payload():
    return {
        "id": 1,
        "title": "learn API automation and testing",
        "completed": True,
        "userId": 1
    }

def get_delete_todo_payload():
    return {}
