""" Modul Operasi Logika atau boolean """
""" ada not, or, dan xor """
print("===Not===")
a = True
c = not a
b = False
d = not b
print('data a = ', a) #menghasilkan true krn value a = true
print('data c = ', c) #menghasilkan false krn tdk sm dg a
print('data b = ', b) #menghasilkan true krn value b = false
print('data d = ', d) #menghasilkan true krn tdk sm dg d

print('operasi OR')
"""kesimpulan jika salah satu true maka hasilnya true"""
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

"""kesimpulan jika ingin menampilkan value dalam
variabel misal variabel a yang ingin ditampilkan
maka ketik huruf a. lalu untuk pemisahan gunakan tanda koma"""

print('operasi AND')
"""kesimpulan jika salah satu false maka hasilnya false"""
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

print('operasi XOR')
""" BUKAN OPERATOR LOGIKA TAPI BITWISE """
""" menghasilkan true jika salah satu true semua false """
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)