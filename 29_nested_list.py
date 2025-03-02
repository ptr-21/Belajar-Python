"""Modul nested list
    -> membuat list di dalam list
"""
data = [1,2]
data_1 = [3,4,5]

listgabungan = [data,data_1]
print(f"list data gabungan = {listgabungan}")

"""contoh penggunaan"""
data1 = ['samsung','galaxy','s25']
data2 = ['oppo','find','x8']
data3 = ['apple','iphone',15]
gabung = [data1,data2,data3]
print(f"list smartphone = {gabung}")
"""kode untuk ambil merek smartphone"""
for smartphone in gabung:
    print(f"Merk\t: {smartphone[0]}")
    print(f"tipe\t: {smartphone[1]}")
    print(f"seri\t: {smartphone[2]}\n")