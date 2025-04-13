# Lambda
def fungsi_kuadrat(angka):
    return angka**2

print(f"kuadrat dari fungsi = {fungsi_kuadrat(4)}")

# menggunakan lambda
# output = lambda argument: expression 
kuadrat= lambda angka: angka**2
print(f"kuadrat dengan lambda = {kuadrat(2)}")

# sorting
data_list = ["dua", "empat", "delapan"]
data_list.sort()
print(f"sorted list = {data_list}") # berdasarkan urutan alfabet

# sorting menggunakan jumlah huruf
data_list.sort(key=len)
print(f"sorting menggunakan key dalam sort = {data_list}")

# sorting data menggunakan alfabet
def alfabet(huruf):
    return len(huruf)

data_list.sort(key=alfabet)
print(f"sorting menggunakan fungsi alfabet = {data_list}")

# sort menggunakan lambda
data_list.sort(key = lambda huruf: len(huruf))
print(f"menggunakan lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# cara fungsi biasa
def kurang_dari_lima(angka):
    return angka<5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(f"data baru = {data_angka_baru}")
data_angka_baru = list(filter(lambda angka: angka<10, data_angka))
print(f"data baru dengan lambda = {data_angka_baru}")

# kasus ganjil
data_ganjil = list(filter(lambda x: (x%2==0), data_angka))
print(f"data ganjil = {data_ganjil}")

# kasus genap
data_genap = list(filter(lambda x: (x%2!=0), data_angka))
print(f"data genap = {data_genap}")

# anonymous
# currying -> Haskell Curry

# cara biasa
def pangkat(angka,n):
    return angka**n

print(pangkat(3,5))

# dengan currying
def pangkat(n):
    return lambda angka: angka**n

pangkat2 = pangkat(2)
print(f"pangkat2 dari 5 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat3 dari 2 = {pangkat3(2)}")

# nilai bebas
print(f"pangkat bebas = {pangkat(2)(3)}") # pangkatnya dulu baru nilai yang dipangkatin