from flask import Flask, request, jsonify

app = Flask(__name__)

test = {
    0: 'hello',
    1: 'world',
    2: 'test',
}

@app.route('/')
def index():
    response = jsonify(test)
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run()