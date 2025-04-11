# width and multiline

nama = "Muhammad Khayruhanif"
umur = 18
tinggi_badan = 166.3
ukuran_sepatu = 42
kesibukan = "ngoding"

# string standard
biodata = f"nama = {nama}, umur = {umur}, tinggi = {tinggi_badan}, sepatu = {ukuran_sepatu}, aktivitas = {kesibukan}"
print("STRING STANDAR")
print(biodata)

# string multiline  (dengan menggunakan enter, newline \n)
biodata = f"nama = {nama} \numur = {umur} \ntinggi = {tinggi_badan} \nsepatu = {ukuran_sepatu} \naktivitas = {kesibukan}"
print("\nSTRING MULTILINE (ENTER)")
print(biodata)


# string multiline (kutip triplets)
biodata = f"""nama = {nama}
umur = {umur}
tinggi = {tinggi_badan}
sepatu = {ukuran_sepatu}
aktivitas = {kesibukan}"""
print("\nSTRING MULTILINE (KUTIP)")
print(biodata)

# mengatur lebar
biodata = f"""nama      = {nama:20}
umur      = {umur:>20} 
tinggi    = {tinggi_badan:>20}
sepatu    = {ukuran_sepatu:20}
aktivitas = {kesibukan:>20}""" # atur jarak "=" secara manual
print("\nMENGATUR LEBAR") # atur jadi rata kanan dengan string = 20 termasuk kata2
print(biodata)