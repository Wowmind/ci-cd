from flask import flask

app = Flask(__name__)

@app.route('/')
def hello();
    return 'My Default Application'
