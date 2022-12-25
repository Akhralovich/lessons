#Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
#Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево

stroka = input(str("Введите строку "))
my_list = []
new_list = []
for i in stroka:
    if i != " ":
        my_list.append(i)
print(my_list)
new_list = list(reversed(my_list))
print(new_list)
if my_list == new_list:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")


