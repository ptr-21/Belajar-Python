"""Modul Operasi List"""
dataangka = [1,2,5,4,7,5,4,7,6,1]
print(f"data angka = {dataangka}")
"""menghitung jumlah angka yang ingin di cari misal 7"""
jumlah_angka_7 = dataangka.count(7)
print(f"jumlah angka 7 = {dataangka}")

"""ambil posisi data index"""
data = ["kocak", 'geming', 'ggwp']
dataggwp = data.index("ggwp")
print(f"data ggwp berada di inex = {dataggwp}")

"""mengurutkan list"""
print(f"data angka sebelum sorting = {dataangka}")
dataangka.sort()
print(f"data setelah di sort = {dataangka}")

print(f"data huruf sebelum sorting = {data}")
data.sort()
print(f"data setelah di sort = {data}")
"""diurutkan berdasarkan abjad"""

"""balik list kebalikan dari sort"""
print(f"data angka sebelum reverse = {dataangka}")
dataangka.reverse()
print(f"data setelah di reverse = {dataangka}")

print(f"data huruf sebelum reverse = {data}")
data.reverse()
print(f"data setelah di reverse = {data}")
"""diurutkan berdasarkan abjad"""