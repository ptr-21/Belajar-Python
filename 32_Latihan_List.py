"""Latihan List"""
"""Seperti membuat db sederhana dengan menggunakan list"""
"""Program list data smartphone"""
list_smartphone = []
while True :
    print("Masukkan data smartphone")
    merk = input("masukkan merk smartphone : ")
    seri = input("Masukkan seri smartphone : ")
    smartphone_baru = [merk,seri]
    list_smartphone.append(smartphone_baru)
    print("\n\n","="*10,"Data Smartphone","="*10)
    for index, smartphone in enumerate(list_smartphone) :
        print(f"{index+1} | {smartphone[0]} | {smartphone[1]}")
    print("\n\n","="*20)
    lanjut = input("Apakah inputan ingin dilanjutkan?(y/n) ")
    if lanjut == "n" :
        break
    print("Input data telah selesai")