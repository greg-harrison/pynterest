from flask_api import FlaskAPI, status
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import json

app = FlaskAPI(__name__)
CORS(app)
auth = HTTPBasicAuth()

users = json.loads(open('mockdata.json').read())
secretData = json.loads(open('mocksecretdata.json').read())

USERDATA = {'admin': 'password'}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USERDATA.get(username) == password


@app.route('/')
def index():
    return users, status.HTTP_200_OK


@app.route('/secret')
@auth.login_required
def secretIndex():
    return secretData, status.HTTP_200_OK


if __name__ == '__main__':
    app.run()