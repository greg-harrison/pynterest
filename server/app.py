from flask_api import FlaskAPI, status
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json, os

app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['PYN_PG_CONNECTION_URI']
db = SQLAlchemy(app)
CORS(app)
auth = HTTPBasicAuth()
version = 'v1.0'

users = json.loads(open('mockdata.json').read())
secretData = json.loads(open('mocksecretdata.json').read())

pyns = [
    {
        "pyn_id": 'b93bfdcd-3507-40d6-9778-71d008197b9d',
        "user_id": '226f454e-0383-43e0-9c2f-776f0332014e',
        "title": "Test",
        "url": "http://www.testing.org",
        "description": "A test",
    },
    {
        "pyn_id": '82ffb50c-9b9b-4275-a4b4-5d7a917a31f6',
        "user_id": '226f454e-0383-43e0-9c2f-776f0332014e',
        "title": "Test",
        "url": "http://www.testing.org",
        "description": "A test",
    },
    {
        "pyn_id": '47b24256-4423-4ab8-90bd-464d28c10aa9',
        "user_id": '226f454e-0383-43e0-9c2f-776f0332014e',
        "title": "Test",
        "url": "http://www.testing.org",
        "description": "A test",
    }
]

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

@app.route('/pynterest/api/'+version+'/pyns', methods=['GET'])
@auth.login_required
def get_pyns():
    return pyns, status.HTTP_200_OK 

@app.route('/pynterest/api/'+version+'/pyns/<pyn_id>', methods=['GET'])
@auth.login_required
def get_pyns(pyn_id):
    if pyn_id:
        pyn = [pyn for pyn in pyns if pyn['pyn_id'] == pyn_id]
        if len(pyn) == 0:
            return status.HTTP_404_NOT_FOUND
        return pyn[0], status.HTTP_200_OK 
    else: 
        return pyns, status.HTTP_200_OK

if __name__ == '__main__':
    app.run()