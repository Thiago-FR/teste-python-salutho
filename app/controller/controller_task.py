from flask import jsonify
from ..service import service_task

def find_all_task():
  result = service_task.find_all_task()

  return jsonify({ "message": result }), 200