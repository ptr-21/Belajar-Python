""" *Modul cara kerja program dan bytecode* """

"""cara menghitung waktu"""
import time
start_time= time.time()
print(time.time() - start_time, "detik")
""" STOP """

print("test")
print("tes\nenter")
#tes comment

""" memanggil variabel dan menaruh assignment """
a = 10
print(a)
"""
di python tidak bisa naruh variabel di bawahh print karena eksekusi
dari atas krn intepreted 
"""



"""
Ini adalah comment multiline.
Bisa digunakan untuk dokumentasi atau keterangan panjang.
kalo di py ga keluar kalo ipynb keluar di output
"""



"""
cara merubah syntax menjadi byte code agar eksekusi lbih cpt spt C++
yaitu program compiler adalah

1. buka terminal
2. ketik python -m py_compile namafile.py
3. lalu untuk eksekusi adalah cd (change directory ke
    folder utk eksekusi program) yaitu __pycache__
4. ketik python namafile.cpython-3.13.pyc
utk angka sesuai dg versi yang dipakai


kalo python lambat krn intepreted bisa ditanggulin dengan cara ini

catatan : cara menjalankan python ada 2 :
1. tekan panah play di ide (kalo vscode)
2. lewat terminal :
    terminal -> new terminal -> ketik " python namafile.py (sesuaikan nama filenya)
    -> enter
"""
