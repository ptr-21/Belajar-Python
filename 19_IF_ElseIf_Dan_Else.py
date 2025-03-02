""" Modul IF, Else If Dan Else """
""" Pengertian :
    Di modul sebelumnya kita memiliki program satu alur yang dimana
    tidak ada kondisi, jadi hanya 1 kondisi saja dan berjalan secara linier.
    contoh sederhana : apapun kondisinya maka program tetap dijalankan dengan 1
    hasil.
    Berbeda dengan menggunakan if, contoh sederhananya adalah :
    apakah seorang siswa mendapatkan nilai kkm? jika ketentuannya adalah kkm
    minimal 75? berikut adalah contoh kodenya
"""
kkm = 75
nilai_siswa = float(input("Masukkan nilai siswa:\t"))
if nilai_siswa == kkm :
    print("nilai siswa yang anda masukkan telah mencapai kkm")
elif nilai_siswa >= kkm and nilai_siswa <= 100 :
    print("nilai siswa yang anda masukkan lebih dari kkm!!, Selamat!!!")
elif nilai_siswa <= kkm :
    print("nilai siswa yang anda masukkan belum sampai kkm :(")
else :
    print("Masukkan nilai yang valid antara 0 - 100")
"""jika bingung dengan tanda operator atau lupa silahkan ke modul atau file
    8.py terimakasih :) """
""" penjelasan :
    if nilai_siswa == kkm adalah jika nilai_siswa sama dengan kkm maka
    print("nilai siswa yang anda masukkan telah mencapai kkm")
    elif (selain dari kondisi if pertama sama tetapi ini jika keadaan
    dalam kondisi kedua selain pertama)
    else : selain dari jika itu semua
"""

"""contoh 2
    misalkan nilai abjad:
    a itu nilai antara 80 - 100
    b itu nilai antara 70 - 80
    c itu nilai antara 55 - 70
    d itu nilai antara 35 - 55
    e itu nilai antara 0 - 35
    maka :
    """

nilai = float(input("Masukkan nilai: "))
if nilai >= 80 and nilai <= 100 :
    print("Nilai abjad : A")
elif nilai >= 70 and nilai <= 80 :
    print("Nilai abjad : B")
elif nilai >= 55 and nilai <= 70 :
    print("Nilai abjad : C")
elif nilai >= 35 and nilai <= 55 :
    print("Nilai abjad : D")
elif nilai >= 0 and nilai <= 35 :
    print("Nilai abjad : E")
else :
    print("Masukkan nilai yang valid antara 0 - 100")