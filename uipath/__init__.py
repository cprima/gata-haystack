from flask import Flask
import os
from .middleware.oauth2_middleware import OAuth2Middleware

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load the default configuration
    app.config.from_object('config.default')

    # Initialize middleware
    OAuth2Middleware(app)

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    app.config.from_envvar('APP_CONFIG_FILE')

    # Import routes
    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
