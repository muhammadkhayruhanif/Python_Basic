import datetime

waktu_sekarang = datetime.datetime.now()
print(f"waktu saat ini = {waktu_sekarang}")
print(f"tahun sekarang = {waktu_sekarang.year}")

from collections import Counter

data_acak = ["a","b","b","c","a","c","a","b","b"]

# hitung biasa
count = 0
for i in data_acak:
    if i == "b":
        count += 1
print(f"jumlah 'b' dengan looping = {count}")

# dengan Counter
data_counter = Counter(data_acak)
print(f"jumlah 'a' dengan Counter = {data_counter["a"]}")

# library dapat dilihat dengan "go to references"