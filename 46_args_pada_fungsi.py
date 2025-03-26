""" args pada fungsi 
    contoh :
    def fungsi(*args)
    tujuan memasukan banyak data atau argumen dlm fungsi lebih simple
"""
"""ini tidak pakai args dan terlalu ribet"""
def function(list):
    data = list.copy()
    merk = data[0]
    tipe = data[1]
    kelas = data[2]
    print(f"Merk hp = {merk}, tipe hp = {tipe}, kelas hp = {kelas}")

function(["Oppo", "Find x8", "Flagship"])

"""ini pakai args, dan tidak perlu pakai list (lebih simple)"""
def fungsi(*args) :
    merk = args[0]
    tipe = args[1]
    kelas = args[2]
    print(f"Merk hp = {merk}, tipe hp = {tipe}, kelas hp = {kelas}")
fungsi("Oppo", "Find x8", "Flagship")

"""contoh lain tapi ga perlu pake args bisa di rubah asal pake * """
def tambah(*data) :
    inisialisasi = 0
    for angka in data :
        inisialisasi += angka
    
    return inisialisasi

tambahan = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {tambahan}")
