import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

ase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test@test.com", password="password")
    session.add(user)

    session.commit()

    address = Address(user_id=user.id, city="Minsk", address="Test")
    session.add(address)

    profile = Profile(user_id=user.id, phone="+375292999999", age=20)
    session.add(profile)

    user = session.query(User).filter(User.email == "test@test.com").first()
    user.password = "new_password"
    session.add(user)
    session.commit()