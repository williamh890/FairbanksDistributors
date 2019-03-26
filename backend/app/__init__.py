from flask import Flask, make_response, jsonify
from .auth import authenticate
app = Flask(__name__)


@app.route('/')
def index():
    return "Send emails"


def create_app():
    from .order import order
    app.register_blueprint(order)
    return app
