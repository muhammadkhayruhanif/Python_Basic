import numpy as np

list_a = [1,2,3,4]
print(f"list_a = {list_a}")

vektor_a = np.array([1,2,3,4])
print(f"vektor_a = {vektor_a}")

print(f"list x2 = {list_a*2}")
print(f"vektor x2 = {vektor_a*2}")


# print(f"list^2 = {list_a**2}") -> tidak bisa
print(f"vektor^2 = {vektor_a**2}")

matriks_b = np.array([(1,2),(3,4)])
print(f"matriks_b (ordo 2x2) = \n{matriks_b}")

print(f"matriks_b^2 (ordo 2x2) = \n{matriks_b**2}")

matriks_zeros = np.zeros([2,2])
print(f"matriks zeros atau matriks nol (ordo 2x2) = \n{matriks_zeros}")

matriks_ones = np.ones([2,2])
print(f"matriks ones atau matriks satu (ordo 2x2) = \n{matriks_ones}")

penjumlahan_matriks = matriks_b**2 + matriks_ones
print(f"penjumlahan dari matriks_b pangkat 2 + matriks satu = \n{penjumlahan_matriks}")