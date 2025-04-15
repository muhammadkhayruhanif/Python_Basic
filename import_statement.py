# import -> mengambil program dari eksternal .py

# 1. menyambungkan program dari eksternal
import program_import

# 2. import dengan data
# data ada di namespace variable
print(program_import.data)

# 3. import dengan fungsi
program_import.pangkat(4,2)

hasil = program_import.perkalian(5,6)
print(hasil)