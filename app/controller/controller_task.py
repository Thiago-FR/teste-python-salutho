from flask import jsonify, request
from ..service import service_task

def find_all_task():
  result = service_task.find_all_task()

  return jsonify({ "message": result }), 200

def create_task():
  username = request.json["username"]
  task = request.json["task"]
  status = request.json["status"]

  result = service_task.create_task({
    "_id": 1,
    "username": username,
    "task": task,
    "status": status,
  })

  return jsonify({ "message": result }), 201
