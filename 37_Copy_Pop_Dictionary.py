"""Modul Copy & Pop Dictionary"""
data_smartphone = {
    "1" : "Samsung galaxy s25",
    "2" : "Samsung galaxy s23",
    "3" : "Apple Iphone 16",
    "4" : "Vivo X200",
    "5" : "Vivo X100"
}

smartphone = data_smartphone.copy
""".copy digunakan agar ketika data_smartphone di manipulasi datanya maka
    smartphone tidak terubah datanya (seperti list)"""
print(f"Data Smartphone : {data_smartphone}\n")
print(f"Smartphone: {smartphone}\n")
data_smartphone["1"]="Samsung Galaxy S25 Ultra"
print(f"Data Smartphone : {data_smartphone}\n")
print(f"Smartphone: {smartphone}\n")

"""Pop Dictionary (berdasasrkan key)"""
dataSamsung = smartphone.pop("2")
print(f"data smartphone 1 = {dataSamsung}\n")
print(f"Smartphone = {smartphone}\n")

"""Popitem Dictionary (dari urutan terakhir)"""
dataTerakhir = smartphone.popitem()
print(f"data terakhir= {dataTerakhir}\n" )
print(f"Smartphone = {smartphone}")