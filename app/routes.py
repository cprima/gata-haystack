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



@routes.route('/uipath/get-processes')
def get_process_data():
    # Use the access token provided by the middleware
    access_token = app.access_token

    # Construct the API URL
    api_url = app.config['UIPATH_CLOUD_BASEURL'].rstrip('/') + '/' + app.config['UIPATH_CLOUD_ORGNAME'] + '/' + app.config['UIPATH_CLOUD_TENANTNAME_CURRENT'] + '/orchestrator_/odata/Processes'

    # Call the API with the access token
    api_response = requests.get(
        api_url,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    # Check for successful API response
    if api_response.status_code == 200:
        data = api_response.json()
        # Further processing of data can be done here as required
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to retrieve data from the UiPath API', 'status_code': api_response.status_code}), api_response.status_code


@routes.route('/uipath/get-releases')
def get_uipath_releases():
    # Use the access token provided by the middleware
    access_token = app.access_token

    # Construct the API URL for the Releases endpoint
    api_url = app.config['UIPATH_CLOUD_BASEURL'].rstrip('/') + '/' + app.config['UIPATH_CLOUD_ORGNAME'] + '/' + app.config['UIPATH_CLOUD_TENANTNAME_CURRENT'] + '/orchestrator_/odata/Releases'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-UIPATH-OrganizationUnitId': '4962651'  # Set the OrganizationUnitId
    }

    # Call the API with the access token and additional headers
    api_response = requests.get(api_url, headers=headers)

    # Check for successful API response
    if api_response.status_code == 200:
        releases = api_response.json()
        # You can process the data as needed here
        return jsonify(releases)
    else:
        #return jsonify({'error': 'Failed to retrieve data from the UiPath API', 'status_code': api_response.status_code}), api_response.status_code
        error_info = {
            'error': 'Failed to retrieve data from the UiPath API',
            'status_code': api_response.status_code,
            'api_response': api_response.text  # Include API response text
        }
        return jsonify(error_info), api_response.status_code