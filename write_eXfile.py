# 1. mode write

# akan membuat file baru jika ada,
# lalu akan overwrite isinya
# overwrite -> menghapus dan menimpa

with open("newtext_1.txt","w",encoding="utf-8") as file:
    file.write("data satu baris-1")

with open("newtext_1.txt","w",encoding="utf-8") as file:
    file.write("data satu baris-2")

with open("newtext_1.txt","w",encoding="utf-8") as file:
    file.write("overwrite")

# 2. mode append -> menambahkan isi tanpa menghapus dan menimpa

with open("newtext_2.txt","a",encoding="utf-8") as file:
    file.write("data dua baris-1\n")

with open("newtext_2.txt","a",encoding="utf-8") as file:
    file.write("data dua baris-2\n")

with open("newtext_2.txt","a",encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# 3. mode r+ -> menimpa isi teks sesuai panjang data

with open("newtext_3.txt","r+",encoding="utf-8") as file:
    file.write("data ke-3\n")

with open("newtext_3.txt","r+",encoding="utf-8") as file:
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")
    file.write("baris ke-3\n")

with open("newtext_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("newtext_3.txt","r+",encoding="utf-8") as file:
    file.write("nimpa")