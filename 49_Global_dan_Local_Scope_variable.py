"""Global dan Local Scope variable
    merk = "samsung" -> disebut sebagai variabel global

    variable local scope :
    
"""
def function():
    local_name = "Apple"
function()
#print(local_name) akan menghasilkan not defined karena hanya bisa di akses pd function
global_variable = "Samsung" #ini global dn bs di akses mn sj
print(global_variable)

"""contoh penggunaan"""
def function1():
    print(f"Merk hp : {Merk}")
Merk = "Vivo"
function1()

"""Contoh selanjutnya : merubah var global"""
number = 15
def number_change(newvalue):
    number = newvalue

print(f"sebelum diubah {number}")
number_change(50)
print(f"sesudah diubah {number}")

"""akan sama karena numbernya itu local jadi belum bs di rbh maka dri itu hrs ksh global
    brkt adalah contohnya
"""
def number_change(newvalue) :
    global number
    number = newvalue
print(f"sebelum diubah {number}")
number_change(50)
print(f"sesudah diubah {number}")

"""Cth lain"""
merk = "samsung"
def merk_change(newmerk) :
    global merk
    merk = newmerk
print(f"sebelum diubah {merk}")
merk_change("Apple")
print(f"sesudah diubah {merk}")

"""Contoh menggunakan for loop"""
number = 0
for i in range(0,5) :
    number += i
    number_dummy = 0
print(number)
print(number_dummy)
if True :
    number = 10
    number_dummy = 10
print(number)
print(number_dummy)

"""kalo global minusnya adalah value dalam
    atau local yang di inisiasi
    ikut berubah datanya
"""