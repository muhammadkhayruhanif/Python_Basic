# casting adalah mengubah tipe data dari tipe data aslinya
print("====INTEGER====")
data_int = 10

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print(data_float, type(data_float))
print(data_str, type(data_str))
print(data_bool, type(data_bool)) # akan bernilai false ketika int = 0

print("====FLOAT====")
data_float = 10.9

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print(data_int, type(data_int))
print(data_str, type(data_str))
print(data_bool, type(data_bool))

print("====STRING====")
data_str = "2" #apabila variabel string tidak memuat angka maka akan 'error'

data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #apapaun nilainya akan true, kecuali string kosong
print(data_int, type(data_int))
print(data_float, type(data_float))
print(data_bool, type(data_bool))

print("====BOOLEAN====")
data_bool = True

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print(data_int, type(data_int))
print(data_float, type(data_float))
print(data_str, type(data_str))