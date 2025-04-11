data_angka = [1,3,4,5,3,4,9,0,4,4,5,6,7,8,9,7,6,6,5,7,5,3,2,2,4]
data_string = ["ayam","ikan","sapi","unta","gajah"]

# melihat jumlah item di list
jumlah_6 = data_angka.count(6)
print(f"jumlah angka 6 = {jumlah_6}")

# melihat indeks dari item list
indeks_sapi = data_string.index("sapi")
print(f"indeks dari'sapi' = {indeks_sapi}")

# mengurutkan list
data_angka.sort()
print(f"mengurutkan data angka \n{data_angka}")

data_string.sort()
print(f"mengurutkan data string \n{data_string}")

# membalikkan urutan list
data_angka.reverse()
print(f"urutan angka jika dibalik \n{data_angka}")