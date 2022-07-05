from ..config.database import mongo

def find_all_task():
  get_collection = mongo.db.users
  result = list(get_collection.find())

  return result