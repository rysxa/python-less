print("========================")
print("* Read File *")
print("========================")
file = open("example.txt", "r")

print(file.read())

print("========================")
print("* Write File *")
print("========================")
file = open("example.txt", "w")

file.write("Ini adalah text yang baru")
file.close()

print("========================")
print("* Append File *")
print("========================")
file = open("example.txt", "a")

file.write("Ini adalah text yang baru")
file.append("\n Ini adalah text yang baru di append")
file.close()
