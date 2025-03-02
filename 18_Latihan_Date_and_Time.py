""" Modul Latihan Date and Time """

""" library time """
import datetime as dt 
""" artinya dari kode tsb mengimport datetime sebagai dt yang dimana dt itu
digunakan untuk memanggil fungsi dari datetime spt oop """

hari_ini = dt.date.today()
"""jangan lupa gunakan kurung karena jika tidak yang diprint adalah octal"""
print("tanggal hari ini adalah:", hari_ini)
""" untuk print tanggal """
print(f"hari ini adalah hari = {hari_ini:%A}")
""" untuk print hari yaitu menggunakan kode ":%A" """
tanggal_merdeka = dt.date(1945,8,17)
print(tanggal_merdeka)
print(f"hari kemerdekaan adalah hari {tanggal_merdeka:%A}")

""" Menghitung umur """
print("Masukkan tanggal lahir anda sesuai dengan form dibawah ini\n")
tanggal = int(input("Tanggal\t\t: ")) 
bulan = int(input("Bulan\t\t: ")) 
tahun = int(input("Tahun\t\t: ")) 
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah: {tanggal_lahir}")
print(f"hari lahir anda: {tanggal_lahir:%A}")
hari_ini = dt.date.today()
umur = (hari_ini - tanggal_lahir).days
umur_dlm_thn = umur // 365
"""jangan lupa gunakan floor division agar dibulatkan kebawah umurnya
jika belum tahu silahkan ke file modul_13"""
print(f"umur anda dalam tahun: {umur_dlm_thn} tahun")
"""ingin mengetahui berapa umur dengan tahun dan bulan"""
umur_bulan = (umur % 365) // 30
print(f"umur anda adalah: {umur_dlm_thn} tahun {umur_bulan} bulan")