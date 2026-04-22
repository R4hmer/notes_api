from app import app
from config import db
from models import User, Note


with app.app_context():
    print("Seeding database...")

    db.drop_all()
    db.create_all()

    user1 = User(username="halima")
    user1.set_password("1234")

    user2 = User(username="testuser")
    user2.set_password("1234")

    db.session.add_all([user1, user2])
    db.session.commit()

    note1 = Note(title="First Note", content="Hello World", user_id=user1.id)
    note2 = Note(title="Second Note", content="Another note", user_id=user1.id)
    note3 = Note(title="Test Note", content="Test content", user_id=user2.id)

    db.session.add_all([note1, note2, note3])
    db.session.commit()

    print("Seeding complete!")