""" Modul latihan perulangan """

""" Membuat Segitiga """
""" 1. Dengan For """
jumlah_baris = 10
hitung = 1
for i in range(10) :
    print("*"*hitung)
    hitung += 1
""" 2. dengan while """
while True :
    print("*"*hitung)
    hitung += 1
    if hitung > jumlah_baris :
        break

""" Modul latihan perulangan """
hitung = 1
while True :
    if (hitung %2) :
        print ("*"*hitung)
        hitung +=1
        """ artinya langung skip jika ganjil"""
    else :
        hitung +=1
        continue 
    if hitung > jumlah_baris :
        break
print("akhir dari program")

""" contoh lain yaitu membuat segitiga sama kaki """
baris = 10
""" variabel yang digunakan untuk membuat segitiga sama kaki sebanyak 10 baris """
hitung = 1
space = int(baris/2)
""" bertujuan untuk agar memberi spasi di kiri tidak sebanyak
jumlah baris karena secara logika bagian kiri dan kanan itu kalo misal
sebaris adalah 10 spasi maka kita memerlukan :
bagian kiri jumlah baris/2 dan kanan pun sama
namun kanan tidak diberi karena di kanan itu unlimited space jadi tidak perlu"""
while True :
    """ tujuan kode if (hitung%2) adalah 
    agar presisi di baris bawahnya karena kita perlu +2 bintang
    saat looping. yang jadi masalah adalah kalo misal 10-1 maka
    dia akan print ** bukan *** """
    if (hitung%2) :
        print(" "*space,"*"*hitung)
        space -=1
        hitung += 1
    else :
        hitung += 1
        continue
    """ ketika ganjil maka di skip, jika tidak di skip maka hasilnya tidak presisi
    dan kacau"""
    if hitung > baris :
        break
    """ jika tidak di break maka akan melanjutkan terus menerus """
print("selesai")


baris = 9
hitung = 1
space = int(baris / 2)
while hitung <= baris:
    if hitung % 2:
        print(" " * space + "*" * hitung)
    hitung += 2
    space -= 1
hitung = baris - 2
space = 1
while hitung > 0:
    if hitung % 2:
        print(" " * space + "*" * hitung)
    hitung -= 2
    space += 1  