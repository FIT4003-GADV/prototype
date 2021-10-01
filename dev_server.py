"""
Spins up a Flask HTTP server to serve requests for alt-text generation (for development purposes).
"""
from absl import app
from flask import Flask
from flask import jsonify
from flask import request

from base_workflow import BaseWorkflow

PORT = 5001

flask_app = Flask(__name__)


@flask_app.route('/', methods=['GET'])
def welcome():
    """
    Welcome route.
    """
    return 'You have reached the dev server...'


@flask_app.route('/generate', methods=['POST'])
def generate():
    """
    Executes the BaseWorkflow from the provided svg string in the POST request's body.
    The body should be JSON-formatted with an "svg" property and the raw svg string as the value.
    Example: {
                "svg": "<svg>...</svg>"
             }
    :return: the output alt-text as a json list.
    """
    content = request.json
    assert 'svg' in content

    bw = BaseWorkflow(content['svg'])
    alt_text = bw.execute()
    print(alt_text)

    return jsonify({'alt_text': alt_text})


def main(argv):
    del argv

    flask_app.run(debug=True, port=PORT)


if __name__ == '__main__':
    app.run(main)
