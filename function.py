print("========================")
print("* Function - Example 1 *")
print("========================")


def greet():
    print("Hello Stranger")


greet()
# Output
# Hello Stranger

print("========================")
print("* Function - Example 2 *")
print("========================")


def greet(name):
    print("Hello Stranger" + name)
    print("Hello Stranger" + name)


greet("Arthur")
# Output
# Arthur

print("========================")
print("* Function - Example 3 *")
print("========================")


def greet(name, age):
    print("Name: " + name)
    print("Age: " + str(age))


greet("Arthur", 18)
# Output
# Name: Arthur
# Age: 18
print("========================")
print("* Function - Example 4 *")
print("========================")
greet(name="Arthur", age=18)
# Output
# Name: Arthur
# Age: 18
print("========================")
print("* Function - Example 5 *")
print("========================")


def add5(number):
    total = number + 5
    return total


number = 10
number_added_5 = add5(number)
print(number_added_5)
# Output
# 15
print("========================")
print("* Lambda Function *")
print("========================")
number = 10
total = lambda n: n + 5
print(total(number))


# Output
# 15
