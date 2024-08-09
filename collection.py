print("========================")
print("* Python Collection Data Types 1 *")
print("========================")
# List adalah sebuah koleksi yang terurut dan dapat diganti.
# List bisa menampung elemen yang duplikat

# append, insert
listExample = [42, "Python", 3.85, 50]
listExample.insert(1, "Data Science")  # memasukan data di index ke 1
listExample.append("Javascript")  # memasukan data dipaling akhir
print(listExample)
# Output
# [42, 'Data Science', 'Python', 3.85, 50, 'Javascript']
print("#======================#")

# remove, pop, del, clear
# jalankan satu persatu
listExample = [42, "Python", 3.85, 50]
print(listExample)
del listExample[2]  # delete spesifik index keberapa
# Output
# [42, 'Python', 3.85, 50]
# [42, 'Python', 50]
listExample.pop()  # delete data terakhir
# Output
# [42, 'Python', 3.85, 50]
# [42, 'Python', 3.85]
listExample.clear()  # delete semua data
# Output
# [42, 'Python', 3.85, 50]
# []
print(listExample)
print("#======================#")

# list iteration
listExample = [40, 55, 20, 75, 80]
for item in listExample:
    if item % 2 == 0:
        print(item)
# Output
# 40
# 20
# 80
print("#======================#")

# check if an item exists in list
listExample = [40, 55, 20, 75, 80]
if 40 in listExample:
    print("Terdapat angka 40 di dalam listExample")
# Output
# Terdapat angka 40 di dalam listExample
print("#======================#")

# methods: len, copy, concat (+ dan extend), index, sort, reverse
listExample = [40, 55, 20, 75, 80]
length = len(listExample)
print(length)
# Output
# 5
print("+++++++++++++++++++++++")

listExample = [40, 55, 20, 75, 80]
listExample2 = listExample.copy()  # variable/entity baru yang berbeda
listExample2[0] = 100
print(listExample)
print(listExample2)
# Output
# [40, 55, 20, 75, 80]
# [100, 55, 20, 75, 80]
print("+++++++++++++++++++++++")
listExample = [40, 55, 20]
listExample2 = [70, 100]
print(listExample + listExample2)
# Output
# [40, 55, 20, 70, 100]
listExample.extend(listExample2)
print(listExample)
# Output
# [40, 55, 20, 70, 100]

print("+++++++++++++++++++++++")
listExample = [40, 55, 20]
listExample.sort()
print(listExample)
# Output
# [20, 40, 55]

print("+++++++++++++++++++++++")
listExample = [40, 55, 20]
listExample.reverse()
print(listExample)
# Output
# [20, 55, 40]
print("#======================#")

print("========================")
print("* Python Collection Data Types 2 *")
print("========================")
# Tuple
tupleExample = ("Python", 20, 3.8, True, 20)
print(tupleExample)
# Output
# ('Python', 20, 3.8, True, 20)
print("#======================#")

customer = {"nama": "Cecep", "umur": 30}
print(customer)
# Output
# {'nama': 'Cecep', 'umur': 30}
print("#======================#")

customer["nama"] = "Dodi"
# print(customer)
print(customer["nama"])
print(customer["umur"])
# Output
# Dodi
# 30
print("#======================#")

numbers1 = {1, 3, 5, 4, 10}
numbers2 = {3, 4, 10, 7, 8}
numbers_union = numbers1.union(numbers2)
print(numbers_union)
# Output
# {1, 3, 4, 5, 7, 8, 10}

difference1 = numbers1.difference(numbers2)
print(difference1)
# Output
# {1, 5}

intersect = numbers1.intersection(numbers2)
print(intersect)
# Output
# {10, 3, 4}

sym_difference = numbers1.symmetric_difference(numbers2)
print(sym_difference)
# Output
# {1, 5, 7, 8}
