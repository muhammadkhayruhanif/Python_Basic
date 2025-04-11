"""
1. celcius, titik beku = 0 titik didih = 100
2. fahrenheit, titik beku = 32 titik didih = 212
3. reamur, titik beku = 0 titik didih = 80
4. kelvin, titik beku 273 titik didih = 373
"""

print("====pilih skala hasil====")
print("celcius")
print("fahrenheit")
print("reamur")
print("kelvin")

hasil = input("masukkan skala hasil :")
celcius = "celcius"
fahrenheit = "fahrenheit"
reamur = "reamur"
kelvin = "kelvin"

if(hasil == celcius):
    # mencari suhu celcius
    print("====pilih skala pengukuran====")
    print("1 = fahrenheit")
    print("2 = reamur")
    print("3 = kelvin")

    suhu = int(input("masukkan jenis suhu :"))

    if(suhu == 1):
        skala = int(input("masukkan suhu :"))
        celcius = (5 * (skala - 32))/9
        print("celcius :", celcius)

    elif(suhu == 2):
        skala = int(input("masukkan suhu :"))
        celcius = 5 * skala / 4
        print("celcius :", celcius)

    elif(suhu == 3):
        skala = int(input("masukkan suhu :"))
        celcius = skala - 273
        print("celcius :", celcius)

    else :
        print("tidak ada hasil")

elif(hasil == fahrenheit):
    # mencari suhu fahrenheit
    print("====pilih skala pengukuran====")
    print("1 = celcius")
    print("2 = reamur")
    print("3 = kelvin")

    suhu = int(input("masukkan jenis suhu :"))

    if(suhu == 1):
        skala = int(input("masukkan suhu :"))
        fahrenheit = (9 * skala /5) + 32
        print("fahrenheit :", fahrenheit)

    elif(suhu == 2):
        skala = int(input("masukkan suhu :"))
        fahrenheit = (9 * skala / 4) + 32
        print("fahrenheit :", fahrenheit)

    elif(suhu == 3):
        skala = int(input("masukkan suhu :"))
        fahrenheit = (skala - 273) * (9/5) + 32
        print("fahrenheit :", fahrenheit)

    else :
        print("tidak ada hasil")
else:
    print("belum dibuat oy")