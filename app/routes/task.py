from crypt import methods
from flask import Blueprint
from ..controller import controller_task

task = Blueprint("task", __name__)

@task.route('/', methods=["GET"])
def index():
  return controller_task.find_all_task()
  # userCollection = mongo.db.users
  # user = {"_id": 1, "name": "Thiago", "taks": "Comer"}
  # result = list(userCollection.find())
  # userCollection.insert_one(user)

@task.route('/insert', methods=["POST"])
def list_task():
  return controller_task.create_task()

@task.route('/edit')
def edit_taks():
  return 'Edit Taks'

@task.route('/delete')
def delete_task():
  return 'Delete Taks'

