# perulangan (while)

"""
while kondisi (boolean) :
    aksi ini
    aksi itu
"""

i = 0
print(f"angka pertama = {i}")

while i < 5 : # program akan berjalan per-statement
    i += 1
    print(f"angka saat ini = {i}")

print("akhir dari program")

# continue, pass, break
# selalu ingat bahwa program akan bekerja pada statement yang berurut

# pass
# sebagai dummy --> tidak akan dieksekusi

angka = 0

while angka < 5 :
    angka += 1
    print(f"angka = {angka}")

    if angka == 3 :
       pass # berfungsi untuk mengganti kode yg seharusnya diisi, tdk akan diproses
    
    print("lanjut")
print("program pass berakhir")

# continue
# melanjutkan loop ke step berikutnya
angka = 0
while angka < 5 :
    angka += 1
    print(f"saat ini = {angka}")

    if angka == 3 :
        print("sekarang 3")
        continue # ketika kondisi true maka statement selanjutnya akan di-skip

    print("selanjutnya")
print("program continue selesai")

# break

"""
berbeda dengan continue, break akan langsung menghentikan code
--> biasanya dipakai untuk pencarian, ketika ketemu maka akan 
berhenti
"""

angka = 0

while angka < 5 :
    angka += 1
    print(f"angka = {angka}")

    if angka == 3 : # 4 dan 5 tidak diprint
        print("ketemu!")
        break

print("program break selesai")

inputan = int(input("cari angka =")) # wajib ke integerkan agar tidak error!
angka = 0

while True :
    angka += 1
    print(f"angka saat ini = {angka}")

    if angka == inputan :
        print("ketemu!")
        break

print("program selesai")