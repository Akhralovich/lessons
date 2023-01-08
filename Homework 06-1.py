
text = input("Введите текст ")
list_text = text.split(' ')
dlin_slovo = max(list_text, key=len)
print(f"Самое длинное слово - {dlin_slovo}")




