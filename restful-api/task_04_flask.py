#!/usr/bin/python3
"""task_04_flask.py"""
import flask
from flask import jsonify, request


app = flask.Flask(__name__)
users_dict = {}


@app.route('/')
def home():
    """Simple Home message"""

    return f"Welcome to the Flask API!"


@app.route('/status')
def status():
    """Simple message status"""

    return f"OK"


@app.route('/data')
def my_data():
    """Get all the users from user_dict"""

    return jsonify(list(users_dict.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Get a specific user"""

    if username not in users_dict:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users_dict[username]), 200


@app.route('/add_user', methods=["POST"])
def add_user():
    """POST a new user"""

    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    users_dict[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({
        'message': "User added", "user": users_dict[username]
    }), 201


if __name__ == "__main__":
    app.run()
