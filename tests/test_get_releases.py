import pytest
import requests_mock
import json
from app import create_app  # Adjust the import according to your app structure

@pytest.fixture
def app_client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Providing app context to the test
        with app.app_context():
            yield client, app

def test_get_uipath_releases(app_client):
    client, app = app_client  # Unpack the client and app objects

    with open('tests/mock_responses/cprimadotnet/Releases_response.json') as f:
        mock_response = json.load(f)

    with requests_mock.Mocker() as m:
        # Mock the OAuth2 token endpoint
        m.post('https://cloud.uipath.com/identity_/connect/token', json={'access_token': 'mocked_access_token'})

        # Mock the API call
        m.get('https://cloud.uipath.com/cprimadotnet/homelab23/orchestrator_/odata/Releases', json=mock_response)
        
        response = client.get('/uipath/get-releases')

        assert response.status_code == 200
        # Additional assertions based on your mock response
