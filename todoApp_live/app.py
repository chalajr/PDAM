from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

tasks = [

]
######## DataBase Functionality   ###########
# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), nullable=False)
    owner = db.Column(db.String(250), nullable=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)


if not os.path.isfile('sqlite:///todo.db'):
    db.create_all()


@app.route("/", methods=['GET'])
def hello_world():
    return "Hello world!"


@app.route("/tasks", methods=['GET'])
def getTasks():
    all_task = db.session.query(Task).all()
    for task in all_task:

        temp_task = {
            'task_name': task.task_name,
            'owner': task.owner,
            'complete': task.complete,
        }

        tasks.append(temp_task)

    return jsonify({'task': tasks})

# POST Method to add info to the array


@app.route('/addTasks', methods=['POST'])
def add_new_tasks():
    if not request is None:
        new_task = Task(
            task_name=request.json['task_name'],
            owner=request.json['owner']
        )

        db.session.add(new_task)
        db.session.commit()

        # tasks.append(new_task)
        return "Sucess. Record created in the database"
    else:
        return "Error, Request is empty"
    return request.json
