"""Latihan Fungsi
    program menghitung luas dan keliling persegi pjg
    fungsi dari os untuk auto clear ketika prgrm sls
    dijlnkn
"""

"""Contoh kalo tidak pake fungsi (def) : """
"""import os
os.system("cls")
print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(f"{'-'*40:^40}")

lebar = int(input("Masukkan lebar persegi: "))
panjang = int(input("Masukkan panjang persegi: "))

luas = panjang * lebar
keliling = 2*(panjang + lebar)
print(f"hasil luas persegi = {luas}")
print(f"hasil keliling: {keliling}")"""

"""contoh diatas jika tidak menggunakan def atau fungsi
    untuk implementasi fungsi berada dibawah ini
"""
import os

def utama():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def inputUser() :
    lebar = int(input("Masukkan lebar persegi: "))
    panjang = int(input("Masukkan panjang persegi: "))
    return lebar, panjang   

def hitung_luas(lebar, panjang) :
    return panjang * lebar

def hitung_keliling(lebar, panjang) :
    return 2* (panjang + lebar)

def display(pesan, value) :
    print(f"hasil perhitungan {pesan} = {value}")

while True :
    utama()
    lebar, panjang = inputUser()
    luas = hitung_luas(lebar, panjang)
    keliling = hitung_keliling(lebar, panjang)
    isContinue = input("apakah anda ingin hitung lagi(y/n)? : ")
    display("Luas", luas)
    display("keliling", keliling)
    if isContinue == "y" :
        utama()
    elif isContinue == "n" :
        break
    else :
        print("Keyword yang Anda masukkan tidak cocok, silakan jawab y/n")

