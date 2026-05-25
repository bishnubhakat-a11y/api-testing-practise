def get_new_photo_payload():
    return {
        "albumId": 1,
        "title": "accusamus beatae ad facilis cum similique qui sunt",
        "url": "https://via.placeholder.com/600/92c952",
        "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    }


def get_update_photo_payload():
    return {
        "id": 1,
        "albumId": 1,
        "title": "updated photo title",
        "url": "https://via.placeholder.com/600/000000",
        "thumbnailUrl": "https://via.placeholder.com/150/000000"
    }

def get_delete_photo_payload():
    return {}
