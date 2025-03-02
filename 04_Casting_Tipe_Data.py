""" *Modul Casting Tipe Data* """
"""apa itu? merubah tipe data dari satu tipe ke tipe data lain"""
""" misal kita punya tipe data = int,float, string, bool """

data_int = 5
print("data = ", data_int, "type = ", type(data_int))

"""kode merubah tipe data"""
data_float = float(data_int)
print("data = ", data_float, "type = ", type(data_float))
data_str = str(data_int)
print("data = ", data_str, type(data_str))
data_boolean = bool(data_int)
""" akan false juga int 0 """
print("data value = ", data_boolean, "tipe data = ", type(data_boolean))

""" dari float ke int, boolean, dan string"""
d_float = 9.2
d_int = int(d_float)
""" akan selalu dibulatkan ke bawah """
print("data value = ", d_int, "tipe data = ", type(d_int))
d_boolean = bool(d_float)
print("data value = ", d_boolean, "tipe data = ", type(d_boolean))
d_string = str(d_float)
print("data value = ", d_string, "tipe data = ", type(d_string))

""" dari boolean ke int float dan string"""
print("")
print("dari boolean ke int float dan string")
print("")
dt_bool = True
df_bool = False
dt_int = int(dt_bool)
print("value = ", dt_int, "tipe data = ", type(dt_int))
dt_float = float(dt_bool)
print("value data = ", dt_float, "tipe data = ", type(dt_float))
dt_str = str(dt_bool)
print("value data = ", dt_str, "tipe data", type(dt_str))
df_int = int(df_bool)
print("value data = ", df_int, "tipe data = ", type(df_int))
df_float = float(df_bool)
print("value data = ", df_float, "tipe data = ", type(df_float))
df_str = str(df_bool)
print("value data = ", df_str, "tipe data = ", type(df_str))

print("")
print("string ke int, float, boolean")
print("")

"""string ke int, float, boolean"""
"""
1. kalo string datanya kosong =
tdk bisa convert ke int, float, tapi bool = false
2. kalo string datanya true atau false maka
tdk bisa convert ke int, float, tapi bool = true walau string false
3. string datanya angka baik itu 0 atau angka selain 0 =
bisa convert ke int, float, tapi bool = true
"""
dsg = "10"
dsg_int = int(dsg)
print("data value = ", dsg_int, "tipe data = ", type(dsg_int))
dsg_boolean = bool(dsg)
print("data value = ", dsg_boolean, "tipe data = ", type(dsg_boolean))
dsg_float = float(dsg)
print("data value = ", dsg_float, "tipe data = ", type(dsg_float))
