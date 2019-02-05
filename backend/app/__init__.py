from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Send emails"

def create_app():
    from .order import order
    app.register_blueprint(order)
    return app
