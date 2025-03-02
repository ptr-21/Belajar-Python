""" Modul Operasi dan Manipulasi String dengan menggunakan metode """
""" Operator dalam bentuk methods :
1. merubah case dari string """

""" Merubah semua ke upper case (capslook) """
data = "halo!"
print("teks asli: " + data)
data = data.upper() #sbg capslook
print("teks upper: " + data)

data_1 = "pRoGrAmMeR"
print("teks asli: " + data_1)
data_1 = data_1.lower() #utk ubah ke lower dari capslook
print('hasil dari lower = ' + data_1)

""" pengecekan huruf apakah up atau lower """

data_2 = "gaming"
cek_lower = data_2.islower() #hasilnya boolean hrs di casting ke str dibwhny
print('apakah huruf \"' + data_2 + '\" low caps semua? ' + str(cek_lower))

data_3 = "I LOVE CODING"
cek_upper = data_3.isupper() #hasilnya boolean hrs di casting ke str dibwhny
print('apakah huruf \"' + data_3 + '\" up caps semua? ' + str(cek_upper))



""" pengecekan huruf diseluruh rangkuman selain up atau lower """

data_4 = "I LOVE CODING" 
"""akan false krn ada spasi (hrs huruf saja titik)"""
cek_alpha = data_4.isalpha() 
"""hasilnya boolean hrs di casting ke str dibwhny kalo tidak di casting hasilnya
akan error dan menampilkan pesan can only concatenate str (not "bool") to str"""
print('apakah \"' + data_4 + '\" huruf semua? = ' + str(cek_alpha))

data_5 = "I < 3 CODING"
"""akan false krn harus angka dan huruf aja dan tdk blh spasi"""
cek_alnum = data_5.isalnum()
"""hasilnya boolean hrs di casting ke str dibwhny kalo tidak di casting hasilnya
akan error dan menampilkan pesan can only concatenate str (not "bool") to str"""
print('apakah \"' + data_5 + '\" ada huruf dan angka? = ' + str(cek_alnum))

data_6 = "123456789"
cek_decimal = data_6.isdecimal()
"""hasilnya boolean hrs di casting ke str dibwhny kalo tidak di casting hasilnya
akan error dan menampilkan pesan can only concatenate str (not "bool") to str"""
print('apakah \"' + data_6 + '\" angka semua? = ' + str(cek_decimal))

data_7 = "apa\nbenar\tkalo ini ada tab spaci???" 
"""akan false krn ada huruf dn tanda baca"""
cek_space = data_7.isspace() 
"""hasilnya boolean hrs di casting ke str dibwhny kalo tidak di casting hasilnya
akan error dan menampilkan pesan can only concatenate str (not "bool") to str"""
print('apakah \"' + data_7 + '\" ada new line, tab, dan spasi? = ' + str(cek_space))

data_8 = "Apa Iya Huruf Depan Ini Besar"
cek_title = data_8.istitle() 
"""hasilnya boolean hrs di casting ke str dibwhny kalo tidak di casting hasilnya
akan error dan menampilkan pesan can only concatenate str (not "bool") to str
catatan : huruf kedua itu tidak boleh terpisah dengan apapun harus huruf jg
di urutan kedua. misal I's itu ga bisa"""
print('apakah \"' + data_8 + '\" huruf depannya besar? = ' + str(cek_title))

""" 
    Rangkuman untuk mengecek :
    islower() -> untuk mengecek apakah semuanya huruf kecil
    isupper() -> untuk mengecek apakah semuanya huruf besar
    isalpha() -> untuk mengecek apakah semuanya hanya huruf saja
    isalnum() -> untuk mengecek apakah isinya ada hanya huruf dan angka
    isdecimal() -> untuk mengecek apakah semuanya angka
    isspace() -> untuk mengecek apakah isinya ada spasi, tab, newline
    istitle() -> untuk mengecek apakah semua kata dimulai huruf besar
"""

""" negecek komponen startswitch() dan endswith() 
startswitch() = utk cek huruf atau pencocokan value mulai dari depan
endswith()    = utk cek huruf atau pencocokan value mulai dari belakang
"""
cek_start = "nitendo ds".startswith("nitendo")
print('start = ' + str(cek_start))
cek_end = "nitendo ds".endswith("ds")
print('end = ' + str(cek_end))

"""penggabungan komponen join() dan split()
join()  = penggabungan
split() = pemisahan yaitu dihapus misal teks kck di split maka kck hilang
"""
data_list = ['main', 'mario', 'bross', 'di', 'nds']
data_gabung = ','.join(data_list)
print(data_list)
print(data_gabung)

joinn = ' '.join(data_list)
print(joinn)

joinnn = ' gg '.join(data_list)
print(joinnn)

data_gabungan = "iniadalahtulisan"
print(data_gabungan.split("adalah"))

"""alokasi karakter menggunakan rjust(), ljust(), dan center()
rjust() = rata kanan (right justify)"""

r_just = "right=".rjust(10) 
""" memberi rata kanan ke kanan sebanyak 10
    misalkan panjang ruas adalah 10 maka teks akan ditulis dari kanan
    dan jika kelebihan sisanya blank. Contoh kalo teksnya aku (jumlah 3 huruf)
    maka jumlah blank space adalah 7 contoh : "       aku"
"""
print("'" + r_just + "'")

l_just = "left=".ljust(10) 
""" memberi rata kiri ke kiri sebanyak 10
    misalkan panjang ruas adalah 10 maka teks akan ditulis dari kiri
    dan jika kelebihan sisanya blank. Contoh kalo teksnya aku (jumlah 3 huruf)
    maka jumlah blank space adalah 7 contoh : "aku       "
"""
print("'" + l_just + "'")

c_just = "aku".center(10) 
""" memberi rata kanan dan kiri sebanyak n/2 (kalo genap)
    kalo ganjil yang kiri adalah floor division dan yang kanan ceil division 
    (pembulatan ke atas)
    n = panjang ruas kosong
    misalkan panjang ruas yang kosong atau sisanya dari kata yang diberikan
    maka ruang kiri dan kanan adalah 7/2 maka menjadi : "   aku    "
"""
print("'" + c_just + "'")
#kalo ingin ditambah karakter agar tidak kosong maka
c_just = "gaming".center(10, "=")
print("'" + c_just + "'")

"""kebalikannya = strip.
apa tujuannya? menghilangkan ruas yang kosong
kalo kiri dan kanannya kosong maka memberikan tanda () saja
kalo kiri dan kanannya ada tanda seperti = maka memberikan tanda "="
"""

c_just = c_just.strip("=") #menghilangkan tanda =
print("'" + c_just + "'")
l_just = l_just.strip() #menghilangkan sisa ruang kosong
print("'" + l_just + "'")

"""sebenarnya masih ada yang lainnya (banyak) jika ingin tau bisa gugling"""