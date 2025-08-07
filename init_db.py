import os
from flask_rest_app.application import create_app
from flask_rest_app import db

if __name__ == "__main__":
    os.environ['APP_ENV'] = 'development'
    app = create_app('development')
    
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!") 