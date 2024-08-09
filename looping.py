print("========================")
print("* Looping *")
print("========================")
# Looping sebanyak 3 kali
for i in range(3):
    print("Looping!")
# angka 5, 10, 15, 20, 25
# start = 5 stop 30 = step = 5
for i in range(5, 30, 5):
    print(i)
print("#======================#")
# Output
# Looping!
# Looping!
# Looping!
# 5
# 10
# 15
# 20
# 25

print("========================")
print("* Break and Continue *")
print("========================")
# Dengan continue statement, kita dapat melewati operasi yang kita lakukan dan langsung lanjut ke iterasi berikutnya.
for i in range(10, 20, 3):
    if i == 13:  # 13 tidak terprint masuk ke continue
        continue
    print(i)
# Output
# 10
# 16
# 19
print("------------------------")
# Print angka ganjil dari 1 sampai 10
for i in range(1, 11):  # jika dia tidak habis dibagi 2
    if i % 2 != 0:
        print(i)
print("#======================#")
# Output
# 1
# 3
# 5
# 7
# 9

print("========================")
print("* While Statement *")
print("========================")
# While statement akan mengesekusi operasi di dalamnya selama kondisinya bernilai True.
uang = 100
while uang > 0:
    print("Masih punya uang: " + str(uang))
    uang -= 10  # uang = uang + str(uang)) 10
print("Uang sudah habis!")
print("#======================#")
# Output
# Masih punya uang: 100
# Masih punya uang: 90
# Masih punya uang: 80
# Masih punya uang: 70
# Masih punya uang: 60
# Masih punya uang: 50
# Masih punya uang: 40
# Masih punya uang: 30
# Masih punya uang: 20
# Masih punya uang: 10
# Uang sudah habis!
