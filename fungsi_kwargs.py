'''**kwargs'''

# fungsi biasa
def fungsi_biasa(nama,tinggi,berat):
    print(f"{nama} memiliki tinggi {tinggi} dengan berat {berat}")

fungsi_biasa("Hanif",175,65)

# fungsi dengan **kwargs
def fungsi_kwargs(**kwargs): # akan menghasilkan dictionary
    print(kwargs)
    nama = kwargs["nama"] # memunculkan data dari key
    print(nama)

fungsi_kwargs(nama="Hanivers",tinggi=180,berat=70)

# fungsi dengan *args dan **kwargs
def fungsi_args_kwargs(*args,**kwargs):
    return args,kwargs

hasilnya = fungsi_args_kwargs(1,2,3,4,5,6,tipe="dictionary")
print(hasilnya)

# studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    else:
        print("tidak ada output")

    return output

hasil1 = math(1,2,3,4,5,option="tambah")
print(f"hasil tambah = {hasil1}")

hasil2 = math(1,2,3,10,5,option="kali")
print(f"hasil kali = {hasil2}")

hasil3 = math(1,2,3,4,option="bagi")