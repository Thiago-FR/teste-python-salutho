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
