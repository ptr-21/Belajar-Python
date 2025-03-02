"""Modul Operator Assignment"""
""" Operasi yang dapat dilakukan dengan penyingkatkan
operasi yang ditambah dengan assignment"""

"""operasi aritmatika"""

"""cnth prtmbhn"""
a = 5 #assignment
print('nilai a= ', a)
a = a + 1 #cnth tidak pake Operator Assignment (sangat ribet)
print('nilai a= ', a)
print()
""" bisa di permudah dengan cara Assignment yaitu"""
a+= 1 #tambah 1 jadi tidak perlu a = a + 1
print('nilai a+= 1, nilai a menjadi ', a)

"""cnth pengurangan"""
b = 5
print('nilai b= ', b)
""" bisa di permudah dengan cara Assignment yaitu"""
b-= 2 #kurang 2 jadi tidak perlu b = b - 2
print('nilai b-= 2, nilai a menjadi ', b)
print()

"""cnth perkalian"""
c = 5
print('nilai c= ', c)
""" bisa di permudah dengan cara Assignment yaitu"""
c*= 2 #kali 2 jadi tidak perlu c = c * 2
print('nilai c+= 2, nilai a menjadi ', c)
print()

"""cnth pembagian"""
d = 5
print('nilai d= ', d)
""" bisa di permudah dengan cara Assignment yaitu"""
d/= 2 #kali 2 jadi tidak perlu d = d / 2
print('nilai d+= 2, nilai a menjadi ', d)
print()

"""cnth perpangkatan"""
e = 5
print('nilai e= ', e)
""" bisa di permudah dengan cara Assignment yaitu"""
e**= 2 #pangkat 2 jadi tidak perlu e = e ** 2
print('nilai e+= 2, nilai a menjadi ', e)
print()

"""cnth modulus"""
f = 5
print('nilai f= ', f)
""" bisa di permudah dengan cara Assignment yaitu"""
f%= 2 #modulus 2 jadi tidak perlu f = f % 2
print('nilai f+= 2, nilai a menjadi ', f)
print()

"""cnth floor division (pembagian bulat ke bawah)"""
g = 5
print('nilai g= ', g)
""" bisa di permudah dengan cara Assignment yaitu"""
g//= 2 #floor division 2 jadi tidak perlu g = g // 2
print('nilai g+= 2, nilai a menjadi ', g)
print()
print()
print()


"""operasi Bitwise"""
"""cnth or"""
h = True
print('nilai h =', h)
h |= False
print('nilai h = True dengan h|= False, nilai h menjadi ', h)
h = True
print('nilai h =', h)
h |= True
print('nilai h = True dengan h|= True, nilai h menjadi ', h)
h = False
print('nilai h =', h)
h |= True
print('nilai h = false dengan h|= True, nilai h menjadi ', h)
h = False
print('nilai h =', h)
h |= False
print('nilai h = false dengan h|= false, nilai h menjadi ', h)
print()

"""cnth and"""
i = True
print('nilai i =', i)
i &= False
print('nilai i = True dengan i&= False, nilai i menjadi ', i)
i = True
print('nilai i =', i)
i &= True
print('nilai i = True dengan i&= True, nilai i menjadi ', i)
i = False
print('nilai i =', i)
i &= True
print('nilai i = false dengan i&= True, nilai i menjadi ', i)
i = False
print('nilai i =', i)
i &= False
print('nilai i = false dengan i&= false, nilai i menjadi ', i)
print()

"""cnth xor"""
j = True
print('nilai j =', j)
j ^= False
print('nilai j = True dengan j^= False, nilai j menjadi ', j)
j = True
print('nilai j =', j)
j ^= True
print('nilai j = True dengan j^= True, nilai j menjadi ', j)
j = False
print('nilai j =', j)
j ^= True
print('nilai j = false dengan j^= True, nilai j menjadi ', j)
j = False
print('nilai j =', j)
j ^= False
print('nilai j = false dengan j^= false, nilai j menjadi ', j)
print()

"""cnth not"""
k = True
print('nilai k =', k)
k != False
print('nilai k = True dengan k!= False, nilai k menjadi ', k)
k = True
print('nilai k =', k)
k != True
print('nilai k = True dengan k!= True, nilai k menjadi ', k)
k = False
print('nilai k =', k)
k != True
print('nilai k = false dengan k!= True, nilai k menjadi ', k)
k = False
print('nilai k =', k)
k != False
print('nilai k = false dengan k!= false, nilai k menjadi ', k)
print()

"""cnth shifting (geser geser)"""
l = 0b0100
print('nilai l =', l)
l >>= 2
print('nilai l >>= 2, nilai l menjadi ', format(l,('04b')))
l <<= 2
print('nilai l <<= 2, nilai l menjadi ', format(l,('04b')))