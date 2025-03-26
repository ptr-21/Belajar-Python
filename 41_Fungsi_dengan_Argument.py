"""Fungsi dengan Argument
    maksudnya bisa diisi dengan input
    kalo fungsi itu deklarasinya begini
    def nama_fungsi(argumen) :
    isi dari fungsi
"""

"""Contoh 1"""
def selamat_datang(pengunjung) :
    '''fungsi menerima inputan nama pengunjung 
    sesuai di (pengunjung)'''
    print(f"selamat datang{pengunjung}")

selamat_datang("MANUSIA")

"""contoh 2"""
def penjumlahan(angka1, angka2) :
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

penjumlahan(5, 2)

"""contoh 3 pakai list"""
def pakelist(peserta) :
    data_peserta = peserta.copy()
    """tujuan pakai copy agar tidak terubah data di nama_peserta"""
    for peserta in data_peserta :
        print(f"selamat datang peserta {peserta}")

nama_peserta = ["Lissa", "Andi", "Dinda"]
pakelist(nama_peserta)
"""analogi di line 30 hingga 31 adalah
    pakelist itu manggil fungsi
    nama_peserta memasukkan data
"""

