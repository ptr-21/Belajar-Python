""" Modul percabangan """

""" Membuat Kalkulator sederhana """
print(5*"=" + "Program Kalkulator sederhana" + 5*"=")
print("operator yang perhitungan yang tersedia")
print("1 untuk penjumlahan")
print("2 untuk pengurangan")
print("3 untuk perkalian")
print("4 untuk pembagian")
operator = int(input("Masukkan operator yang ingin digunakan (1/2/3/4): "))
angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))
if operator == 1 :
    hsl = angka_1 + angka_2
    print(f"hasil dari penjumlahan {angka_1} dengan {angka_2} adalah {hsl}")
elif operator == 2 :
    hsl = angka_1 - angka_2
    print(f"hasil dari pengurangan {angka_1} dengan {angka_2} adalah {hsl}")
elif operator == 3 :
    hsl = angka_1 * angka_2
    print(f"hasil dari perkalian {angka_1} dengan {angka_2} adalah {hsl}")
elif operator == 4 :
    hsl = angka_1 / angka_2
    print(f"hasil dari pembagian {angka_1} dengan {angka_2} adalah {hsl}")
else :
    print("Masukkan operator yang sesuai")