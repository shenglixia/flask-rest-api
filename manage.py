from flask_migrate import Migrate
from flask_script import Manager
from flask_rest_app import db
from flask_rest_app.application import create_app

app = create_app('development')

migrate = Migrate(app, db)

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
