from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
