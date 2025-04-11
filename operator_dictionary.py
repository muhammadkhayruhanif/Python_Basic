# bentuk dictionary
data_dict = {
    "nama":"hanif",
    "kelas":28,
    "gender":"laki-laki",
    "usia":"20 tahun",
}

## mencari panjang dictionary
lendict = len(data_dict)
print(f"panjang dari dict : {lendict}")

## mengecek key exist atau tidak
KEY = "usia"
CHECKKEY = KEY in data_dict
print(f"cek {KEY} ada di dict : {CHECKKEY}")

CHECKKEY = "agama" in data_dict
print(f"cek agama ada di dict : {CHECKKEY}")

## memanggin value menggunakan get
ambil_value = data_dict["nama"]
print(f"ambil nilai menggunakan key biasa \n{ambil_value}")

ambil_value_get = data_dict.get("gender")
print(f"ambil nilai menggunakan key 'get' \n{ambil_value_get}")

# menggunakan get tetapi key tidak ditemukan
ambil_value_get = data_dict.get("agama") # none
print(f"key tidak ada \n{ambil_value_get}")

ambil_value_get = data_dict.get("agama","key tidak ditemukan") # key tidak ditemukan
print(f"key tidak ada tapi dengan pesan \n{ambil_value_get}")

## mengupdate data
data_dict["nama"] = "dudung"
print(f"mengupdate dict biasa \n {data_dict}")

data_dict.update({"kelas":"ST28"})
print(f"mengupdate dict dengan update() \n {data_dict}")

data_dict.update({"Univ":"IPB"})
print(f"menambahkan key dengan update() \n {data_dict}")

## menghapus key dan value
del data_dict["Univ"]
print(f"data dict terbaru \n {data_dict}")