daftar_negara = {
    "Asia":"Indonesia",
    "Australia":"Australia",
    "America":"Panama",
    "Europe":"British",
    "Balkan":"Albania",
    "Africa":"Maroko"
}

# coba dengan for
for negara in daftar_negara:
    print(negara) # hanya keluar keys

# melihat key saja
keys = daftar_negara.keys()
print(keys)

# melihat value saja
values = daftar_negara.values()
print(values)

# melihat items
items = daftar_negara.items()
print(items)

for key in daftar_negara.keys():
    print(key) # hanya mengeluarkan key

for value in daftar_negara.values():
    print(value)

for item in daftar_negara.items():
    print(item)

for benua,negara in daftar_negara.items():
    print(f"\nBenua: {benua}, negara: {negara}")