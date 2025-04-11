## looping list dan enumerate

kumpulan_angka = [1,3,2,4,5,5,6,4,5,9,0,8]

# for loop dan range
for i in kumpulan_angka :
    print(f"angka = {i}")

# while loop
panjang = len(kumpulan_angka)

while i < panjang :
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
data = [1,3,"lima","tujuh",9,2]

[print(f"data = {i}") for i in data]

# enumerate
# bisa memunculkan indeks dan item sekaligus
for index,item in enumerate(data) :
    print(f"indeks = {index}, data = {item}")