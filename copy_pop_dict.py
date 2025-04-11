daftar_negara = {
    "Asia":"Indonesia",
    "Australia":"Australia",
    "America":"Panama",
    "Europe":"British",
    "Balkan":"Albania",
    "Africa":"Maroko"
}

# copy
print(f"dictionary asli = {daftar_negara}\n")

benua_negara = daftar_negara # hasilnya memiliki id yg sama

print(f"dictionary copy = {benua_negara}\n")

# copy menggunakan method
nama_negara = daftar_negara.copy() # akan menghasilkan id berbeda
print(f"dicopy dengan method = {nama_negara}\n")

daftar_negara["Asia"] = "Jepang"

print(f"hasil asli = {daftar_negara}\n")
print(f"hasil copy biasa = {benua_negara}\n")
print(f"hasil copy method = {nama_negara}\n")

# pop dictionary (hanya item yg diinginkan)
data_baru = daftar_negara.pop("Balkan")
print(f"hasil pop = {data_baru}\n")

print(f"dictionary hasil pop = {daftar_negara}\n")

# popitem (item terakhir saja)
data_new = daftar_negara.popitem()
print(f"hasil popitem = {data_new}\n")

print(f"dictionary hasil popitem = {daftar_negara}\n")