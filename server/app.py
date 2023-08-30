#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/') #Routing: the association of URLS
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


