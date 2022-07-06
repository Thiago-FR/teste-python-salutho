def find():
    mongo = [
        {
            "_id": 1,
            "date": "Tue, 05 Jul 2022 20:46:18 GMT",
            "responsible": "Thiago",
            "status": "Concluido",
            "task": "Comer"
        }
      ]

    return mongo


def find_one(id):
    mongo = {
          "_id": 1,
          "date": "Tue, 05 Jul 2022 20:46:18 GMT",
          "responsible": "Thiago",
          "status": "Concluido",
          "task": "Comer"
      }

    return mongo


def insert_one(obj):
    return True


def find_one_and_update(id, task):
    return True


def find_one_and_delete(id):
    return True
