"""Type Hints Pada / Untuk Fungsi
    Bentuk std fungsi :
    def fungsi(Parameter):
    print(parameter)
    fungsi(value dari parameter)

    yang masalah adalah kalo
    def fungsi(parameter):
    hasil = parameter**2
    print(hasil)
    fungsi("samsung")
    akan menghasilkan error, maka dari itu type hint solusi
    berikut adalah dibawahnya
"""
def fungsi_hints(tipedata:int) :
    pangkat = tipedata**10
    return pangkat

hasil = fungsi_hints(2)
print(hasil)

""" jadi fungsi type hint itu ibarat untuk mengcasting tipe data inputan 
    jika inputan beda dari tipe data yg dignkn otomatiis error
    dibawah ini adalah contoh berikutnya
"""
import string
def fungsi_dghints (tipe:string):
    print(tipe)
fungsi_dghints("samsung")
