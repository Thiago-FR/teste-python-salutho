from ..config.database import mongo


def find_all_task():
    get_collection = mongo.db.users
    result = list(get_collection.find())

    return result


def find_one_task(id):
    get_collection = mongo.db.users
    result = get_collection.find_one({"_id": id})

    return result


def create_task(taks):
    get_collection = mongo.db.users
    result = get_collection.insert_one(taks).inserted_id

    return result


def update_task(id, task):
    get_collection = mongo.db.users
    get_collection.find_one_and_update({"_id": id}, {"$set": task})


def delete_task(id):
    get_collection = mongo.db.users
    get_collection.find_one_and_delete({"_id": id})
