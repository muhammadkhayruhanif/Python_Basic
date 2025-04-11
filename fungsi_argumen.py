# def --> definition
"""
def nama_fungsi(argumen/parameter/input):
    badan fungsi
"""

# fungsi dengan argumen
def hello(nama):
    print(f"halo, selamat datang {nama}!")

hello("Hanif")

# fungsi dengan argumen untuk angka
def penjumlahan(angka_1,angka_2):
    jumlah = angka_1 + angka_2
    print(f"jumlah dari {angka_1} + {angka_2} = {jumlah}")

penjumlahan(100,50)

# fungsi dengan argumen menggunakan list
def restoran(nama_menu):
    daftar_menu = nama_menu.copy()
    for menu in daftar_menu:
        print(f"menu {menu}")

makanan_menu = ["nasi goreng", "ayam bakar", "soto betawi", "rujak"]

restoran(makanan_menu)