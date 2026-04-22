from flask import request, session
from models import Note, User
from config import db


def register_note_routes(app):

    def get_current_user():
        user_id = session.get('user_id')
        if not user_id:
            return None
        return User.query.get(user_id)

    @app.route('/notes', methods=['POST'])
    def create_note():
        user = get_current_user()
        if not user:
            return {"error": "Unauthorized"}, 401

        data = request.get_json()

        note = Note(
            title=data.get('title'),
            content=data.get('content'),
            user_id=user.id
        )

        db.session.add(note)
        db.session.commit()

        return {
            "id": note.id,
            "title": note.title,
            "content": note.content
        }, 201

    @app.route('/notes', methods=['GET'])
    def get_notes():
        user = get_current_user()
        if not user:
            return {"error": "Unauthorized"}, 401

        page = request.args.get('page', 1, type=int)

        notes = Note.query.filter_by(user_id=user.id).paginate(
            page=page,
            per_page=5,
            error_out=False
        )

        return {
            "notes": [
                {
                    "id": n.id,
                    "title": n.title,
                    "content": n.content
                } for n in notes.items
            ],
            "total": notes.total,
            "pages": notes.pages,
            "current_page": page
        }, 200

    @app.route('/notes/<int:note_id>', methods=['PATCH'])
    def update_note(note_id):
        user = get_current_user()
        if not user:
            return {"error": "Unauthorized"}, 401

        note = Note.query.get(note_id)

        if not note or note.user_id != user.id:
            return {"error": "Forbidden"}, 403

        data = request.get_json()

        note.title = data.get('title', note.title)
        note.content = data.get('content', note.content)

        db.session.commit()

        return {
            "id": note.id,
            "title": note.title,
            "content": note.content
        }, 200

    @app.route('/notes/<int:note_id>', methods=['DELETE'])
    def delete_note(note_id):
        user = get_current_user()
        if not user:
            return {"error": "Unauthorized"}, 401

        note = Note.query.get(note_id)

        if not note or note.user_id != user.id:
            return {"error": "Forbidden"}, 403

        db.session.delete(note)
        db.session.commit()

        return {}, 204