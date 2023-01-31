"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки,
методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

from lesson_09.library.figures import Point, Circle, Triangle, Square


if __name__ == "__main__":
    a = Point(3, 7)
    circle = Circle(a, 3)

    a = Point(3, 7)
    b = Point(5, 2)
    square = Square(a, b)

    a = Point(1, 1)
    b = Point(7, 2)
    c = Point(5, 5)
    triangle = Triangle(a, b, c)

    for figure in [circle, square, triangle]:
        print(figure.__class__.__name__, figure.perimeter(), figure.area())