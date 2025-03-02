""" *Modul Operasi Aritmatika* """

a = 10
b = 3

""" operasi tambah"""
tambah = a + b
print("a = 10, b = 3")
print("hasil penjumlahan a + b = ", tambah)
print(a, '+', b, '=', tambah )

""" operasi pengurangan"""
kurang = a - b
print("a = 10, b = 3")
print("hasil pengurangan a + b = ", kurang)
print(a, '-', b, '=', kurang )

""" operasi perkalian """
kali = a * b
print("a = 10, b = 3")
print("hasil perkalian a * b = ", kali)
print(a, '*', b, '=', kali)

""" operasi pembagian """
bagi = a / b
print("a = 10, b = 3")
print("hasil perkalian a / b = ", bagi)
print(a, '/', b, '=', bagi)

""" operasi eksponen(pangkat) '**' """
eksponen = a ** b
print("a = 10, b = 3")
print("hasil eksponen a ** b = ", eksponen)
print(a, '**', b, '=', eksponen)

""" operasi modulus hasil sisa bagi """
modulus = a % b
print("a = 10, b = 3")
print("hasil modulus a % b = ", modulus)
print(a, '%', b, '=', modulus)

""" operasi floor division kebalikan dari modulus misal 
hasil pembagian adalah 3.3 jadi 3
di bulatkan kebawah """
floor_division = a // b
print("a = 10, b = 3")
print("hasil floor division a // b = ", floor_division)
print(a, '//', b, '=', floor_division)

""" prioritas operasi, operational precedence """
x = 3
y = 2
z = 4

hasil_operasi = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil_operasi)

"""
yang dilakukan atau diprioritaskan oleh python adalah
1. ()
2. eksponen (**)
3. perkalian dan teman2 = * / % //
mana yang didahulukan di no 3? sesuai urutan!!
4. + dan -
cara hitungnya pada hasil_operasi adalah
= (3 ** 2) * 4 + (3/2) - (2%4) // 3
= (9 * 4) + 1,5 - (2//3)
= 36 + 1,5 - 0
= 37,5

kalo penjumlahannya yang dikurung duluan maka itu yg dikerjakan dulu
contoh :
"""
u = 5
i = 3
c = 5

hasil_tes = (u + i) * c
print(hasil_tes)
