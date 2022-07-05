from ..config.database import mongo

def find_all_task():
  get_collection = mongo.db.users
  result = list(get_collection.find())

  return result

def create_task(taks):
  get_collection = mongo.db.users
  result = get_collection.insert_one(taks).inserted_id

  return result