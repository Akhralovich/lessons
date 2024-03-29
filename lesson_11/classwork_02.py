"""
Создать функцию для поиска всех пользователей с определенным именем.
Запустить функцию и найти хотя бы одного пользователя по имени.
"""

import sqlite3


def select_user_by_name(name: str) -> list:
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (name,)
        )
        session.commit()
        return cursor.fetchall()


def select_user_by_age(from_age: int, to_age: int) -> list:
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age >= ? AND  age <= ?;
            """,
            (from_age, to_age)
        )
        session.commit()
        return cursor.fetchall()


def main():
    while True:
        choice = input("Выполнить поиск по возрасту [1] или имени [2]:")
        if choice == "1":
            start = input("Введите минимальный возраст:")
            stop = input("Введите максимальный возраст:")
            print(select_user_by_age(int(start), int(stop)))
        elif choice == "2":
            search = input("Введите имя:")
            print(select_user_by_name(search))
        else:
            return print("Пока!")


if __name__ == "__main__":
    main()