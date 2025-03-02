"""Modul String"""
data = "ini merupakan data string berjalan dengan karakter"
print(data) #print data string diatas (pada variabel data)

"""1. cara membuat string
    bisa menggunakan single quote, cth '..........'
    bisa menggunakan double quote, cth ".........."
    bisa menggunakan gabungan antara single dan double quote, cth '".........."'
    yang tujuannya adalah bisa mengeprint double quote
    catatan : tidak bisa print('ayo pergi hari jum'at') krn udh ketutup
"""

data = 'data ini merupakan string menggunakan single quote'
print(data) 
data = "data ini merupakan string menggunakan double quote"
print(data)
data = '"menggunakan gabungan single dan double quote utk menampilkan petik dua"'
print(data)
data = "'menggunakan gabungan double dan single quote utk menampilkan petik satu'"
print(data)
cthlain = "hari ini adalah jum'at"
print(cthlain)

"""2. backlash"""
""" menggunakan tanda \
    membuat tanda ' menjadi string
"""
print('ayo pergi mancing di hari kam\'is')
print('what\'s your name?')

"""backlash"""
print('C:\\users\\admin')
""" tidak bisa satu \ """

"""tab"""
print('mencoba\ttab spasi')

"""backspace"""
print('mencoba\bbackspace')

"""enter (newline)
\n tujuannya yaitu utk enter (newline)
\r tujuannya yaitu utk enter tapi dibalik(newline)"""
print('mencoba\nspasi enter') #lf -> line feed -> utk unix, macos, linux
print('mencoba\rspasi enter') #cr -> carriage return -> utk commodore, acorn, lisp
print('mencoba\r\nspasi enter') #crlf -> line feed carriage return -> utk windows

"""3. string literal atau raw"""

"""dibawah ini tidak valid dan path yang dituju tdk bisa krn tdk kebaca
dan urutan kedua bisa digunakan (menggunakan raw string)"""
print('C:\admin')
print(r'C:\admin')

"""multiline literal string :
    bisa membuat dan menampilkan kata lebih dari satu baris. serta membuat text
    panjang
    contoh :
"""
print(r"""
      username : admin
      passsword : admin123
      website : www.websiteopensource.com
      """)

