DB_USER = "lexa"
DB_PASSWORD = "lexa"
DB_NAME = "lexa"

if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user = User(email="test@test.com", password="password")
session.add(user)

session.commit()