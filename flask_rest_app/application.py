import logging
import os

from flask import Flask, jsonify
from werkzeug.utils import import_string
from . import config, db

logger = logging.getLogger(__name__)


def create_app(environment):
    """Creates a new Flask application and initialize application."""

    config_map = {
        'development': config.Development(),
        'testing': config.Testing(),
        'production': config.Production(),
    }

    config_obj = config_map[environment.lower()]

    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.url_map.strict_slashes = False
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/init-db', 'init_db', init_db)

    register_blueprints(app)

    db.init_app(app)

    return app


def home():
    return jsonify(dict(name='Flask REST API'))


def init_db():
    """Initialize database tables"""
    try:
        db.create_all()
        return jsonify(dict(message='Database tables created successfully!'))
    except Exception as e:
        return jsonify(dict(error=str(e))), 500


def register_blueprints(app):
    root_folder = 'flask_rest_app'

    for dir_name in os.listdir(root_folder):
        module_name = root_folder + '.' + dir_name + '.views'
        module_path = os.path.join(root_folder, dir_name, 'views.py')

        if os.path.exists(module_path):
            try:
                module = import_string(module_name)
                obj = getattr(module, 'app', None)
                if obj:
                    app.register_blueprint(obj)
            except Exception as e:
                logger.warning(f"Could not register blueprint for {module_name}: {e}")
