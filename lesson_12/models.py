import logging

from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from lesson_13.services import create_user
from lesson_13.utils import create_tables

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_USER = "manti"
DB_PASSWORD = "manti"
DB_NAME = "manti"


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)

    menu = """
        1. Создать пользователя
        2. Найти пользователя
        3. Выйти
        """

    while True:
        logger.info(menu)
        print()
        choice = input("Выберите функцию: ")

        if choice == "1":
            email = input("Введите email: ")
            password = input("Введите пароль: ")

            user = create_user(session, email, password)
            logger.info(f"Пользователь #{user.id} создан")
        elif choice == "3":
            exit()