""" Anonymous dan lambda function
    fungsinya membuat program menjadi lebih simple
    dibawah adalah contoh lambda function
"""
result = lambda number:number**2
print(f"hasil darii lambda adalah {result(3)}")

"""Contoh lain dengan 2 input
    artinya adalah 5 pangkat 2
"""
result1 = lambda num, pow : num**pow
print(f"hasil darii lambda adalah {(result1(5,2))}")

"""Contoh lain kalo sort untuk list"""
data = ["Apple", "Samsung", "Oppo", "Vivo", "Realme"]
data.sort()
print(f"sorted list = {data}")

"""Kalo berdasarkan panjang huruf pake lambda"""
data.sort(key=lambda data:len(data))
print(f"sorted list by words len = {data}")

"""kalo ga pake lambda"""
def len_data(merk):
    return len (merk)
data.sort(key=len_data)
print(f"sorted list by words len = {data}")

"""masuk ke filter tapi dibawah ini contoh kalo tidak pake fungsi lambda"""
number_data = [1,2,3,4,5,6,7,8,9,10]
def less_than_5(number):
    return number < 5
number_data_1 = list(filter(less_than_5, number_data))
print(number_data_1)

"""ini kalo pake fungsi lambda"""
number_data_filter = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
number_data_filter_1 = list(filter(lambda x:x<5, number_data_filter))
print(number_data_filter_1)

"""contoh lain kalo mau ambil genap"""
number_data_filter_2 = list(filter(lambda x:(x%2==0), number_data_filter))
print(number_data_filter_2)

"""contoh lain kalo mau ambil ganjil"""
number_data_filter_2 = list(filter(lambda x:(x%2!=0), number_data_filter))
print(number_data_filter_2)

"""contoh lain kalo mau kelipatan 3"""
number_data_filter_3 = list(filter(lambda x:(x%3==0), number_data_filter))
print(number_data_filter_3)

"""anonymouse function
    currying atau haskell curry
    tekniknya menggunakan lambda dan mengembangkannya
"""
def pangkat(number, n ):
    result = number**n
    return result
result_data = pangkat(5,2)
print(f"kalo pake normal function {result_data}")

"""ini kalo pake currying
    lambda itu sebuah fungsi tapi anonymouse (belum punya nama variabel)
    ket :
    pangkatn = pangkat(5) 5 itu adalah n nya
    print(f"pangkat 5 = {pangkatn(10)}") 10 itu di numbernya
"""
def pangkat(n):
    return lambda number:number**n
pangkatn = pangkat(5)
print(f"pangkat 5 = {pangkatn(10)}")

"""atau bisa gini (karena n itu adalah nilai pangkat maka n di dahulukan sesuai dengan def pangkat n)"""
print(f"hasil dari 5 pangkat 4 adalah {(pangkat(4)(5))}")
