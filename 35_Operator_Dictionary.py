"""Modul Operator Dictionary"""
dataDictionary = {
    "1":"Samsung",
    "2":"Apple",
    "3": "Vivo"
}
"""Panjang Dictionary"""
lenDictionary = len(dataDictionary)
print(f"panjang Data Dictionary : {lenDictionary}")

"""Mengecek Key exist atau tidak"""
key = "1"
checkKey = key in dataDictionary
"""Mengecek apakah key ada di dataDictionary"""
print(f"apa benar {key} ada di data dictionary: {checkKey}")

"""Mengakses value dengan get"""
print(dataDictionary["1"])
print(dataDictionary.get("1"))
"""menampilkan pesan ketika key tidak ditemukan"""
print(dataDictionary.get("4","Key tidak ditemukan"))

"""Update / manipulasi data"""
dataDictionary["1"] = "OPPO"
"""Tambah data (hanya tinggal tambah key yang tidak ada)"""
dataDictionary["4"] = "Huawei"
print(dataDictionary)

"""Menggunakan fungsi update (fungsinya sama saja)"""
dataDictionary.update({"1":"Lenovo"})
print(dataDictionary)
dataDictionary.update({"5":"Motorola "})
print(dataDictionary)

"""Delete data pada dictionary"""
del dataDictionary["4"]
print(dataDictionary)