"""Modul manipulasi List (masuk ke dlm operasi)"""
data = ["kocak", 'geming', 'ggwp']

"""cara ambil data dari list
    def terdapat index dalam list
    cth : 0,1,2,3, dst
    kalo dari belakang tinggal kasih mines
    cth -1 adalah mengambil index terakhir sendiri
    kenapa tidak -0 karena 0 tidak terdef
"""
data1 = data[0]
print(f"data pertama adalah {data1}")
last = data[-1]
print(f"data pertama adalah {last}")
"""mengambil info jumlah data list"""
range_data = len(data)
print(f"panjang data adalah {range_data}")

""""manipulasi data list
    tuj (def) -> merubah isi data list baik menambahkan atau mengurangi
"""
"""cth 1 menambahkan item pada list sesuai posis
    ket = kalo insert bisa disesuaikan psosisinya, kalo append = nambah
    data terakhir
"""
print(f"data sebelum ditambah = {data}")
"""cth ilustrasi "data.insert(posisi, data) -> data.insert(1, world)"""
data.insert(1, 'world')
print(f"data sesudah ditambah = {data}")

data.append("spelt")
print(f"data sesudah ditambah diakhir = {data}")

"""menambahkan list dengan list"""
databaru = ["intel",'core','i9']
data.extend(databaru)
print(f"data sesudah digabung (list dengan list) = {data}")

"""Merubah data"""
data[2] = "hello world"
print(f"data sesudah dirubah di index 2 = {data}")
"""menghapus data"""
data.remove("kocak")
print(f"data sesudah hapus teks kocak = {data}")
"""menghapus data palling belakang"""
data.pop()
print(f"data sesudah dihapus palling belakang =  {data}")
"""menghapus data urutan index 2"""
data.pop(2)
print(f"data sesudah dihapus di index 2 =  {data}")
data.pop(-2)
print(f"data sesudah dihapus di index -1 dari belakang =  {data}")
data.remove("halo")
print(f"data sesudah hapus teks halo = {data}")
"""pasti akan error karena tidak ada datanya"""