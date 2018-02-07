from flask_api import FlaskAPI, status
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from queries.pyns import get_all_pyns as get_all_pyns_query 
from queries.pyns import get_pyn_by_id as get_pyn_by_id_query 
from queries.pyns import get_pyns_by_user_id as get_pyns_by_user_id_query 
import json, os

app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['PYN_PG_CONNECTION_URI']
db = SQLAlchemy(app)
CORS(app)
auth = HTTPBasicAuth()
version = 'v1.0'

pyns = json.loads(open('mockdata/mockdata.json').read())
secretData = json.loads(open('mockdata/mocksecretdata.json').read())

USERDATA = {'admin': 'password'}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USERDATA.get(username) == password


@app.route('/')
def index():
    test.test_func()
    return users, status.HTTP_200_OK


@app.route('/secret')
@auth.login_required
def secretIndex():
    return secretData, status.HTTP_200_OK

@app.route('/pynterest/api/'+version+'/pyns', methods=['GET'])
@auth.login_required
def get_all_pyns():
    return get_all_pyns_query()

@app.route('/pynterest/api/'+version+'/pyns/<pyn_id>', methods=['GET'])
@auth.login_required
def get_pyns(pyn_id):
    return get_pyn_by_id_query(id)

@app.route('/pynterest/api/'+version+'/pyns/user/<user_id>', methods=['GET'])
@auth.login_required
def get_user_pyns(user_id):
    return get_pyns_by_user_id_query(id)

if __name__ == '__main__':
    app.run()