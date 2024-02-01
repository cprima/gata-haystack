from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from uipath import create_app

app = create_app()

if __name__ == '__main__':
    print(app)
    app.run(host='0.0.0.0')
    app.run(debug=True)
