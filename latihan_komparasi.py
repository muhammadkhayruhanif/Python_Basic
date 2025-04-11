# latihan komparasi dan logika

# ++++3----10++++ menggunakan 'or'
inputUser = float(input("kurang dari 3 \natau \nlebih dari 10 \nmasukkan angka :")) # \n = enter5

isKurangDari = inputUser < 3
isLebihDari = inputUser > 10

isKomparasi = isKurangDari or isLebihDari
print(isKomparasi)

print("============")

# ----3++++10---- menggunakan 'and'
inputUser = float(input("lebih dari 3 \ndan \nkurang dari 10 \nmasukkan angka :"))

isLebihDari = inputUser > 3
isKurangDari = inputUser < 10

isKomparasi = isLebihDari and isKurangDari
print(isKomparasi)

print("============")

# ++++0----5++++8----11++++
inputUser = float(input("masukkan angka :"))

kasus1 = inputUser < 0
kasus2 = inputUser > 5
kasus3 = inputUser < 8
kasus4 = inputUser > 11

penyelesaian = kasus1 or kasus2 and kasus3 or kasus4
print(penyelesaian)