from ..model import model_task
import datetime


def find_all_task():
    result = model_task.find_all_task()

    return result


def create_task(responsible, task, status):
    if responsible == '' or task == '' or status == '':
        raise ValueError("Todos os campos devem ser preenchidos")

    get_all_taks = model_task.find_all_task()

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
    result = model_task.create_task(format_task)

    return result


def update_task(id, responsible, task, status):
    if responsible == '' or task == '' or status == '':
        raise ValueError("Todos os campos devem ser preenchidos|400")

    get_task = model_task.find_one_task(int(id))

    if get_task is None:
        raise ValueError("Id não encontrado|404")

    format_task = {
          "_id": 1,
          "responsible": responsible,
          "task": task,
          "status": status,
        }

    model_task.update_task(int(id), format_task)


def delete_task(id):
    get_task = model_task.find_one_task(int(id))

    if get_task is None:
        raise ValueError("Id não encontrado|404")

    model_task.delete_task(int(id))
