# template
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'gender':'gender',
    'sks':'000',
    'ipk':'00'
}

# fromkeys
print(f"{'DATA MAHASISWA':^20}")
print("="*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # merubah value dari keys menjadi none
#print(mahasiswa)

mahasiswa['nama'] = input("masukkan nama : ")
mahasiswa['nim'] = int(input("masukkan NIM (8 angka) : "))
mahasiswa['gender'] = input("masukkan gender (Laki-laki/perempuan) : ")
mahasiswa['sks'] = int(input("masukkan SKS (1-144) : "))
mahasiswa['ipk'] = float(input("masukkan IPK (0.0) : "))

print(mahasiswa)