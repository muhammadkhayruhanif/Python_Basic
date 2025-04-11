# latihan perulangan membuat segitiga

# menggunakan for

angka = 10
count = 1

for i in range(angka) :
    print("*"*count)
    count += 1

print("segitiga dengan while")

# menggunakan while

count = 1
i = 0

while i < 5 :
    print("*"*count)
    i += 1
    count += 1

print("segitiga dengan while 2")

count = 1

while True :
    print("*"*count)
    count += 1

    if count > angka :
        break

# hanya segitiga ganjil
print("segitiga hanya ganjil")
count = 1
while True :
    if count %2 :
        print("*"*count)
        count += 1

    else :
        count += 1
        continue

    if count > angka :
        break

# segitiga sama kaki

count = 1
angka2 = angka // 2
print("segitiga sama kaki")

while True :
    if count %2 :
        print(" "*angka2, "*"*count)
        count += 1
        angka2 -= 1

    else :
        count += 1
        continue

    if count > angka :
        break

while True :
    if count %2 :
        angka2 += 1
        print(" "*angka2, "*"*count)
        count -= 1

    else :
        count -= 1
        continue

    if count < 0 :
        break