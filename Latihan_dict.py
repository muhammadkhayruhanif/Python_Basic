import string
import random

# template

mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'gender':'gender',
    'sks':'000',
    'ipk':'00'
}

data_mahasiswa = {}
# fromkeys
while True:
    print(f"{'DATA MAHASISWA':^20}")
    print("="*20)
    
    mahasiswa = dict.fromkeys(mahasiswa_template.keys()) # merubah value dari keys menjadi none
    #print(mahasiswa)

    mahasiswa['nama'] = input("masukkan nama : ")
    mahasiswa['nim'] = int(input("masukkan NIM (8 angka) : "))
    mahasiswa['gender'] = input("masukkan gender (Laki-laki/perempuan) : ")
    mahasiswa['sks'] = int(input("masukkan SKS (1-144) : "))
    mahasiswa['ipk'] = float(input("masukkan IPK (0.0) : "))

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    # dari tutorial sebelumnya
    print(f"{'KEY':<6}  {'Nama':<15}  {'NIM':<8}  {'Gender':<9}  {'SKS':<3}  {'IPK':<3}")
    print('-'*58)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]["nim"]
        GENDER = data_mahasiswa[KEY]["gender"]
        SKS = data_mahasiswa[KEY]["sks"]
        IPK = data_mahasiswa[KEY]["ipk"]

        print(f"{KEY:<6}  {NAMA:<15}  {NIM:<8}  {GENDER:<9}  {SKS:<3}  {IPK:<3}")

    is_done = input("\nMasukkan data lagi? (y/n) :")    
    if is_done == 'n':
        break

print("Program berakhir!")