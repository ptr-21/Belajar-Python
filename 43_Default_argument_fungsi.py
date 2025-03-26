"""Default argument fungsi
biasanya kalo pake argument :
def fungsi(argument) :

kalo default :
def fungsi(argument = nilai defaultnya)
"""

"""ini adalah tidak pake default"""
def panggilan(nama) :
    print(f"hello {nama}")
panggilan("alice")

"""ini adalah pake default"""
def panggilan(nama = "pelanggan") :
    print(f"hello {nama}")
panggilan()
"""apa itu maksud ada defaultnya
    jadi kalo tidak ada yang isi inputannya maka
    otomatis menampilkan defaultnya
"""

"""coba default lebih 1 arguments"""
def sapaPelanggan(nama = "Pelanggan", surat = "yang terhormat") :
    print(f"Selamat Datang {nama} {surat}")
sapaPelanggan()
""""kalo pakai nama aja"""
sapaPelanggan("alice")
"""kalo inputannya lengkap"""
sapaPelanggan("alice", "pelanggan setia")

"""contoh lain pake default argument"""
def hitung(angka, pangkat) :
    hasil = angka**pangkat
    return hasil
print(hitung(5,2))
hasilhitung = hitung(2, 5)
print(hasilhitung)

"""contoh lain pake default argument dan banyak inputan"""
def jumlah(angka1 = 5, angka2 = 7, angka3 = 5, angka4 = 9, angka5 = 10):
    hasiljumlah = angka1 + angka2 + angka3 + angka4 + angka5
    return hasiljumlah
print(jumlah())
print(jumlah(angka4=70))