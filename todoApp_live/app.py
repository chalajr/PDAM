from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

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


if not os.path.isfile('sqlite:///todo.db'):
    db.create_all()


@app.route("/hello", methods=['GET'])
def hello_world():
    return "Hello world!"


@app.route("/tasks", methods=['GET'])
def getTasks():
    return jsonify({'task': tasks})


@app.route("/addTask", methods=['POST'])
def addTasks():
    return 0
