""" deep copy nested list
->  di modul sebelumnya kita dapat memakai copy list
    agar dapat membuat list baru tapi duplikat dgn list sblmnya
    namun yang jadi masalah adalah ketika membuat list di dalam list
    lalu ketika di copy maka bagian list yang di dalam list tidak membuat baru
    dan reference ke memory yang sama (seperti 29_nested_list.py)
"""
data = [1,2]
data1 = [3,4,5]
datagbg = [data,data1]

"""mengambil data pertama dari nested list"""
dataprtama = datagbg[0][1]
"""artinya adalah array urutan ke 0 dan ambil data urutan dlm array ke 1"""
print(dataprtama)
dataa = datagbg.copy()
""" terkait masalah list di dalam list adalah
    misal di dalam list a = b c d
    lalu ketika di buat a.copy maka 
    misal a.copy itu adalah e
    tetapi di dalam e yaitu = b c d itu memorinya sama semua.
    gimana cara buktikannya? ini caranya :
"""

print(f"alamat memory dari array 0 index 1 di datagbg = {hex(id(datagbg[0][1]))}")
print(f"alamat memory dari array 0 index dataa = {hex(id(dataa[0][1]))}")

"""di modul 29.py ketika kita menggunakan copy() maka
    copy() -> shallow copy jadi tidak semuanya di copy atau duplikat
    sehingga list di dalam listnya masih menggunakan refrence
    solusinya adalah menggunakan deepcopy
    dibawah ini adalah aplikasi deepcopy
"""
from copy import deepcopy
datagbg = [data,data1,10]
datagbg_deepcopy = deepcopy(datagbg)
print(f"address data asli = {hex(id(datagbg[1][1]))}")
print(f"address data deep copy = {hex(id(datagbg_deepcopy[1][1]))}")