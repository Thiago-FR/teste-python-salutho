from ..model import model_task


def find_all_task():
    result = model_task.find_all_task()

    return result


def create_task(taks):
    result = model_task.create_task(taks)

    return result


def update_task(id, task):
    model_task.update_task(int(id), task)


def delete_task(id):
    model_task.delete_task(int(id))
