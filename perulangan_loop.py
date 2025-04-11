# perulangan (loop)

"""
for kondisi :
    aksi
"""

# menggunakan list
angka1_list = [0,2,4,5,7,9]

for i in angka1_list :
    print(f"hasil perulangan = {i}")

print("akhir program ke-1 \n")

# menggunakan range
angka2_range = range(5) # dari 0 sampai 4 

for i in angka2_range :
    print(f"hasil perulangan = {i}")

print("akhir program ke-2 \n")

# menggunakan range
angka2_range = range(1,5) # dari 1 sampai 4

for i in angka2_range :
    print(f"hasil perulangan = {i}")

print("akhir program ke-3 \n")

# menggunakan string
data1_string = "ini adalah looping"

for huruf in data1_string :
    print(huruf)

print("akhir dari program ke-4")