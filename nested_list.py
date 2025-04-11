# list biasa
data_0 = [1,2]
data_1 = [3,4]
data_gabung = [1,2,3,4]

# nested list / list bersarang
nested_list_1 = [data_0,data_1]
print(nested_list_1)

nested_list_2 = [[1,2],[5,6]]
print(nested_list_2)

nested_list_3 = [data_0,data_1,5,6]
print(nested_list_3)

# contoh penggunaan
peserta_1 = ["Asep",20,"Laki-laki"]
peserta_2 = ["Ayu",19,"Perempuan"]
peserta_3 = ["Budi",21,"Laki-laki"]
peserta_4 = ["Adi",18,"Laki-laki"]

list_gabungan = [peserta_1,peserta_2,peserta_3,peserta_4]
print(f"list gabungan \n{list_gabungan}")

for peserta in list_gabungan :
    print(f"nama \t: {peserta[0]}")
    print(f"umur \t: {peserta[1]}")
    print(f"gender \t: {peserta[2]}\n")

# mengcopy nested list
list_copy = list_gabungan.copy()

peserta_1[0] = "Bayu"
print(f"dari list copy \n{list_copy}")
print(f"dari list asli \n{list_gabungan}") # tetap berubah, maka diperlukan teknik lain

## deep copy nested list

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]

# memanggil data 
data_ke_1 = data_2D[0][1] # memanggil data list pertama item kedua
print(data_ke_1)

# mengcopy data
data_2D_copy = data_2D.copy()
print(f"adress data asli = {hex(id(data_2D))}")
print(f"adress data copy = {hex(id(data_2D_copy))}") # shallow copy --> belum semuanya kecopy

# deep copy 

from copy import deepcopy

data_2D_deepcopy = deepcopy(data_2D)
print(f"adress data asli = {hex(id(data_2D))}")
print(f"adress data deep = {hex(id(data_2D_deepcopy))}")

data_0 [0] = 20

print(f"data asli = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")