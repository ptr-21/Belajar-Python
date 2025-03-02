""" Modul Operasi dan Manipulasi String """
""" 1. menyambung string (concatenate) """
nama_pertama = "mario"
nama_terakhir = "bross"
nama_keturunan = "nds"
nama_lengkap_dg_keturunan = nama_pertama + nama_terakhir + nama_keturunan
print(nama_lengkap_dg_keturunan)
"""kalo nambahin spasi: """
nama_lengkap_dg_keturunan = nama_pertama + " " + nama_terakhir + " " + nama_keturunan
print(nama_lengkap_dg_keturunan)
"""kalo nambahin tanda petik satu (') : """
nama_lengkap_dg_keturunan = nama_pertama + " " + nama_terakhir + "'" + nama_keturunan
print(nama_lengkap_dg_keturunan)

""" 2. menghitung panjang dari string (operator length) """
panjang_string = len(nama_lengkap_dg_keturunan)
print("panjang huruf dari " + nama_lengkap_dg_keturunan + " = " + str(panjang_string))
""" harus pake str karena menghitung panjang dari text"""

""" 2. operator utk string
mengecek apakah ada komponen char atau string di string
maksudnya adalah misal buat kata kata yaitu :
aku adalah orang, lalu ingin cek apakah ada huruf a atau tidak di teks tersebut
caranya adalah :"""
d = "d"
cek_status = d in nama_lengkap_dg_keturunan
print("string " + d + "ada di" + nama_lengkap_dg_keturunan + " = " + str(cek_status))
e = 'bross\'nds'
cek_status1 = e in nama_lengkap_dg_keturunan
print("string " + e + " ada di " + nama_lengkap_dg_keturunan + " = " + str(cek_status1))
f = "d"
cek_status2 = d not in nama_lengkap_dg_keturunan
print("string " + d + " tidak ada di " + nama_lengkap_dg_keturunan + " = " + str(cek_status2))

"""mengulang string"""
print("ha"*10)
print(10*"ha")

""" indexing (potong text / ambil text sebagian dimulai dari 0)"""
print("kata di index ke-0 : " + nama_lengkap_dg_keturunan[0])
print("kata di index ke-1 : " + nama_lengkap_dg_keturunan[1])
print("kata di index ke-10 : " + nama_lengkap_dg_keturunan[10])
""" kalo mines diambil dari belakang 
kalo -0 hasilnya sama"""
print("kata di index ke-1 (-1) : " + nama_lengkap_dg_keturunan[-1])
print("kata di index ke-10 (-10) : " + nama_lengkap_dg_keturunan[-10])
"""ambil kata di antara kalo misal dari index ke 0 hingga 5
di python yang terakhir tdk diikuti jadi kalo hingga 5 harus + 1"""
print("index dari 0 ke 5 adalah: " + nama_lengkap_dg_keturunan[0:6]) #kata trkhr + 1
print("index dari 5 ke 10 adalah: " + nama_lengkap_dg_keturunan[5:11]) #kata trkhr + 1
print("index 0, 2, 4, 6, 8, 10 adalah: " + nama_lengkap_dg_keturunan[0:11:2])
"""artinya adalah antara 5 sampai 10 lalu increment 2 (loncatin 1 angka)"""

"""item paling kecil"""
print('paling kecil: ' + min(nama_lengkap_dg_keturunan))
"""item paling besar"""
print('paling kecil: ' + max(nama_lengkap_dg_keturunan))

"""ascii (pengecekan ascii) :
mengambil code ascii dari karakter string yaitu ord"""
ascii_code = ord(" ")
print("ascii code spasi adalah " + str(ascii_code))
"""cara ingin thu ascii code 117 itu huruf apa"""
b = 117
print("ascii code spasi adalah " + chr(b))

"""operator dalam bentuk method
sbnrnya diatas tdk ada method bawaan, spt str itu adalah kelas"""
data_str = "profesi saya adalah ternak lele"
jumlah_str = data_str.count("l") 
""" data_str adalah objectnya  kalo .count() adalah methodnya.
tujuan kode tersebut adalah cari tau berapa jumlah huruf l"""
print('jumlah huruf 0 pada data_str adalah = ' + str(jumlah_str) )

