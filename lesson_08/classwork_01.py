"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Добавить конструктор класса и инициализировать атрибуты класса значениями переменных.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""
from lesson_08.library.cat import Cat
from lesson_08.library.dog import Dog


if __name__ == "__main__":
    dog = Dog(100, 50, "My Dog", 10)
    dog.bark()

    dog.change_name(name="New Name")
    dog.bark()

    cat = Cat(100, 50, "My Cat", 10)
    cat.meow()