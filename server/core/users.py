"""
persistent function
"""
import json


def write_to_file(content):
    """
    write user to a json file
    """
    with open("/static/json/users.json", "w", encoding="utf8") as users:
        users.write(json.dumps(content))


def read_from_file():
    """
    read users from a json file
    """
    with open("/static/json/users.json", "r", encoding="utf8") as users:
        return json.loads(users.read())


def get_all_users():
    """
    /api/v1/user get method
    operationId: get_all_users
    """
    users = read_from_file()
    users_in_store = []
    for key, value in users.items():
        current_user = {"id": key, **value}
        users_in_store.append(current_user)

    return users


def remove_user(user_id):
    """
    /api/v1/user/{user_id} delete method
    operationId: remove_user
    """
    users = read_from_file()
    del users[user_id]
    write_to_file(users)


def update_user(user_id, user):
    """
    /api/v1/user/{user_id} put method
    operationId: update_user
    """
    users = read_from_file()
    user_ids = users.keys()
    users[id] = {"name": user.name, "breed": user.breed, "price": user.price}
    write_to_file(users)


def add_user(user):
    users = read_from_file()
    ids = users.keys()
    new_id = int(ids[-1]) + 1
    users[new_id] = {"name": user.name, "breed": user.breed, "price": user.price}
    write_to_file(users)


def get_user(id):
    users = read_from_file()
    user = users[id]
    user["id"] = id
    return user
