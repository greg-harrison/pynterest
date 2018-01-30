from flask_api import FlaskAPI, status
from flask_cors import CORS
import json

app = FlaskAPI(__name__)
CORS(app)

users = json.loads(open('mockdata.json').read())

@app.route('/')
def index():
    return users, status.HTTP_200_OK


if __name__ == '__main__':
    app.run()