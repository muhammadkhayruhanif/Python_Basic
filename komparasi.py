# setiap hasil operasi komparasi adalah boolean
"""
> lebih dari
< kurang dari
>= lebih dari sama dengan
<= kurang dari sama dengan
is
is not
"""
a = 4
b = 2

print("lebih dari (>)")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

print("kurang dari (<)")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

print("lebih dari sama dengan (>=)")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

print("kurang dari sama dengan (<=)")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

# "is" sebagai operasi komparasi object identity
"""
x = 4, x --> variabel yang memakai memori, sedangkan 4 --> literal
x akan memiliki alamat id tempat nilai disimpan
"""

x = 4
y = 4

print("nilai x = 4", "id = ", hex(id(x))) # python akan menggunakan memori yg sama karena memiliki nilai sama
print("nilai y = 4", "id = ", hex(id(y)))
komparasi_is = x is y # melihat hasil komparasi variabel dengan variabel
print(x, "is", y, "=", komparasi_is)

# "is not" kebalikan dari "is"
is_not = x is not y
print(x, "is not", y, "=", is_not)

z = 3
is_not = x is not z
print(x, "is not", z, "=", is_not)