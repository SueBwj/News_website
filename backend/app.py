from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import key_param
from source.summarization_v2 import summarization_fun

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    summary, content, comment = summarization_fun()
    return jsonify([summary, content, comment])


if __name__ == '__main__':
    app.run()
