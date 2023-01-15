""
Найти в списке ниже количество не уникальных элементов:
"""
from math import sqrt

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
my_set = set(my_list)

print(len(my_list) - len(my_set))

"""
Взять список из предыдущей задачи, извлечь элементы со 2-го по 4-й включительно и вывести их в обратном порядке.
"""

my_slice = my_list[2:5]
print(my_slice[::-1])


"""
Создать переменную содержащую сторону квадрата, создать новый список,
в котором будут периметр квадрата, площадь квадрата и диагональ квадрата.
"""

square_size = 12
new_list = [square_size * 4, square_size ** 2, sqrt(2 * square_size ** 2)]
print(new_list)