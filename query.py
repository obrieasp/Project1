from app import create_app, db
from app.models import User
app = create_app()

with app.app_context():
    db.create_all()

    users = db.session.query(User).all()
    for user in users:
        print(user.id, user.name, user.email)

    new_user = User(name='John Doe', email='john.doe@example.com')
    db.session.add(new_user)
    db.session.commit()

    print(f'Added new user: {new_user.name} ({new_user.email})')