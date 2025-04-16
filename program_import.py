# sambungkan program dengan file eksternal menggunakan 'import'

print("ini adalah cara mengimport") # hasil akan langsung keluar

data = "mengimport data menggunakan namespace" # perlu menggunakan namespace untuk memanggil data

# fungsi akan langsung mengeluarkan nilai
def pangkat(a:int, b:int)->int: 
    hasil = a**b
    print(hasil)

# fungsi akan mengeluarkan nilai data harus dipanggil
def perkalian(a:int, b:int)->int:
    return a*b