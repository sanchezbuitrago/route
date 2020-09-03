import os

from models import db
from routes import app

project_dir = os.path.dirname(os.path.abspath(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:changeme@localhost:5432/route'
db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
