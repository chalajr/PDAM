from flask import Flask, jsonify

app = Flask(__name__)


tasks = [
    {
        'task_name': 'task 1', 'owner': 'Patricio'
    },
    {
        'task_name': 'task 2', 'owner': 'Pedro'
    }
]


@app.route("/hello/", methods=['GET'])
def hello_world():
    return jsonify({'task': tasks})
