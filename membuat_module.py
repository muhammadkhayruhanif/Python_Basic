# module matematika dengan import

# from program_module import *
from program_module import tambah as add # menggunakan from dan alias
from program_module import kali as multipy
from program_module import pangkat as namanya_terserah

import program_module as math # <--- bisa dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = math.kali(2,4,6,8,10)
print(f"hasil kali = {hasil_kali}")

pangkat3 = namanya_terserah(3)
print(f"hasil pangkat 3 dari 2 = {pangkat3(2)}")