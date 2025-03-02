""" *Modul Tipe Data* """

#mencari tau tipe data yang digunakan
int = 1
print("value: ", int)
print("tippe data yang digunakan: ",type(int))
float = 5.5
print("value: ", float)
print("tipe data yang digunakan: ", type(float))
string = "tes data"
print("isi data string: ", string)
print("tipe data yang digunakan: ", type(string))
boolean = False
print("isi data boolean : ", boolean)
print("tipe data: ", type(boolean))

# tipe data khusus
# bilangan kompleks atau ada imajiner
dataComplex = complex(5,6)
print("isi dataComplex: ", dataComplex)
print("tipe data: ", type(dataComplex))

#tipe data  dari bahasa c 
#tapi harus import packaging c
#tujuannya agar bissa mengugnakan tipe data yang tidak ada di python
from ctypes import c_double
data_c_double = c_double(5.5)
print("isi data dari data_c_double: ", data_c_double)
print("tipe data dati data_c_double ", type(data_c_double))

"""tipe data yang ada di python ada di output semua"""