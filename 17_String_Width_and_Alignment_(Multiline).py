""" Modul String Width and Alignment (Multiline) """
"""Data"""
brand = "samsung"
seri = "galaxy"
tipe = "s"
urutan = 25
chipset = "snapdragon"
seri_chip = "8 elite"

"""data string standard"""
data_gabung = f"nama ponsel = {brand} {seri} {tipe}{urutan}, chipset =  {chipset} {seri_chip}"
print(data_gabung)

"""data string multiline -> memberikan \n : sebagai enter """
data_gabung = f"nama ponsel = {brand} {seri} {tipe}{urutan},\nchipset =  {chipset} {seri_chip}"
print(data_gabung)

"""data string multiline pakai kutip triplets (double kutipnya tiga) """
data_gabung = f"""
nama ponsel = {brand} {seri} {tipe}{urutan}
chipset     = {chipset} {seri_chip}
"""
print(data_gabung)
"""seperti menulis di word dan bisa sekaligus atur lebar :) :d"""

"""sama saja bedanya ini mengatur lebar. Penjelasan kode :
{' ' * 5} geser ke kanan 5"""
data_gabung = f"""
nama ponsel ={' ' * 5}{brand} {seri} {tipe}{urutan}
chipset     = {' ' * 5}{chipset} {seri_chip}
"""
print(data_gabung)