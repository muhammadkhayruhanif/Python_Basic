# kalkulator sederhana

# angka1, operator (+, -, x atau *, /), angka2, hasil

angka1 = float(input("masukkan angka ke-1 :"))
operator = input("masukkan operator (+,-,x,/) :")
angka2 = float(input("masukkan angka ke-2 :"))

if operator == "+" :
    hasil = angka1 + angka2
    print("hasil :", hasil)

elif operator == "-" :
    hasil = angka1 - angka2
    print("hasil :", hasil)

elif operator == "x" or operator == "*" :
    hasil = angka1 * angka2
    print("hasil :", hasil)

elif operator == "/" :
    hasil = angka1 / angka2
    print("hasil :", hasil)

else :
    print("langkah-langkah anda salah!")