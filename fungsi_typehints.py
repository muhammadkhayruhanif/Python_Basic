"""
def fungsi_biasa(argument):
    hasil = argument**2
    return argument

print(fungsi_biasa(4))

fungsi_biasa(2.33)

fungsi_biasa("Roti") # akan error
"""

# fungsi dengan type hints
def fungsi_hints(argument:int):
    hasil = argument**2
    return hasil

print(fungsi_hints(10))
print(fungsi_hints(3.5))
# fungsi_hints("roti") --> akan error (walaupun di python tdk ada problem)

"""
'''type hints di C++ (tidak seperti python)'''

int pangkat(int angka):
"""

# type hints seperti C++
def perpangkatan(arguments:int) -> int: # fungsinya hanya untuk memberi informasi
    hasilnya = 2**arguments
    return hasilnya

print(perpangkatan(10))
print(perpangkatan(2.5))
# print(perpangkatan("roti")) --> tetap error

# ketika memiliki baris code yang banyak fungsi type hints untuk mempermudah informasi