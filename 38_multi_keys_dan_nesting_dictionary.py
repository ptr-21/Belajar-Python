"""Modul multi keys dan nesting dictionary"""
import datetime 
pegawai1 = {
    'nama' : 'harris sudirman',
    'id_pegawai' : '1254789',
    'jam_kerja_seminggu' : '40',
    'lembur' : 'false',
    'tanggal_masuk' : datetime.datetime(2025,2,27)
}
pegawai2 = {
    'nama' : 'budi harjo',
    'id_pegawai' : '44488848',
    'jam_kerja_seminggu' : '42',
    'lembur' : 'true',
    'tanggal_masuk' : datetime.datetime(2025,2,25)
}
pegawai3 = {
    'nama' : 'dini sudarni',
    'id_pegawai' : '48411210',
    'jam_kerja_seminggu' : '48',
    'lembur' : 'true',
    'tanggal_masuk' : datetime.datetime(2025,2,2)
}

"""Memasukkan data ke dalam key"""
dataPegawai = {
    'key1':pegawai1,
    'key2':pegawai2,
    'key3':pegawai3
}
"""untuk mengatur tata letak print"""
print(f"{'key':<4} {'Nama':<17} {'id Pegawai':<12} {'Jam Kerja Seminggu':<2} {'Lembur':<2} {'Tanggal Masuk':<8}")

for pegawai in dataPegawai :
    key = pegawai
    nama = dataPegawai[key]['nama']
    idpegawai = dataPegawai[key]['id_pegawai']
    jamKerjaSeminggu = dataPegawai[key]['jam_kerja_seminggu']
    lembur = dataPegawai[key]['lembur']
    tngglMasuk = dataPegawai[key]['tanggal_masuk'].strftime("%x")
    print(f"{'key':<4} {nama:<17} {idpegawai:<12} {jamKerjaSeminggu:<18} {lembur:<6} {tngglMasuk:<8}")
