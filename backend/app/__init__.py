from flask import Flask, make_response, jsonify
from .auth import authenticate
app = Flask(__name__)


@app.route('/')
def index():
    return "Send emails"

@app.route('/login')
@authenticate
def login():
    return make_response(jsonify({"Success":"Authentication code is valid"}), 200)


def create_app():
    from .order import order
    app.register_blueprint(order)
    return app
