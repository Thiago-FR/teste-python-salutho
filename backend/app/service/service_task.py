# from ..config.database import mongo
import datetime


def find_all_task(model_task, mongo):
    result = model_task.find_all_task(mongo)

    return result


def create_task(model_task, mongo, responsible, task, status):
    if responsible == '' or task == '' or status == '':
        raise ValueError("Todos os campos devem ser preenchidos")

    get_all_taks = model_task.find_all_task(mongo)

    new_id = 0

    if len(get_all_taks) != 0:
        new_id = int(get_all_taks[-1]["_id"])

    new_id += 1

    format_task = {
          "_id": new_id,
          "responsible": responsible,
          "task": task,
          "status": status,
          "date": datetime.datetime.now(),
        }

    model_task.create_task(mongo, format_task)

    return format_task


def update_task(model_task, mongo, id, responsible, task, status):
    if responsible == '' or task == '' or status == '':
        raise ValueError("Todos os campos devem ser preenchidos|400")

    get_task = model_task.find_one_task(mongo, int(id))

    if get_task is None:
        raise ValueError("Id não encontrado|404")

    format_task = {
          "_id": 1,
          "responsible": responsible,
          "task": task,
          "status": status,
        }

    model_task.update_task(mongo, int(id), format_task)


def delete_task(model_task, mongo, id):
    get_task = model_task.find_one_task(mongo, int(id))

    if get_task is None:
        raise ValueError("Id não encontrado|404")

    model_task.delete_task(mongo, int(id))
