""" *Modul mengambil input data dari user* """

data = input("Masukkan data: ")
""" seperti printf dan scanf namun data yang diambil dari inputan user
merupakan tipe data string event yang dimasukkan user itu angka.
jika ingin mengambil data selain str, maka
Disinilah peran casting diperlukan """
print("data = ", data, "tipe data = ", type(data))

"""mengambil data user selain str dengan casting"""
data_float = float(input("masukkan angka float: "))
print("data = ", data_float, "tipe data = ", type(data_float))

data_int = int(input("masukkan angka int: "))
print("data = ", data_int, "tipe data = ", type(data_int))

data_boolean = bool(int(input("Masukkan angka antara 1 atau 0 utk boolean: ")))
print("data = ", data_boolean, "tipe data = ", data_boolean)
