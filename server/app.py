from flask_api import FlaskAPI, status
import json

app = FlaskAPI(__name__)

users = json.loads(open('mockdata.json').read())

@app.route('/')
def index():
    return users, status.HTTP_200_OK


if __name__ == '__main__':
    app.run()