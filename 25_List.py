"""Modul List"""
angka = 1
angka1 = 2
angka2 = 3
"""ribett"""
"""ada cara lain yaitu array tapi tidak ada di python
    maka dari itu dapat menggunakan list
"""
data_angka = [1,2,3,4,5]
print(data_angka)
string = ["halo","gaes","kita",'sedang',"belajar"]
print(string)
d_boolean = [True, False, True,True]
print(d_boolean)
daata_campuran = [1,'jajan',2,'makanan berat', 'juice',True,False]
print(daata_campuran)
#ambil karakter dari pertama hingga ke 3
ambilkarakter = daata_campuran[:3] #
print(ambilkarakter)
#ambil karakter dari pertama hingga ke 3 tapi dari belakang
ambilkarakter = daata_campuran[-3:] #
print(ambilkarakter)
#mengubah karakter sesuai index di dalam []
daata_campuran[0] = 0
print(daata_campuran)

"""data campuran"""
jarak = range(0,10)
jarakgnp = range(0,10,2) # 2 sebagai setiap 2 atau +2
datalist = list(jarak)
print(datalist)
datalist = list(jarakgnp)
print(datalist)

"""list dengan for loop, list comprehensi"""
datalist_for = [i for i in range(0,10)]
"""i = untuk i di dalam jarak 0 hingga 10"""
print(datalist_for)
"""di buat jarak seperti kuadrat, kalo mau pangkat 3 tinggal ganti 3"""
datalist_for = [i**2 for i in range(0,10)]
print(datalist_for)

"""Membuat list pake for dan pake if
    dibawah ini adalah contoh jika ingin expect genap only
"""
list_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_for_if)

"""misal tdk mau ada 0"""
list_for_if = [i for i in range(0,10) if i != 0]
print(list_for_if)