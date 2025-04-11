# fungsi default

# def fungsi_biasa (argumen)
# def fungsi_default (argumen = "value")

# fungsi biasa
def fungsi_biasa(nama):
    print(f"hai {nama}!")

fungsi_biasa("Hanif")
# fungsi_biasa --> akan error

# fungsi dengan default
def fungsi_default(makanan = "roti"):
    print(f"saya makan {makanan}")

fungsi_default("ayam bakar")
fungsi_default() # tetap akan berjalan

# fungsi dengan default ke-2
def perpangkatan(angka,pangkat = 2):
    hasil = angka**pangkat
    return hasil

print(perpangkatan(5,3)) # biasa

defaultnya = perpangkatan(5)
print(defaultnya)

dibalik = perpangkatan(pangkat = 4, angka = 2)
print(dibalik)