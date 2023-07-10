import requests
from flask import Flask

app = Flask(__name__)

STORAGE_SERVICE_URL = 'http://storage:5000'


@app.route('/help')
def help():
    storage_help_response = requests.get(f"{STORAGE_SERVICE_URL}/help")
    return f"Auth: Hi! There, I am Auth\nStorage: {storage_help_response.text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
