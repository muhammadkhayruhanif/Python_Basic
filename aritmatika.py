a = 10
b = 3

print("a =", a, "b =", b)

# penjumlahan +
hasil = a + b
print("penjumlahan :", hasil)

# pengurangan -
print("pengurangan :", a - b)

# perkalian *
print("perkalian :", a * b)

# pembagian /
print("pembagian :", a / b) # hasil akan menjadi float

# eksponen **
print("pemangkatan :", a ** b)

# modulus %
print("modulo :", a % b)

# pembagian kebawah (floor division) //
print("floor :", a // b)

# prioritas operasi (operational precedence)

x = 3
y = 2
z = 5

prioritas = x ** y * z / y + x - z % y // x 
print("prioritas operasi :", prioritas)

kurung = (x + y) * z
print("hasil kurung :", kurung)

# urutan prioritas
"""
1. kurung ()
2. eksponen **
3. perkalian, pembagian, dsb * / % //
4. pertambahan dan pengurangan + -
"""