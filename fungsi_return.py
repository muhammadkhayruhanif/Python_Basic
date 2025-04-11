# fungsi dengan return

"""
def nama_fungsi(return):
    badan fungsi
    return fungsi --> untuk mengeluarkan nilai
"""
# input --> fungsi --> output

# kuadrat
def kuadrat(angka):
    hasil = angka**2
    return hasil

x = kuadrat(4)
print(x)

# perkalian
def perkalian(angka_1,angka_2):
    return angka_1 * angka_2

print(perkalian(3,6))

hasil_tambah = 10 + perkalian(7,2)
print(hasil_tambah)

# fungsi dengan return banyak
def operasi_aritmatika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah, kurang, kali, bagi

y =operasi_aritmatika(9,5) # hasilnya tuple
print(y)

t,k,l,b = operasi_aritmatika(9,5)

print(f"hasil tambah = {t}")
print(f"hasil kurang = {k}")
print(f"hasil kali   = {l}")
print(f"hasil bagi   = {b}")