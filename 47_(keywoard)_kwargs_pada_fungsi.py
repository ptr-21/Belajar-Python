""" **(keywoard) kwargs pada fungsi 
    dibawah ini kalo tanpa kwargs
"""
def function(merk, tipe, kelas):
    print(f"merk hp : {merk}, tipe hp : {tipe}, kelas hp : {kelas}")
function("Xiaomi", "Redmi Note 8", "Entry Level")

"""kalo ini pake kwargs jadi nulis key atau dictionary bisa di tulis di luar function"""
def function(**kwargs) :
    print(kwargs)
function(merk="oppo", tipehp="reno 10", kelashp="midrange")

"""contoh lain"""
def function(**kwargs) :
    merk = kwargs["merk"]
    tipehp = kwargs["tipehp"]
    kelashp = kwargs["kelashp"]
    print(f"merk hp : {merk}, tipe hp : {tipehp}, kelas hp : {kelashp}")
function(merk="Vivo", tipehp="x200", kelashp="Flagship")


"""Contoh lain lagi"""
def matematika(*args, **kwargs):
    inisialisasi = 0
    if kwargs["pilihan"] == "tambah":
        for angka in args:
            inisialisasi += angka
    elif kwargs["pilihan"] == "kali":
        inisialisasi = 1
        for angka in args :
            inisialisasi *= angka
    else :
        print("operasi yang anda pilih tidak tersedia")
    return inisialisasi
perhitungan = matematika(1,2,5,4,7,5,pilihan="tambah")
print(f"hasil penjumlahan adalah : {perhitungan}")
perhitungan1 = matematika(1,2,5,4,7,5,pilihan="kali")
print(f"hasil perkalian adalah : {perhitungan1}")

""""kwargs itu mengambil data dictionary"""