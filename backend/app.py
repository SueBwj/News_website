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
def SummaryResponseToRightSide():
    summary, content, comment = summarization_fun()
    return jsonify({
        'status': 'success',
        'summary': summary,
        'content': content,
        "comment": comment
    })


if __name__ == '__main__':
    app.run()
