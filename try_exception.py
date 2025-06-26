#input_contoh = int(input("masukkan angka :"))

#hasil_contoh = 10/input_contoh
#print(hasil_contoh)

"""
1. input_contoh = 0
ZeroDivisionError -> runtime error

2. print(hasil_contoh
SyntaxError

3. file = open("data.txt", "r") -> file tidak dibuat
FileNotFoundError -> runtime error
"""

input_nilai = int(input("masukkan nilai :"))
hasil = 0

try:
    hasil = 10/input_nilai

except:
    print("input tidak boleh 0")

"""
except ValueError: # Lebih spesifik menangani jika input bukan angka
    print("Input harus berupa angka.")
except ZeroDivisionError: # Menangkap error pembagian dengan nol
    print("Input tidak boleh 0.")
except Exception as e: # Tangani error lain yang mungkin terjadi
    print(f"Terjadi error tak terduga: {e}")
"""
    
print(f"hasil :{hasil}")

#contoh di aplikasi

while(True):
    inputan = int(input("masukkan angka :"))

    try:
        hasil = 10/inputan
        print(f"hasil :{hasil}")
        is_done = input("lanjutkan? (y/n)")
        if is_done == "n":
            break

    except:
        print("nilai input tidak boleh 0")

print("akhir dari program")

#contoh aplikasi untuk membuat file data.txt

"""
try:
    with open("data.txt",'r') as file:
        print(file.read())

except:
    with open("data.txt",'w',encoding='UTF-8') as file:
        file.write("file baru")
"""

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(5,6))
    
angka = 0

try:
    hasil = 10/angka
except ZeroDivisionError as error_massage:
    print(error_massage)