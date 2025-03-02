""" Modul Looping List and Enumerate """
""" Looping dari list
    for loop
"""
data = [1,2,3,4,5,6]
for i in data :
    print(f"angka {i}")
merk = ["vivo","samsung","apple"]
for i in merk :
    print(f"merk : {i}")

print("\nfor loop dan range")
kumpulan_data = [5,4,7,8,9,5,45,2]
pjg = len(kumpulan_data)
for i in range(pjg) :
    print(f"angka = {kumpulan_data[i]}")

"""while"""
print("\n while loop")
kumpulan_data = [5,4,7,8,9,5,45,2]
pjg = len(kumpulan_data)
i = 0
while i < pjg :
    print(f"data = {kumpulan_data[i]}")
    i += 1

"""List comprehension"""
print("List comprehension")
data = ["samsung", "oppo", "vivo"]
[print(f"data = {i}")for i in data]

data_kuadrat = [5,4,7,8,9,5,45,2]
angka_kuadrat = [i**2 for i in data_kuadrat]
print(angka_kuadrat)

"""Enumerate"""
print("Enumerate")
data = ["samsung", "oppo", "vivo"]
for index,dataa in enumerate(data) :
    print(f"index = {index}, data = {data}")

"""ketika menggunakan enumerate bisa menghilangkan
    for loop dan range
"""