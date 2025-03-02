"""Modul Copy List
    -> menduplikat list dengan copy list
"""
a = ["kocak", 'geming', 'ggwp']
b = a
"""itu bukan copy tapi pass by reference"""
print(f"data a = {a}")
print(f"data b = {b}")
b.sort()
print(f"data a = {a}")
print(f"data b = {b}")
"""yang jadi masalah adalah b dan a saling berkaitan
    mengapa demikian? karena si b refrence ke a.
    Jika ingin tau kita bisa cek address nya a dan b
"""
print(f"alamat memory dari a = {hex(id(a))}")
print(f"alamat memory dari b = {hex(id(b))}")

"""solusi dari ini semua adalah dengan cara mengcopy yaitu :"""
c = a.copy()
print(f"alamat memory dari c = {hex(id(c))}")

"""ketika memori sama maka akan menggunakan list yang sama
    saling berhubungan karena menggunakan 1 list.
    ketika menggunakan .copy akan membuat list baru dan menggunakan memory
    lainnya. bukti lainnya adalah dibawah ini juga (merubah teks)
"""
c[1] = "samsung"
print(c)