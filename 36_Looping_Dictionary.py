"""Modul Looping Dictionary"""
merk_smartphone = {
    "1" : "Apple",
    "2" : "Samsung",
    "3" : "Xiaomi",
    "4" : "Oppo",
    "5" : "Vivo "
}

"""Looping"""
for merk in merk_smartphone :
    print(merk)
    """yang keluar hanya keynya saja yang jadi masalah ini tidak diket
    ini list atau bukan"""

"""Operator untuk mengambil item atau iterables (iterasi)"""
keys = merk_smartphone.keys()
print(keys)
for key in merk_smartphone.keys() :
    print(key)



"""Mengambil data (valuenya saja)"""
values = merk_smartphone.values()
print(values)

"""Menggunakan Loop"""
for value in merk_smartphone.values() :
    print(value)

items = merk_smartphone.items()
print(items)
for item in merk_smartphone.items() :
    print(item)

for key,value in merk_smartphone.items():
    print(f"key = {key}, value = {value}")