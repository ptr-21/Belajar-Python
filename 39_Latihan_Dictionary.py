""" Modul Latihan Dictionary """
import datetime
"""Template Dictionary Pegawai"""
template_pegawai = {
    'nama' : 'nama',
    'id_pegawai' : '000000',
    'jam_kerja_seminggu' : 0,
    'lembur' : False,
    'tanggal_masuk' : datetime.datetime(1111,1,1)
}
data_pegawai = {}
print(f"{'DATA PEGAWAI':^20}")
print("-"*20)

pegawai = dict.fromkeys(template_pegawai.keys())
print(pegawai)
pegawai['nama'] = input("Nama Pegawai: ")
pegawai['id_pegawai'] = input("ID Pegawai: ")
pegawai['jam_kerja_seminggu'] = int(input("Jam kerja Seminggu: "))
pegawai['lembur'] = pegawai['jam_kerja_seminggu'] > 40  # Hasilnya akan True atau False
tahunLahir = int(input("Tahun Lahir (YYYY): "))
bulanLahir = int(input("Bulan Lahir (1 - 12): "))
tanggalLahir = int(input("Tanggal Lahir (1 - 31): "))
pegawai['tanggal_masuk'] = datetime.datetime(tahunLahir,bulanLahir,tanggalLahir).date()
print(pegawai)
