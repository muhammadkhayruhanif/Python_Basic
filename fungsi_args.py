# fungsi dengan *args

# memasukkan data/argumen

# fungsi biasa
def fungsi_biasa(nama,tinggi,berat):
    print(f"{nama} dengan tinggi {tinggi} dan berat {berat}")

fungsi_biasa("Hanif",175,65)

# fungsi dengan list
def fungsi_list(data_list):
    data = data_list.copy()

    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    
    print(f"{nama} dengan tinggi {tinggi} dan berat {berat}")

fungsi_list(["Hana",165,50])    

# fungsi *args
def fungsi_args(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]

    print(f"{nama} dengan tinggi {tinggi} dan berat {berat}")

fungsi_args("Ahmad",170,62)

# studi kasus
# *args bisa dirubah
def penjumlahan(*data):
    # data memiliki tipe tuple, dan bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil1 = penjumlahan(1,2,3,4,5)
print(f"hasil = {hasil1}")

hasil2 = penjumlahan(2,4,6,8,10)
print(f"hasil = {hasil2}")