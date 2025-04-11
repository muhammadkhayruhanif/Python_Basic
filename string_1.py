# cara membuat string

buat_string = "ini adalah string" # string --> kumpulan karakter, spasi juga string
print(buat_string)

"""
1. string menggunakan single quote '...'
2. string menggunakan double quote "..."
"""

# single quote
data = 'menggunakan single quote'
print(data)

# double quote
data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"') # disatukan ("" --> menjadi string)

print("hari ini adalah hari Jum'at") # terdapat tanda kutip --> gunakan kutip dua

# mengunakan tanda \ --> membuat ' jadi string
print('hari ini adalah hari Jum\'at') # menghilangkan fungsi kutip
print('isn\'t won\'t you come')

# backslash
print("C:\\user\\Hanif") # tidak bisa print C:\user\Hanif --> gunakan backslash \

# tab \t
print("benda1\tbenda2") # memberikan tab --> menjauhkan

# backspace \b
print("benda1 \bbenda2") # menghapus spasi --> mendekatkan

# newline \n --> memberikan enter
print("baris pertama\nbaris kedua") # LF --> line feed --> unix, linux, macos
print("baris pertama\rbaris kedua") # CR --> carriage return --> commodore, acorn, lisp
print("baris pertama\r\nbaris kedua") # CRLF --> line feed carriage return --> windows

# string literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder') # r sebagai raw, apabila banyak \n, \r, \t, dsb --> guankan raw
print(r'\r\n\t\b\a')

# multiline literal string
print("""
nama : Hanif
Kelas : ST 28
Semester : 1
kegiatan : ngoding
""")

# multiline literal string dan RAW
print(r"""
website : www.https:\n\web\r
data : C:\raw\new
""")