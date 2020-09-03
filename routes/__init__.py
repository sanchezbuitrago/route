from flask import Flask
from routes.users import users_routes


app = Flask(__name__)
app.register_blueprint(users_routes, url_prefix="/users")
