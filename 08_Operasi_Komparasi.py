""" *Modul Operasi Komparasi* """
""" > membandingan nilai 
setiap hasil dari Operasi Komparasi menghasilkan true dan false
operasinnya adalah :
>, <, >=, <=, ==, !=, is, is not
lbh bsr, lbh kcl, lbh bsr sm dgn, lbh kcl sm dgn, sm dgn, tdk sm dgn, is, is not
"""

a = 4
b = 2
c = 5
d = 4

print("operator lebih dari dengan")
print()
tes = a > 3
print (a, '>', 3, '=', tes)
tes1 = a < 3
print (a, '<', 3, '=', tes1)

print()
print("operator kurang dari dengan")
print()
tes2 = a < 5
print (a, '>', 5, '=', tes2)
tes3 = a > 5
print (a, '>', 5, '=', tes3)

print()
print("operator lebih dari sama dengan")
print()
ls = a>=d
ls1 = a>=b
ls2 = a>=c
print (a, '>=', d, '=', ls)
print (a, '>=', b, '=', ls1)
print (a, '>=', c, '=', ls2)

print()
print("operator kurang dari sama dengan")
print()
ks = a<=d
ks1 = a<=c
ks2 = a<=b
print (a, '<=', d, '=', ks)
print (a, '<=', b, '=', ks1)
print (a, '<=', c, '=', ks2)

print()
print("operator sama dengan")
print()
sd = a==d
sd1 = a==c
sd2 = a==b
print (a, '==', d, '=', sd)
print (a, '==', b, '=', sd1)
print (a, '==', c, '=', sd2)

print()
print("operator tidak sama dengan")
print()
tsd = a!=d
tsd1 = a!=c
tsd2 = a!=b
print (a, '!=', d, '=', tsd)
print (a, '!=', b, '=', tsd1)
print (a, '!=', c, '=', tsd2)

""" is sebagai komparasi object identity"""

a = 5
b = 5
c = 3
print('nilai a =',a,',id = ',hex(id(a)))
print('nilai b =',b,',id = ',hex(id(b)))

print(id(a)) #menampilkan address memory
print(hex(id(b)))
coba = a is b
cobaa = a is c
print('a is b = ', coba)
print('a is c = ', cobaa)
coba1 = a is not c
cobaa1 = a is not b
print('a is not c = ', coba1)
print('a is not b = ', cobaa1)

"""
*Kesimpulan atau rangkuman*

Komparasi Selain is dan is not (spt >, <, >=, <=, ==, !=)
dapat bekerja pada syntax literal apa itu? spt a == 4
Kenapa demikian ?
Krn a ada nilainya sedangkan 4 di sebut sebagai literal krn tdk ada var nya
a itu memakan memori
Kalo 4 tidak memakan memori krn dia hidup sebaris dengan a
Jadi a bisa dipanggil lain di baris berikutnya

Is itu dapat digunakan untuk membandingkan komparasi antara 
nilai yang memakan memori, dengan membandingkan object

Membandingkan memori antara object istilahnya

Jadi a yang is 
Misal a is 4 itu tdk bs

Yang bisa adalah
a = 4
b = 4

a is b = hasilnya true

Jangan gunakan is kalo bandingin dengan literal spt a is 5 
krn tdk bs dan is atau is not tdk dpt bekerja dg literal
"""
