class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(self):
        print(f'Привет меня зовут {self.name}, мне {self.age} лет')


p1 = Person("Василий", 36)
p1.myfunc()

