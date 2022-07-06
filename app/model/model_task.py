def find_all_task(mongo):
    result = list(mongo.find())
    return result


def find_one_task(mongo, id):
    result = mongo.find_one({"_id": id})

    return result


def create_task(mongo, taks):
    mongo.insert_one(taks)

    return True


def update_task(mongo, id, task):
    mongo.find_one_and_update({"_id": id}, {"$set": task})

    return True


def delete_task(mongo, id):
    mongo.find_one_and_delete({"_id": id})

    return True
