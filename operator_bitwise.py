# operator bitwise, operasi biner, binary
"""
| 'OR'
& 'AND'
^ 'XOR'
~ 'NOT'
>> 'SHIFT RIGHT'
<< 'SHIFT LEFT'

contoh : 2 --> biner : 00000010 --> lihat dari index karena 1 ada di index ke-1, maka 2^1 = 2
"""

a = 9
b = 5

"""
00000101
00001001
--------(OR)
00011010 --> menggunakan aturan komparasi misal 0 atau 0 = 0, 1 atau 0 = 1, dsb
"""
print("====OR=====")
c = a | b # dalam aturan OR seperti dijumlah saja
print("nilai :", a, "binary :", format(a,'08b')) # fungsi format() untuk memperlihatkan string
print("nilai :", b, "binary :", format(b,'08b'))
print("---------------------------(|)")
print("nilai :", c, "binary :", format(c,'08b'))

print("====AND====")
c = a & b
print("nilai :", a, "binary :", format(a,'08b'))
print("nilai :", b, "binary :", format(b,'08b'))
print("---------------------------(&)")
print("nilai :", c, "binary :", format(c,'08b'))

print("====XOR====")
c = a ^ b
print("nilai :", a, "binary :", format(a,'08b'))
print("nilai :", b, "binary :", format(b,'08b'))
print("---------------------------(^)")
print("nilai :", c, "binary :", format(c,'08b'))

print("====NOT====")
c = ~a
print("nilai :", a, "binary :", format(a,'08b'))
print("---------------------------(~)") # bernilai negatif apabila dari positif dan sebaliknya
print("nilai :", c, "binary :", format(c,'08b')) # akan dimirrorkan tetapi bukan dengan 0

# ingin di-FLIP bisa menggunakan XOR
print("---------------------------(^)")
d = 0b00001001
e = 0b11111111
print("nilai :", d ^ e, "binary :", format(d ^ e,'08b'))
# python tidak punya UNSIGNED tetapi hanya punya SIGNED 

print("SHIFT RIGHT")
c = a >> 2 # akan menggeser angka 1 ke kanan sebanyak n
print("nilai :", a, "binary :", format(a,'08b'))
print("---------------------------(>>)")
print("nilai :", c, "binary :", format(c,'08b'))

print("SHIFT LEFT")
c = a << 3 # akan menggeser angka 1 ke kiri sebanyak n
print("nilai :", a, "binary :", format(a,'08b'))
print("---------------------------(<<)")
print("nilai :", c, "binary :", format(c,'08b'))