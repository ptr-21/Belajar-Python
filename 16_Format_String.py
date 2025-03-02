""" Modul Format String """
""" Contoh Generic """
spek = "dimensity "
spek1 = "processor"
data_str = "mediatek " + spek + "gaming " + spek1
print(data_str)
print()

"""contoh diatas itu terlalu panjang. tujuan modul ini adalah
    memperingkas. dibawah ini adalah cara mempersingkatnya"""
data_str1 = f"mediatek {spek}gaming {spek1}"
print(data_str1)

"""biasa kalo gabungin tipe data itu harus di casting misal tipe data
    aslinya adalah decimal atau selain tipe data string
    jika gabung dengan string maka harus casting"""


angka = 6.2
datastr = "ukuran layar = " + str(angka)
print(datastr)

"""sedangkan jika pake format string pada data angka decimal"""
angka = 6.2
datastr = f"ukuran layar = {angka}"
print(datastr)

"""sama saja cuma ingin di potong jumlah digit angka desimalnya
    angkanya disesuaikan saja setelah angka:. lalu berikan f"""
angka = 6.215975
datastr = f"ukuran layar = {angka:.2f}"
print(datastr)

"""sama aja tapi menentukan jumlah angka di depannya titik"""
angka = 5976.215975
datastr = f"ukuran = {angka:6.5f}" #lebih dominan jumlah yang ditentukan stlh titik
print(datastr)
datastr = f"ukuran = {angka:8.2f}" # jika kslhrn cuma 7 digit ankga maka kiri dikasih spasi
print(datastr)
datastr = f"ukuran = {angka:08.2f}" # jika diberi 0 maka depannya ada angka 0
print(datastr)

"""contoh pada data angka integer (bilangan bulat)"""
jalur_nasional = 15
datastr = f"kode jalan nasional = {jalur_nasional:d}"
print(datastr)
"""kalo integer boleh dikasih :d setelah nama variabel
    atau kalo tidak juga tidak masalah"""

"""contoh pada data angka ribuan.
    biasanya jika angka ribuan, setiap 3 digit diberi tanda
    koma "," tapi jika tidak perlu maka tidak perlu ditulis ":," """
harga = 15000000
datastr = f"harga apel aipon 16 = {harga:,}"
print(datastr)

"""contoh data boolean"""
data_boolean = True
format_str = f"isi data = {data_boolean}"
print(format_str)
data_boolean1 = False
format_str1 = f"isi data = {data_boolean1}"
print(format_str1)

"""menampilkan tanda + atau -"""
data_min = -15
data_plus = 15
format_min = f"data angka minus = {data_min}"
print(format_min)
format_plus = f"data angka plus = {data_plus}"
print(format_plus)
"""kalo ingin menampilkan tanda + maka : """
format_plus = f"data angka plus dengan tanda = {data_plus:+d}"
print(format_plus)
"""note : kalo int itu pakai d kalo float pakai .f jika 2 angka saja maka .2f"""

"""Memformat Persen"""
data_persen = 0.045
persen = f"data persen = {data_persen}"
print(persen)
"""kalo ingin dijadiin presentase dan diblk koma hanya ingin 2 digit max saja"""
persen = f"data persen dengan 2 digit max terakhir = {data_persen:.2%}"
print(persen)

""" di dalam kurung kurawal kita bisa melakukan apa saja operasinya. contoh :"""
harga_per_pcs = 50000
jumlah_yang_dibeli = 5
total_harga = f"total yang harus dibayarkan = Rp. {harga_per_pcs * jumlah_yang_dibeli:,}"
print(total_harga)

""" Format angka lain (binary, octal, hexadecimal)
penjelasan code :
bin, oct, hex adalah tools untuk merubah dari angka ke misal
bin = binary
oct = octal
hex = hexadecimal
"""

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hex)