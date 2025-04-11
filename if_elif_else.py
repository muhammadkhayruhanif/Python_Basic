# if dan else

"""
1. if nya
2. kondisinya
3. aksinya
"""
# program sebelumnya
nama = input("masukkan nama :")
# if kondisi : aksi
# program selanjutnya

# program if inline
if nama == "hanif" : print("halo hanif!")

# program if indentation
if nama == "hanif" : # kondisi bersifat boolean (true/false)
    print("selamat datang, hanif!")
    print("selamat bersenang-senang!")
# else (hasil selain nilai true)
else :
    print("anda bukan hanif!")

"""
if kondisi 1 :
    aksi true 1

elif kondisi 2 :
    aksi true 2

elif kondisi 3 :
    aksi true 3
    
else :
    aksi false
"""
nama = input("masukkan nama lagi :")

if nama == "abe" : # kondisi true 
    print("halo abe!") # aksi true 

elif nama == "bece" : 
    print("hai bece!")

elif nama == "zeze" :
    print("selamat datang zeze!")

else : # kondisi false semua
    print("kamu siapa?") # aksi false

print("akhir dari program")