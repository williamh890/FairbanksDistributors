from flask import Flask

app = Flask(__name__)
from .order import order
app.register_blueprint(order)

@app.route('/')
def index():
    return "Send emails"
