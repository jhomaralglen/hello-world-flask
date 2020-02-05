import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to python!"

@app.route('/hello-world')
def hello():
    return 'Hello world!'

if __name__ == "__main__":
    app.run()
