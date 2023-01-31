"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""
from lesson_09.library.my_time import MyTime

if __name__ == "__main__":
    time1 = MyTime(12, 12, 12)
    time2 = MyTime(1, 17, 34)
    print(time1 == time2)
    print(time1 + time2)
    print(time1 * 2)
    print(time1 - time2 + MyTime(7, 45, 0))