data = input("masukkan data :") # input nilai
print(data, type(data)) #tipe data ketika diinput pasti string

# apabila ingin mengganti tipe data gunakan casting
input_nilai = input("masukkan angka :")
data_int = int(input_nilai)
print(data_int, type(data_int))

input_angka = int(input("masukkan nilai :"))
print(input_angka, type(input_angka))

# diperlukan teknik khusus pada tipe data boolean
data_bool = bool(input("masukkan data ke bool :"))
print(data_bool, type(data_bool)) # akan selalu bernilai true

# cara yang benar untuk tipe data boolean
data_boolean = bool(int(input("masukkan data bool baru :"))) # input harus 1 atau 0
print(data_boolean, type(data_boolean))