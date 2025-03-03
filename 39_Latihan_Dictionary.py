""" Modul Latihan Dictionary """
import datetime
import random
import string
"""Template Dictionary Pegawai"""
template_pegawai = {
    'nama' : 'nama',
    'id_pegawai' : '000000',
    'jam_kerja_seminggu' : 0,
    'lembur' : False,
    'tanggal_masuk' : datetime.datetime(1111,1,1)
}
data_pegawai = {}
while True :
    print(f"{'DATA PEGAWAI':^20}")
    print("-"*20)

    pegawai = dict.fromkeys(template_pegawai.keys()) 
    """mengambil key dari template_pegawai"""
    print(pegawai)
    pegawai['nama'] = input("Nama Pegawai: ")
    pegawai['id_pegawai'] = input("ID Pegawai: ")
    pegawai['jam_kerja_seminggu'] = int(input("Jam kerja Seminggu: "))
    pegawai['lembur'] = pegawai['jam_kerja_seminggu'] > 40 
    """ Hasilnya akan True atau False """
    tahunMasuk = int(input("Tahun Masuk (YYYY): "))
    bulanMasuk = int(input("Bulan Masuk (1 - 12): "))
    tanggalMasuk = int(input("Tanggal Masuk (1 - 31): "))
    pegawai['tanggal_masuk'] = datetime.datetime(tahunMasuk,bulanMasuk,tanggalMasuk).date()
    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_pegawai[KEY] = pegawai
    print(pegawai)
    print(f"\n{'KEY':<6}{'Nama':<17} {'ID Pegawai':<8} {'Jam kerja Seminggu':<10} {'Lembur':<5} {'Tanggal Masuk':<10}")
    print('-'*75)
    for pegawai in data_pegawai:
        KEY = pegawai #untuk nambah data dan parsing di for pegawai
        NAMA = data_pegawai[KEY]['nama']
        IDPEGAWAI = data_pegawai[KEY]['id_pegawai']
        JAMKERJASEMINGGU = data_pegawai[KEY]['jam_kerja_seminggu']
        LEMBUR = data_pegawai[KEY]['lembur']
        TANGGALMASUK = data_pegawai[KEY]['tanggal_masuk'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {IDPEGAWAI:<8} {JAMKERJASEMINGGU:<10} {LEMBUR:<5} {TANGGALMASUK:<10}")
    print("\n")
    is_done = input("Apakah anda ingin tambah data lagi (y/n)? ")
    if is_done == "n":
        break
print("program telah selesai, terimakasih")
