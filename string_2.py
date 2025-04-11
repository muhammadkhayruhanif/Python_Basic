# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Muhammad"
nama_terakhir1 = "Khayru"
nama_terakhir2 = "hanif"
concatenate = nama_pertama + " " + nama_terakhir1 + nama_terakhir2 # fungsi " " untuk memberikan spasi
print(concatenate)

# 2. mengukur panjang string
panjang = len(concatenate)
print("panjang dari", concatenate, "=", panjang) # spasi juga dihitung

# 3. operator pada string
# mengecek apakah terdapat komponen char atau string di string
#concatenate = Muhammad Khayruhanif
Y = "Y" # char
status = Y in concatenate # ada dalam string
print("'Y' teradapat pada 'Muhammad Khayruhanif' =", status) # false --> Y berbeda dengan y ( meskipun ada dalam string)

nif = "nif" # string
status = nif in concatenate
print("'nif' terdapat pada 'Muhammad Khayruhanif =", status) # true --> "nif" ada di string

Muh = "Muh"
status = Muh not in concatenate # tidak ada dalam string
print("'Muh' tidak terdapat pada 'Muhammad Khayruhanif =", status) # false --> "Muh" ada di string

# mengulang string
print("wk"*5) # di akhir
print(7*"ha") # di awal

# indexing --> index dimulai dari 0
cari_index = concatenate[0] # string pada index ke-0
print("index ke-0 =", cari_index)

cari_index = concatenate[8] # string pada index ke-8
print("index ke-8 =", cari_index) # index ke-8 = " ", spasi termasuk string

cari_index = concatenate[-1] # string pada index ke-(-1)
print("index ke-(-1) =", cari_index) # string paling akhir --> karena -0 = 0

# indexing dari n ke m
kata_index = concatenate[0:4] # dari 0 sampai 3 --> 4-0 (string terakhir tidak masuk)
print("index dari 0 sampai 3 =", kata_index)

kata_index = concatenate[3:8]
print("index dari 3 sampai 7 =", kata_index)

kata_index = concatenate[0:20:2] # index dari 0 ke 20 dijeda 2
print("index ke [0,2,4,6,...,18] =", kata_index)

# item terkecil (min)
string_min = min(concatenate) # " " --> spasi merupakan item terkecil di string
print("item terkecil =", string_min)

# item terbesar (max)
string_max = max(concatenate) # "y" --> a,b,c,...,y terbesar
print("item terbesar =", string_max)

# ASCII
ascii_code = ord(" ")
print("ASCII code untuk spasi = " + str(ascii_code))

ascii_code = ord("y")
print("ASCII code untuk 'y' = " + str(ascii_code))

data = 117
print("char untuk ASCII 117 = " + chr(data))

# operator dalam bentuk method
nama = "raja purba sasakala nirwana"
jumlah = nama.count("a") # method --> string (objek) nempel dengan methodnya --> Object Oriented Programming
print(" jumlah string 'a' pada " + nama + " = " + str(jumlah))