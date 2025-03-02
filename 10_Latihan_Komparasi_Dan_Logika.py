""" Modul Latihan Komparasi Dan Logika """

""" Membuat gabungan area rentang dari angka
misal punya daerah :
++++++++3-------------10++++++++++++
kalo soal seperti ini harus mengambil dua daerah yang kurang dari 3
dan lebih besar dari 10
"""
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10: "))
#++++++++3-------------
#memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(isKurangDari)
isLebihDari = (inputUser > 10)
print(isLebihDari) 
#gabungan 2 daerah misal krg dari 3 atau lbh dari 10 maka true
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

""" Kasus Irisan
------3+++++10------
hanya 3 hingga 10 yang true
"""
print()
inputUser = float(input("Masukkan angka yang bernilai antara 3 hingga 10: "))
isLebihSama = inputUser >= 3
print(isLebihSama)
isKurangSama = inputUser <= 10
print(isKurangSama)
isLebihKurangsama = isLebihSama and isKurangSama
print(isLebihKurangsama)

""" PR 
1.
------0++++++++5------8+++++11--------
2.
++++++0--------5++++++8-----11++++++++
"""

inputUser = float(input("Masukkan angka\n antara 1 hingga 4\n atau\n 9 hingga 10"))
lebihDari = inputUser > 0
kurangDari = inputUser < 5
lebihDari1 = inputUser > 8
kurangDari1 = inputUser < 11
lebihKurangDari = lebihDari and kurangDari
lebihKurangDari1 = lebihDari1 and kurangDari1
correctanswer = lebihKurangDari or lebihKurangDari1
print(correctanswer)

inputUser1 = float(input("Masukkan angka\nkurang dari 0\natau\nantara 6 hingga 7\natau\nlebih dari 11"))
kurangdari0 = inputUser1 < 0
lebihdari5 = inputUser1 > 5
kurangdari8 = inputUser1 < 8
lebihdari11 = inputUser1 > 11
kurleb5hgg8 = lebihdari5 and kurangdari8
jawabanbenar = kurangdari0 or kurleb5hgg8 or lebihdari11
print(jawabanbenar)