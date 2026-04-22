from flask import Flask
from config import db, migrate, bcrypt
from models import User, Note
from routes.auth_routes import register_auth_routes
from routes.note_routes import register_note_routes


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    register_auth_routes(app)
    register_note_routes(app)


    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)