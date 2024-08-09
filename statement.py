print("========================")
print("* Conditional Statement 1 *")
print("========================")
x = 5
y = 10
z = 15
print(not (x > y))
print(x < y)
print(x < y and y > z)
print(x < y or y > z)
# x < y = 5 < 10 = True (Statement 1)
# y > z = 10 > 15 = False (Statement 2)
# Statement 1 and Statement 2 = True and False = False
# Statement 1 or Statement 2 = True or False = True
print("#======================#")
# Output
# True
# True
# False
# True

print("========================")
print("* Conditional Statement 2 *")
print("========================")
x = 10
y = 15
# Contoh 1
if x == y:  # False
    print("X sama dengan Y")
if x < y:  # True
    print("X kurang dari Y")
# Contoh 2
a = 10
b = 15
c = 20
if a > b:
    print("A lebih besar dari B")
else:
    print("A tidak lebih besar dari B")
print("#======================#")
# Output
# X kurang dari Y
# A tidak lebih besar dari B

print("========================")
print("* Conditional Statement 3 *")
print("========================")
a = 10
b = 5
if a > b:
    print("A lebih besar dari B")
elif a == b:
    print("A sama dengan B")
else:
    print("B lebih besar dari A")
print("#======================#")
# Output
# A lebih besar dari B