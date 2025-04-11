# latihan memasukkan data buku

list_buku = []
while True :
    data_buku = input("\nmasukkan nama buku\t:")
    data_author = input("masukkan nama penulis\t:")
    print("\n")

    nested_buku = [data_buku,data_author]
    list_buku.append(nested_buku)

    for index,buku in enumerate(list_buku) :
        print(f"{index+1} | {buku[0]}\t| {buku[1]}")

    lanjut = input("\napakah list dilanjutkan? (y/n) :")
    if lanjut == "n" :
        break