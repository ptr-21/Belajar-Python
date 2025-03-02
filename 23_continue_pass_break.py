""" Modul continue, pass, break """

""" ini kalo tidak ada apa apa spt tidak ada continue, pass, break""" 
value = 0
while value < 5 :
    value += 1
    if value % 2 != 0 :
        print("angka ganjil")
    else :
        print("angka genap")
    print(value)
    print()

""" continue : misalkan ada 2 kondisi dimana angka 1 hingga 2 itu bilangan yang
    di terima dan 4 hingga 5 juga di terima sedangkan 3 itu tidak diterima
    maka kondisinya adalah demikian
"""

val = 0
while val < 5 :
    val += 1
    print(f"Angka saat ini : {val}")
    if val == 3 :
        print("tidak diterima")
        continue
    """fungsi continue disinilah yang mengskip tidak diterima
    jadi kita bisa mempunyai 2 kondisi"""
print()

""" pass : berfungsi sebagai dummy, dan tidak akan di eksekusi """
""" contoh implementasi pass :
    catatan : pada kode pas itu tidak di apa apakan
    jadi tidak di eksekusi kodenya hanya dummy atau kosong aja
"""
value1 = 0
while value1 < 5 :
    value1 += 1
    if value1 % 2 != 0 :
        pass
    else :
        pass
    print(value1)

""" Break :
    start -> ketika kondisi true maka :
    pergi ke aksi 1 lalu ketika aksi 1 telah dijalankan
    maka dia akan ke finish program (jika tidak ada aksi berikutnya)
    tetapi jika kita membuat program aksi berikutnya maka dia akan lanjut
    eksekusi ke aksi berikutnya dan ketika aksi berikutnya terdapat break
    maka dia akan stop hingga kode break saja
"""

data = 0
while data < 15 :
    data += 1
    print(f"data sekarang: {data}")
    if data == 3:
        print("data anda tidak diterima")
        break
    print("data diterima")

""" Contoh 2 """
user = int(input("Masukkan angka yang ingin anda ulang perhitungannya: "))
val1 = 0
while True :
    val1 += 1
    print(f"urutan = {val1}")
    if val1 == user:
        print("perulangan perhitungan telah selesai")
        break
    print("ini adalah perulangan sesuai dengan urutan")
print("program selesai dijalankan")