"""Fungsi dengan return (return value)
    contoh ilustrasi 1 :
    y =  f(x) 
    f = nama fungsi
    x = variabel input
    y = outputnya yang dimana returnnya ke outputnya

    contoh ilustrasi 2 :
    def fungsi (inputan) :
    hasil = input ** 2
    return hasil
    y = fungsi(x)
    atau contoh di dunia nyata
    def fungsi_kuadrat(x) :
    hasil = x**2
    return hasil
    y = kuadrat(4)
    y = 16
    dibawah ini adalah contoh programnya
"""
def kuadrat(x) :
    fungsikuadrat = x**2
    return fungsikuadrat

y = kuadrat(5)
print(y)

"""bisa dengan cara dibawah ini karena
    definisinya tadi return
"""
print(kuadrat(3))

z = 15 + kuadrat(3)
print(z)

"""fungsi penjumlahan"""
def penjumlahan(angka1, angka2) :
    return angka1 + angka2

a = penjumlahan(5, 15)
print(a)

"""contoh kalo operasi mtk banyak"""
def operator_mtk(angka1, angka2) :
    pertambahan = angka1 + angka2
    pengurangan = angka1 - angka2
    perkalian = angka1 * angka2
    pembagian = angka1 / angka2
    return pertambahan, pengurangan, perkalian, pembagian

tambah,kurang,kali,bagi = operator_mtk(5,15)

print(f"Hasil Tambah = {tambah}")
print(f"Hasil kurang = {kurang}")
print(f"Hasil kali = {kali}")
print(f"Hasil bagi = {bagi}")

"""cara bacanya adalah 
    1. buat argumen value parameter sesuai kebutuhan
    kalo di kodenya angka1 dan angka2 berarti 2
    dimana argumen value itu menerima inputan value
    2. buat statement sesuai keinginan misal 
    kalo 4 program ya buat 4 seperti di kode
    3. buat return sebanyak 4 sesuai statement yang
    telah dibuat
    4. ketika di luar def ya buat sebanyak 4 juga var
    untuk menghasilkan return 4 (sesuai statemen yang
    telah dibuat)
    kalo misal 8 ya 8 buat varnya
    5. print digunakan untuk menghasilkan returnnya
    sesuai urutan kalo misal tambah dulu ya 
    return pertamanya penjumlalhan
"""