#data tipe : integer
data_integer = 4
type(data_integer) #mengetahui tipe data
print(data_integer, "data tipe :", type(data_integer))

#data tipe : float
data_float = 10.2
print(data_float, "data tipe :", type(data_float))

#data tipe : string
data_string = "ini string"
print(data_string, "data tipe :", type(data_string))

#data tipe : boolean
data_bool = True
print(data_bool, "data tipe :", type(data_bool))

#data tipe : complex
data_complex = complex(3,2) #mendefinisikan bilangan imajiner, 2 sebagai imajinernya
print(data_complex, "data tipe :", type(data_complex))

from ctypes import c_double # memakai tipe data dari C (double, long, longlong, char)
data_c_double = c_double(10.32)
print(data_c_double, "data tipe : ", type(data_c_double))