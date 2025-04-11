a = 5

# assignment penjumlaha
a += 1
print("a += 1 =", a)

# assignment pengurangan
a -= 2 # akan menggunakan nilai terakhir
print("a -= 2 =", a)

# assignment perkalian
a *= 5
print("a *= 5 =", a)

# assignment pembagian
a /= 2
print("a /= 2 =", a)

# assignment modulo
a %= 3
print("a %= 3 =", a)

# assignment floor division
b = 15
print("b = 15")
b //= 4
print("b //= 4 =", b)

# assignment eksponen
c = 10
print("c = 10")
c **= 3
print("c **= 3 =", c)

# operasi assignment bitwise

# assignment OR
d = True
print("d =", d)
d |= False
print("d |= false, d bernilai :", d)
d |= True
print("d |= true, d bernilai :", d)

# assignment AND
d = True
print("d =", d)
d &= False
print("d &= false, d bernilai :", d)
d &= True
print("d &= true, d bernilai :", d)

# assignment XOR
d = True
print("d =", d)
d ^= False
print("d ^= false, d bernilai :", d)
d ^= True
print("d ^= true, d bernilai :", d)

# assignment SHIFTING

# assignment SHIFTING RIGHT
e = 0b00001000
print("nila e :", format(e,'08b'))
e >>= 2
print("e >>= 2, nilai e menjadi :", format(e,'08b'))

# assignment SHIFTING LEFT
e <<= 1 # menggunakan nilai terakhir
print("e <<= 1, nilai e menjadi :", format(e,'08b'))