from flask import Blueprint
from models import db
from models.users import User

users_routes = Blueprint('users', __name__)


@users_routes.route('/', methods=["GET"])
def hello_world():
    user = User('admin', 'admin@example.com')
    db.session.add(user)
    db.session.commit()
    return 'Hello, World!!!!!!!!!!!!!!!!!!!!!'
