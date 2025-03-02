"""Modul Operator Bitwise"""
"""disebut sebagai operasi biner, binary
bitwise artinya adalah operasi masing masing bit
misal ada int 2 jadi bitnya ada 8 misal
2 -> 00000010
     76543210
           2 pangkat 1 = 2
int 1 -> 00000001
                2 pangkat 0 = 1
kalo int 9 -> 00001001
                  2^3 2^0
kesimpulan semakin ke kiri pangkatnya nambah kalo kanan sendiri 0
jadi dimulai dari 0
artinya adalah semua dipangkatkan 

itu binary

kalo bitwise itu perhitungan antara binary di or kan
misal ada int 2 dan 1 maka
2 -> 000000010
1 -> 000000001
hsl  000000011
kalo 1 dan 1 maka hasilnya 000000010
sbnrnya ada selain or juga ttpan yaitu and, xor, not
"""
a = 9
b = 5

"""bitwise OR (|)"""
c = a | b
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',b,',binary: ', format(b, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))
#08b adalah format untuk menampilkan binary dn hrs tulis spt: print(format(c, '08b'))

"""bitwise AND (&)"""
c = a & b
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',b,',binary: ', format(b, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))

"""bitwise xor (^)"""
c = a ^ b
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',b,',binary: ', format(b, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))

"""bitwise not (~)"""
c = ~a
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))
#dibuat xor karena biar ga mines jawaban binernya
#kenapa hrs dibuat demikian krn maka akan dibuat mirror
#misal plus maka jwbnnya mines
d = 0b0000001001
e = 0b1111111111
print('nilai: ', e^d, 'binary: ', format(e^d, '08b'))
#untuk ngeflip agar dibalik dari min ke tdk min

#operator shifting
#Shift right pakai tanda ">>"
c = a >>1
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))
#shift left
c = a <<1
print('nilai: ',a,',binary: ', format(a, '08b'))
print('nilai: ',c,',binary: ', format(c, '08b'))