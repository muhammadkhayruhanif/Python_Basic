## global dan local scope

nama_global = "hanif" # ini adalah variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"nama dia = {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop ke-{i} {nama_global}")

# akses variabel global dalam percabangan
if True:
    print(f"nama saya adalah {nama_global}")

## variabel local scope
def fungsi3():
    variabel_local = "lokalnya"

fungsi3()
#print(variabel_local) -> tidak dapat di-print karena berada dalam fungsi

# contoh 1: penggunaan
buah = "apel"

def fungsi2(buah):
    buah = "nanas"

fungsi2("jeruk")
print(buah)

angka = 0

def fungsi_local(nilai_baru):
    angka = nilai_baru # hanya nilai lokal
    angka += 1

fungsi_local(10) # tidak akan berjalan
print(angka)

# contoh 2: merubah variabel global
angka = 10
name = "KHANIF"

def fungsi_global(nilai_baru_lagi,nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru_lagi
    name = nama_baru

print(f"sebelum {angka,name}")
fungsi_global(15,"hanivers")
print(f"setelah {angka,name}") # akan berubah

# contoh 3: tidak berlaku untuk loop dan percabangan
number = 0

for i in range(0,5):
    number += i
    number_dummy = 4

print(number)
print(number_dummy)

if True:
    number = 12
    number_dummy = 12

print(number)
print(number_dummy)