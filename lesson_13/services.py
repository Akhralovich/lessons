from lesson_13.models import User


def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user