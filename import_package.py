import sains.matematika
from sains import fisika
from sains.fisika import kelajuan as laju

import time # melihat seberapa cepat program dijalankan

t_start = time.time()
hasil_kurang = sains.matematika.kurang(10,8,6,4)
print(f"hasil pengurangan = {hasil_kurang}")

## melihat waktu eksekusi program
t_end = time.time()
print(f"waktu yang dibutuhkan = {t_end - t_start} sekon")

# fugsi dari package fisika
kelajuan_benda = laju(100,10) # s: 100 meter, t: 10 sekon
print(f"kelajuan benda = {kelajuan_benda} m/s")

"""
__pycache__ merupakan penyimpanan bytecode atau code yang lebih mendekati bahasa mesin
sehingga program yang dijalankan lebih cepat, apabila dihapus maka pada proses run selanjutnya
akan dibuat kembali secara otomatis
"""