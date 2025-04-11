mahasiswa1 = {
    'nama':"Hanif hanivers",
    'nim':'01234567',
    'gender':'Laki-laki',
    'sks':56,
    'ipk':3.6
}

mahasiswa2 = {
    'nama':"Surto Narto",
    'nim':'01234589',
    'gender':'Laki-laki',
    'sks':38,
    'ipk':3.9
}

mahasiswa3 = {
    'nama':"Hana Maya",
    'nim':'01233462',
    'gender':'Perempuan',
    'sks':104,
    'ipk':3.3
}

mahasiswa4 = {
    'nama':"Yono Mulyo",
    'nim':'01234897',
    'gender':'Laki-laki',
    'sks':136,
    'ipk':3.1
}

mahasiswa5 = {
    'nama':"Tuti Tatitu",
    'nim':'01234982',
    'gender':'Perempuan',
    'sks':96,
    'ipk':3.9
}

# nested dictionary
data_mahasiswa = {
    'MHS001':mahasiswa1,
    'MHS002':mahasiswa2,
    'MHS003':mahasiswa3,
    'MHS004':mahasiswa4,
    'MHS005':mahasiswa5
}

#print(data_mahasiswa)

# < rata kiri
# > rata kanan
# ^ rata tengah

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