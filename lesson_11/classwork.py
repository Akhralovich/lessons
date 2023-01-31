import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


def select_user(firstname: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (firstname,)
        )
        session.commit()
        return cursor.fetchone()


if __name__ == "__main__":
    # create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    # create_user("Roma", "Chaika", "manti.by+1@gmail.com", "Pass", 22)
    # create_user("Dima", "Chaika", "manti.by+2@gmail.com", "Test", 34)

    result = select_user("Roma")
    logger.info(result)