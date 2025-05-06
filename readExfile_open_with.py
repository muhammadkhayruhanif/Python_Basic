## Tutorial membaca file eksternal

print(4*"=", "Membaca file txt", 3*"=")
file = open("teks.txt", mode="r") # mode = "r" -> read, "w" -> write

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# print(file.read()) -> print semua baris di file txt

print(file.readline()) # baca baris pertama
print(file.readline(),end="") # baca baris kedua

print(file.readline(),end="") # "end" menghilangkan \n (akhir dari baris terdapat \n)
# print sudah berfungsi untuk enter

## baca semua baris sebagai list
print(file.readlines())

"""
# mengclose program
print(f"apakah file sudah diclose: {file.closed}")
file.closed()
print(f"apakah file sudah diclose: {file.closed}")
"""

# salah satu teknik membuka file di python

print(4*"=", "Membaca file txt dengan with", 3*"=")

with open("teks.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose: {file.closed}") # akan langsung ditutup ketika selesai menjalankan
    
print(f"apakah file sudah diclose: {file.closed}")