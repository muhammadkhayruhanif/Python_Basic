# date and time (latihan)

import datetime as dt

hari_ini = dt.date.today() # mengecek tanggal saat ini
print(hari_ini)

# mencari umur
print("MASUKKAN TANGGAL LAHIR")
tanggal = int(input("tanggal :"))
bulan = int(input("bulan   :"))
tahun = int(input("tahun   :"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir      : {tanggal_lahir}")
print(f"hari lahir         : {tanggal_lahir:%A}") # melihat hari pada tanggal

print("================================")
print(f"tanggal saat ini   : {hari_ini}")
print(f"hari ini adalah    : {hari_ini:%A}")

print("================================")
jumlah_hari = hari_ini - tanggal_lahir
umur_tahun = jumlah_hari.days // 365
umur_bulan = (jumlah_hari.days % 365) // 30
print(f"saat ini sudah     : {umur_tahun} tahun {umur_bulan} bulan")