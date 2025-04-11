# contoh generic
biasa = "World!"
print("Hello " + biasa)
# string
format_str = f"Hello {biasa}"
print(format_str)

# boolean
bool = False
format_bool = f"boolean = {bool}"
print(format_bool)

# angka
angka = 2006.5
format_angka = f"angka = {angka}"
print(format_angka)

# bilangan bulat
bil_bulat = 18
format_bil = f"bilangan bulat = {bil_bulat:d}" # float --> error
print(format_bil)

# bilangan dengan ordo ribuan
ribuan = 7000
jutaan = 1000000
format_ribuan = f"bilangan ribuan = {ribuan:,}" # menampilkan ',' pada ribuan
print(format_ribuan)
format_jutaan = f"bilangan jutaan = {jutaan:,}"
print(format_jutaan)

# bilangan desimal
desimal = 1225.2024
format_desimal = f"ubah desimal jadi 2 saja = {desimal:.2f}" # titik dan 2 angka tipe float di belakang
print(format_desimal)

# menampilkan leading zero
desimal = 1225.2024
format_zero = f"tambah dua nilai 0 di depan = {desimal:011.3f}"
print(format_zero)


# menampilkan tanda + atau -
minus = -10
plus = 10
desimal = -10.21
format_minus = f"memuat tanda (-) = {minus:+d}"
format_plus = f"memuat tanda (-) = {plus:+d}"
format_desimal = f"memuat tanda (-) = {desimal:+2f}"
print(format_minus)
print(format_plus)
print(format_desimal)

# memformat persentase
persen = 0.124
format_persen = f"persen = {persen:.3%}" # 3 angka di belakang koma
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 25000
terjual = 31
format_aritmatika = f"jumlah penjualan = {harga*terjual}"
print(format_aritmatika)

# format angka lain (binary, octal, hexadicimal)
bilangan = 255
format_binary = f"binary = {bin(bilangan)}"
format_octal = f"octal = {oct(bilangan)}"
format_hex = f"hexadesimal = {hex(bilangan)}"
print(format_binary)
print(format_octal)
print(format_hex)