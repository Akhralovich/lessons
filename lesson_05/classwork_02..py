"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и
возвращает их сумму и максимальное из них.
"""


def sum_and_max(*args):
    my_sum = 0
    my_max = args[0]
    for element in args:
        my_sum += element
        if element > my_max:
            my_max = element
    return my_sum, my_max


def sum_and_max_2(*args):
    return sum(args), min(args)


sum_and_max(1, 2, 3)
sum_and_max(1, 2, 3, 4, 5, 6)
sum_and_max(1, 2, 3, -5)