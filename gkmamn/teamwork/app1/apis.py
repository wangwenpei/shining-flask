from flask import Blueprint

api = Blueprint('teamwork.app1', __name__)


@api.route('/')
def hello():
    return 'I am app1!'
