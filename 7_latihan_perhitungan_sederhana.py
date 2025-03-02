""" *Modul latihan perhitungan sederhana* """
""" conversi suhu antara celcius, reamur, fahrenheit, kelvin """
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input("Masukkan suhu dalam satuan celcius yang ingin dikonversi: "))
reamur = (4/5)*celcius
print("suhu dalam reamur: ", reamur, "reamur")
fahrenheit = ((9/5)*celcius) + 32
print("suhu dalam farenheit: ", fahrenheit, "fahrenheit")
kelvin = celcius + 273
print("suhu dalam farenheit: ", kelvin, "kelvin")

"""
Latihan
1. fahrenheit ke kelvin
2. kelvin ke fahrenheit
"""

f = float(input("Masukkan suhu suhu dalam satuan fahrenheit yang akan dikonversi ke kelvin: "))
f_to_c = 5/9 * (f-32)
c_to_k = f_to_c + 273
print("suhu dari fahrenheit ke kelvin: ", c_to_k, "kelvin")

k = float(input("Masukkan suhu suhu dalam satuan kelvin yang akan dikonversi ke fahrenheit: "))
k_to_r = 4/5 * (k-273)
r_to_f = (9/4 * k_to_r) + 32
print("suhu dari fahrenheit ke kelvin: ", r_to_f, "kelvin")