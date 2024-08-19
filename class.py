print("========================")
print("* Class *")
print("========================")


class Angka:
    jumlah = 8


a = Angka()
print(a.jumlah)
b = Angka()
print(b.jumlah)
# Output
# 8
# 8

print("========================")
print("* Class Object - 1 *")
print("========================")


class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


p1 = Person("Selly", 20, 95)
p2 = Person("Ahyeon", 25, 80)

print(p1.__dict__)
print(p2.__dict__)
# Output
# {'name': 'Selly', 'age': 20, 'score': 95}
# {'name': 'Ahyeon', 'age': 25, 'score': 80}

print("========================")
print("* Class Object - 2 *")
print("========================")


class Animal:  # Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!")


class Cat(Animal):  # Child Class
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight


class Dog(Animal):  # Child Class
    def __init__(self, name, age, types):
        super().__init__(name, age)
        self.color = types
