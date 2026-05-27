from src.utils.helpers import generate_random_string

def get_new_todo_payload():
    return {
        "title": f"Learn API Automation {generate_random_string(5)}",
        "completed": False,
        "userId": 1
    }



def get_update_todo_payload():
    return {
        "id": 1,
        "title": f"Master API Automation {generate_random_string(5)}",
        "completed": True,
        "userId": 1
    }

def get_delete_todo_payload():
    return {}
