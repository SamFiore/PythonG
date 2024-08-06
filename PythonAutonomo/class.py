class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

name = input("Enter your name: ")
age = input("Enter your age: ")

p2 = Person(name, age)

print(p2.name)
print(p2.age)

class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass

p3 = Person2("Alex", 99)
del p3
print(p3.name)

