"""Modul Dictionary"""
""" List -> sebagai pengganti array di python, 
    mengakses data dengan menggunakan index misal kalo index 0 yang
    diambil maka [0]
    Perbedaan Dictionary dengan List adalah :
    Dictionary adalah associative array
    menggunakan identifier untuk mengakses datanya atau key yang tidak perlu 
    menggunakan index untuk mengaksesnya
    dictionary itu collection yang bisa mengakses data berupa apapun
"""
dataList = ['samsung','vivo','oppo']
dataDict = {
    'a' : "samsung",
    'b' : "Apple",
    'c' : 24,
    'd' : dataList

}
print(f"data di dalam dictionary : {dataDict}")
"""print akses merk berdasarkan key"""
print(f"data di dalam b : {dataDict['b']}")
"""kegunaannya adalah membutuhkan sebuah data yang memiliki struktur"""
print(f"data di dalam c : {dataDict['c']}")
print(f"data List : {dataDict['d']}")