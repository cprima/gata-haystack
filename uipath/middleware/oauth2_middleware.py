"""
OAuth2Middleware.py

This module contains the OAuth2Middleware class which is used for handling OAuth2 authentication in a Flask application. It is designed to be used as middleware that intercepts requests and performs OAuth2 Client Credentials Flow to obtain an access token from an OAuth2 provider. The obtained access token is then used for authenticated requests to external APIs.

The middleware attaches itself to the Flask application using the 'before_request' hook. Every incoming request first triggers the execution of the authenticate_request method. This method authenticates with the configured OAuth2 provider using client credentials (client ID and client secret) and retrieves an access token. The access token is then stored in the Flask application context, making it available for use in subsequent route handlers.

Key Functions:
- __init__(app=None): Initializes the OAuth2Middleware instance. Optionally takes a Flask app object to immediately register the middleware.
- init_app(app): Attaches the middleware to a Flask application.
- authenticate_request(): Handles the actual OAuth2 authentication process. This method is automatically invoked before each request to ensure that a valid access token is always available.

External libraries used:
- `requests`: For making HTTP POST requests to the OAuth2 provider's token endpoint.
- `flask`: For accessing the current application context and returning JSON responses in case of authentication failure.

Configuration:
The middleware expects the following configuration variables to be present in the Flask application's configuration:
- `UIPATH_ACCESS_TOKEN_URL`: The OAuth2 token endpoint URL.
- `UIPATH_CLIENT_ID`: The client ID for OAuth2 authentication.
- `UIPATH_CLIENT_SECRET`: The client secret for OAuth2 authentication.
- `UIPATH_SCOPE`: The scope of the access request.

Note:
The middleware assumes that the Flask application will handle any necessary error responses or exceptions that may occur during the authentication process.
"""
import requests
from flask import current_app as app, jsonify

class OAuth2Middleware:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(self.authenticate_request)

    def authenticate_request(self):
        # Implement the OAuth2 Client Credentials Flow
        auth_response = requests.post(
            app.config['UIPATH_ACCESS_TOKEN_URL'],
            data={
                'grant_type': 'client_credentials',
                'client_id': app.config['UIPATH_CLIENT_ID'],
                'client_secret': app.config['UIPATH_CLIENT_SECRET'],
                'scope': app.config['UIPATH_SCOPE']
            }
        )

        # Check for successful authentication
        if auth_response.status_code == 200:
            app.access_token = auth_response.json().get('access_token')
        else:
            return jsonify({'error': 'Authentication failed'}), auth_response.status_code
