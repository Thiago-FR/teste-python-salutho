from flask import jsonify, request
import pymongo
from ..model import model_task
from ..config.database import mongo


def find_all_task(service_task):
    result = service_task.find_all_task(model_task, mongo.db.users)

    return jsonify(result), 200


def create_task(service_task):
    try:
        description = request.json["description"]
        task = request.json["task"]
        status = request.json["status"]

        result = service_task.create_task(
          model_task,
          mongo.db.users,
          description,
          task,
          status,
        )

        return jsonify({"message": result}), 201
    except pymongo.errors.DuplicateKeyError:
        return jsonify({"message": "Id já existe"}), 401
    except (KeyError, ValueError):
        return jsonify({
          "message": "Todos os campos devem ser preenchidos"
        }), 401


def update_task(service_task, id):
    try:
        description = request.json["description"]
        task = request.json["task"]
        status = request.json["status"]

        service_task.update_task(
          model_task,
          mongo.db.users,
          id,
          description,
          task,
          status,
        )

        return jsonify({"message": "Update True"}), 200
    except KeyError:
        return jsonify({
              "message": "Todos os campos devem ser preenchidos"
            }), 401
    except ValueError as error:
        message, code = str(error).split('|')

        return jsonify({
              "message": message
            }), code


def delete_task(service_task, id):
    try:
        service_task.delete_task(model_task, mongo.db.users, id)

        return jsonify({"message": "Delete True"}), 200
    except ValueError as error:
        message, code = str(error).split('|')

        return jsonify({
              "message": message
            }), code
