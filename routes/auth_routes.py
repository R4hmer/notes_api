from flask import request, session, jsonify
from models import User
from config import db


def register_auth_routes(app):

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Missing fields"}, 400

        if User.query.filter_by(username=username).first():
            return {"error": "Username already exists"}, 400

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return {"id": user.id, "username": user.username}, 201


    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            return {"id": user.id, "username": user.username}, 200

        return {"error": "Invalid credentials"}, 401


    @app.route('/me', methods=['GET'])
    def me():
        user_id = session.get('user_id')

        if not user_id:
            return {"error": "Unauthorized"}, 401

        user = User.query.get(user_id)

        return {"id": user.id, "username": user.username}, 200


    @app.route('/logout', methods=['DELETE'])
    def logout():
        session.pop('user_id', None)
        return {}, 204