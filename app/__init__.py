from flask import Flask
from config import DevelopmentConfig, ProductionConfig
import os
from .middleware.oauth2_middleware import OAuth2Middleware


def create_app():
    app = Flask(__name__)

    # Initialize middleware
    OAuth2Middleware(app)
    
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Import routes
    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
