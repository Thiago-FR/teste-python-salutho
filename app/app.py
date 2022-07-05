from flask import Flask
from .routes.task import task
from .config import database

def create_app(config_object="app.config.settings"):
  app = Flask(__name__)
  app.config.from_object(config_object)
  app.register_blueprint(task)
  database.init_app(app)

  return app
