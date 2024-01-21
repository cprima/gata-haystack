"""
routes.py

This module defines the routes for the Flask application 'project-gata-haystack'. It includes routes for displaying the main index page and for handling requests to the UiPath Orchestrator API.

The module uses a Flask Blueprint named 'routes' to define and manage these routes. It makes use of the Flask `render_template` function to render HTML templates, and `jsonify` for returning JSON responses.

Routes:
- `/`: The index route which renders the homepage with the project name.
- `/uipath/machines`: A route to fetch and display machine data from the UiPath Orchestrator API. This route utilizes an OAuth2 access token, obtained and managed by middleware, to authenticate the API request.

The module expects the OAuth2 access token to be provided by middleware and uses Flask's `current_app` context to access the application configuration and the access token.

External libraries used:
- `flask`: For creating routes and handling HTTP requests.
- `requests`: For making HTTP requests to external APIs.
"""
from flask import Blueprint, render_template, jsonify, current_app as app
import requests

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html', project_name="project-gata-haystack")

@routes.route('/uipath/machines')
def get_uipath_machines():
    # Use the access token provided by the middleware
    access_token = app.access_token

    # Construct the API URL
    api_url = app.config['UIPATH_CLOUD_BASEURL'].rstrip('/') + '/' + app.config['UIPATH_CLOUD_ORGNAME'] + '/' + app.config['UIPATH_CLOUD_TENANTNAME_CURRENT'] + '/orchestrator_/odata/Machines'

    # Call the API with the access token
    api_response = requests.get(
        api_url,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    # Check for successful API response
    if api_response.status_code == 200:
        machines = api_response.json().get('value', [])
        # Pass the machines data to the render_template function
        return render_template('machines.html', machines=machines)
    else:
        return jsonify({'error': 'Failed to retrieve data from API'}), api_response.status_code
