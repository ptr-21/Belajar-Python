""" Modul Perulangan Looping dengan for loop """
""" misalkan nilai yang diminta minimal adalah 5
    maka caranya adalah :
"""
print("perulangan tidak menggunakan for")
val = 1
print(val)
val = val + 1
print(val)
val = val + 1
print(val)
val = val + 1
print(val)
val = val + 1
print(val)
print()

""" kalo cuma 5 masih mudah, bagaimana jika harus 50?
    akan ribet bukan? maka dari itu perlu pemanggilan for agar 
    efisien dan tidak perlu copy paste sebanyak 50.
    berikut adalah kodenya :
"""
""" untuk semua i di dalam range 50"""
print("perulangan menggunakan for")
for i in range (50) :
    """ ujung tidak diambil krn batas akhir tidak diikutkan """
    print(i)
print()


""" contoh lain dengan menggunakan list / array"""
print("data list")
data_array = [0, 1, 2, 3, 4, 5]
for i in data_array:
    print(i)
print()

""" contoh mengulangi teks """
for i in range (10):
    print("I love Python")

""" Penjelasan :
    alur kode ini adalah mengecek kondisi, misal data_array = [0, 1, 2, 3, 4, 5]
    maka dia akan mengecek apakah perulangan telah mencapai batas akhir yaitu
    pada kode in data_array
    jika sudah melebihi maka dia akan berhenti yg analoginya spt false lalu
    tidak menghasilkan apa apa
"""