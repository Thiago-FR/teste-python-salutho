from flask import jsonify, request
import pymongo
from ..service import service_task


def find_all_task():
    result = service_task.find_all_task()

    return jsonify(result), 200


def create_task():
    try:
        responsible = request.json["responsible"]
        task = request.json["task"]
        status = request.json["status"]

        result = service_task.create_task(
          responsible,
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


def update_task(id):
    try:
        responsible = request.json["responsible"]
        task = request.json["task"]
        status = request.json["status"]

        service_task.update_task(
          id,
          responsible,
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


def delete_task(id):
    try:
        service_task.delete_task(id)

        return jsonify({"message": "Delete True"}), 200
    except ValueError as error:
        message, code = str(error).split('|')

        return jsonify({
              "message": message
            }), code
