from flask import Blueprint
from ..controller import controller_task
from ..service import service_task

task = Blueprint("task", __name__)

LIST_URL = '/api/todo-list'


@task.route(LIST_URL, methods=["GET"])
def list_taks():
    return controller_task.find_all_task(service_task)


@task.route(LIST_URL, methods=["POST"])
def create_task():
    return controller_task.create_task(service_task)


@task.route(f'{LIST_URL}/<id>', methods=["PUT"])
def edit_taks(id):
    return controller_task.update_task(service_task, id)


@task.route(f'{LIST_URL}/<id>', methods=["DELETE"])
def delete_task(id):
    return controller_task.delete_task(service_task, id)
