import os
from flask_rest_app.application import create_app

if __name__ == "__main__":
    os.environ['APP_ENV'] = 'development'
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000, debug=True) 