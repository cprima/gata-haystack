# Project Gata Haystack

## Requirements

- Python virtualenv, e.g. `python -m venv O:\venv\flask-jinja2-authlib`
- (in WSL) `make setup`
- .env file with `DEVELOPMENT_UIPATH_CLIENT_ID="12345678-1234-5678-1234-567812345678"
DEVELOPMENT_UIPATH_CLIENT_SECRET="s3cr3t#123456789"`
- (in WSL) make run

```bash
$  make run
Activating virtual environment...
source /path/to/venv/flask-jinja2-authlib/Scripts/activate && /path/zo/venv/flask-jinja2-authlib/Scripts/python.exe app.py
<Flask 'app'>
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.47.11.42:5000
Press CTRL+C to quit
 * Restarting with stat
<Flask 'app'>
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

## Code Structure

This Flask project is structured to promote readability, maintainability, and separation of concerns, making it scalable for future development. Below is an overview of the key components and their roles in the application:

### Root Directory

- `app.py`: The entry point of the Flask application. It creates and configures the Flask app instance.
- `config.py`: Contains the configuration classes for different environments (development, production), utilizing environment variables for sensitive data.
- `.env`: A file to store environment variables (not tracked in version control for security reasons).
- `requirements.txt`: Lists all the Python dependencies that need to be installed.

### `app/` Directory

This directory contains the main package of the Flask application and is further divided into subdirectories and files:

- `__init__.py`: Initializes the Flask app and brings together different components like routes, configurations, etc.
- `routes.py`: Defines all the routes (URLs) of the application, including the logic for each route.

#### `templates/` Subdirectory

- Contains Jinja2 templates for rendering HTML. These templates are used by the view functions in `routes.py` to present data to users in a web browser.

#### `static/` Subdirectory

- Houses static files like CSS, JavaScript, and images. This is where you would store your `favicon.ico` and any other static assets your application uses.

#### `middleware/` Subdirectory

- The middleware/ subdirectory is an integral part of the application, housing the middleware components. Middleware in a Flask application acts as an intermediary layer that can process requests before they reach the route handlers and responses before they are sent back to the client. This directory includes implementations for various middleware functionalities that enhance the application's capabilities.

### Configuration Management

- The application uses `python-dotenv` to load environment variables from the `.env` file. This allows us to keep sensitive information like API keys and secrets out of the source code.
- `config.py` defines different configuration classes for various environments (like `DevelopmentConfig` and `ProductionConfig`). These classes inherit from a base `Config` class and override specific settings as needed.

### APIs and External Services

- The application is set up to interact with external APIs (like UiPath and Spotify), authenticated via OAuth2. Configuration for these APIs, including client IDs and secrets, are managed through environment variables and are loaded in `config.py`.
- The `routes.py` file contains routes that handle interactions with these external services, abstracting the API logic from the main application flow.
