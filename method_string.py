# operasi string dalam bentuk method

## merubah case dari string

# merubah semua string ke upper case
salam1 = "assalamualaikum"
string_upper = salam1.upper()
print("upper dari 'assalamualaikum' = " + str(string_upper)) # concatenate

# merubah semua string ke lower case
salam2 = "WAALAIKUMSALAM"
string_lower = salam2.lower()
print("lower dari " + salam2 + " = " + str(string_lower))

## pengecekan dengan isX method

# contoh pengecekan lower case
apakah_lower = salam1.islower()
print(salam1 + " apakah lower case = " + str(apakah_lower)) # hasilnya booleane

# contoh pengecekan upper case
apakah_upper = salam2.isupper()
print(salam2 + " apakah upper case = " + str(apakah_upper))

salam3 = "Insya Allah"
apakah_upper = salam3.isupper()
print(salam3 + " apakah upper case = " + str(apakah_upper))

"""
1. isalpha()   --> mengecek huruf saja
2. isalnum()   --> mengecek huruf dan angka
3. isdecimal() --> mengecek angka saja 
4. isspace()   --> mengecek spasi, tab, newline \n
5. istitle()   --> mengecek kata awal sebagai huruf besar
"""

judul = "Ada apa Dengan Cinta" # 'apa' tidak huruf besar
cek_judul = judul.istitle()
print(judul + " istitle = " + str(cek_judul)) # harus dirubah ke string

## ngecek komponen dengan startswith() dan endswith()

# startswith()
mulai = "semua dimulai dari konsisten"
mulai_method = "semua dimulai dari konsisten".startswith("semua") #l langsung dari literals
print("'" + mulai + "'" + " dimulai oleh 'semua' = " + str(mulai_method)) 

# endswith()
akhir = mulai.endswith("dari")
print("'" + mulai + "'" + " diakhiri oleh 'dari' = " + str(akhir)) # harusnya 'konsisten'

## penggabungan komponen join() split()

# join()
pisah = ['aku', 'sedang', 'belajar', 'ngoding']
gabung = " ".join(pisah) # ingat!
print(gabung)

# split()
gabung = "aku sedang belajar ngoding"
print(gabung.split(" ")) # akan dirubah ke list

# alokasi karakter rjust() ljust() center()

print(4*"="+"PEMISAH"+"="*4) # biasanya begini

# rjust() --> right justify
kanan = "RIGHT"
print("'" + kanan.rjust(10) + "'") # akan menjadi di kanan 10 string termasuk kata2

# ljust() --> left justify
kiri = "LEFT"
print("'" + kiri.ljust(10) + "'") # akan menjadi di kiri 10 string termasuk kata2

#center()
tengah = "CENTER"
print("'" + tengah.center(10) + "'") # akan menjadi di tengah 10 string termasuk kata2

pemisah = tengah.center(14,'=') # menambahkan karakter pada spasinya
print(pemisah)

# kebalikannya --> split()
pemisah = tengah.split('=')
print(pemisah)

text = "ada apa dengan cinta"
jadi_judul = text.capitalize()
print(jadi_judul)