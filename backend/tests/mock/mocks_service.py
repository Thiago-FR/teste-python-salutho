def find_all_task(mock):
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


def create_task(mock, task):
    return True


def update_task(mock, id, task):
    return True


def find_one_task(mock, id):
    mongo = {
            "_id": 1,
            "date": "Tue, 05 Jul 2022 20:46:18 GMT",
            "responsible": "Thiago",
            "status": "Concluido",
            "task": "Comer"
        }

    return mongo


def delete_task(mock, id):
    return True