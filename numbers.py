print("========================")
print("* Penjumlahan *")
print("========================")
angka = 5
print("Angka sebelum ditambah: " + str(angka))

# Cara 1
angka = angka + 5
print("Angka setelah ditambah: " + str(angka))

# Cara 2
angka += 5
print("Angka setelah ditambah: " + str(angka))
print("#======================#")
# Output
# Angka sebelum ditambah: 5
# Angka setelah ditambah: 10
# Angka setelah ditambah: 15

print("========================")
print("* Pembagian *")
print("========================")
angka1 = 8
angka2 = 3

print(angka1 / angka2)
print(angka1 // angka2)  # pembulatan kedepan
print("#======================#")
# Output
# 2.6666666666666665
# 2

print("========================")
print("* Function Math *")
print("========================")
import math

# Using methods
print(math.pow(2, 3))
print(math.ceil(3.2))
print(math.sqrt(25))  # float
# Using constants
print(math.pi)
print("#======================#")
# Output
# 8.0
# 4
# 5.0
# 3.141592653589793

print("========================")
print("* String *")
print("========================")
text = "coding studio"
print(text.upper())
print(text.lower())
print(len(text))
print(text.split())
print(text.capitalize())
print(text.index("s"))
print("#======================#")
# Output
# CODING STUDIO
# coding studio
# 13
# ['coding', 'studio']
# Coding studio
# 7

print("========================")
print("* String Concatenation *")
print("========================")
# Untuk menggabungkan dua buah string, kita dapat
# menggunakan syntax +

x = "Coding"
y = "Studio"
print(x + y)
print(x + " " + y)
print(x + " " + y + " " + str(100))
print("#======================#")
# Output
# CodingStudio
# Coding Studio
# Coding Studio 100

print("========================")
print("* String Format *")
print("========================")
# print("Bakal terjadi error " + 1)
print("Tidak ada error " + str(1))  # gunakan str() untuk print integer
nama = "Cecер"
umur = 20
text = "{} berumur {} tahun."
print(text.format(nama, umur))
print("#======================#")
# Output
# Tidak ada error 1
# Cecер berumur 20 tahun.
print("========================")
print("* In Vs. Not In *")
print("========================")
# Kita dapat memeriksa apakah sebuah substring terdapat dalam sebuah string.
text = "Coding Studio"
print("Studio" in text)  # True
print("Code" in text)  # False
print("#======================#")
# Output
# True
# False
