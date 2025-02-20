#!/usr/bin/python3
"""task_04_flask.py"""
import flask


app = flask.Flask(__name__)

@app.route('/')
def home():
    return f"Welcome to the Flask API!"


if __name__ == "__main__":
    app.run()