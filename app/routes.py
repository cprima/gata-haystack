from flask import Blueprint, jsonify, render_template, request
import requests
import os

routes = Blueprint('routes', __name__)

from flask import current_app as app

@routes.route('/')
def index():
    return render_template('index.html', project_name="project-gata-haystack")


@routes.route('/uipath/machines')
def get_uipath_machines():
    # OAuth2 Client Credentials Flow
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
        access_token = auth_response.json().get('access_token')
        # Call the API
        api_response = requests.get(
            app.config['UIPATH_CLOUD_BASEURL'].rstrip('/') + '/' + app.config['UIPATH_CLOUD_ORGNAME'] + '/' + app.config['UIPATH_CLOUD_TENANTNAME_CURRENT'] + '/orchestrator_/odata/Machines',
            headers={'Authorization': f'Bearer {access_token}'}
        )

        # Check for successful API response
        if api_response.status_code == 200:
            machines = api_response.json().get('value', [])
            # Pass the machines data to the render_template function
            return render_template('machines.html', machines=machines)
        else:
            return jsonify({'error': 'Failed to retrieve data from API'}), api_response.status_code
    else:
        return jsonify({'error': 'Authentication failed'}), auth_response.status_code
