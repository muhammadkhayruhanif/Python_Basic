# index  0(-3)  1(-2)   2(-1)
data = ["ayam","bakso","sate"]
print(f"data awal ={data}")

# melihat info jumlah data
jumlah_data = len(data)
print(f"jumlah data = {jumlah_data}")

# melihat index data
index_0 = data[0]
print(f"data index ke-0 = {index_0}")

index_akhir = data[-1] 
print(f"data index ke-(-1) = {index_akhir}")

## manipulasi data

# memasukkan data
data.insert(1,"bubur") # data.insert(posisi,item)
print(f"data dimasukkan \n{data}")

# memasukkan data paling terakhir di list
data.append("mie")
print(f"data dimasukkan akhir \n{data}")

# gabungkan list dengan list
data_baru = ["teh","kopi","jus"]
data.extend(data_baru)
print(f"data digabungkan dengan list \n{data}")

# merubah item list
data[1] = "timbel"
print(f"merubah item list \n{data}")

# menghapus data
data.remove("bakso")
# data.remove("Bakso") akan error karena penulisan harus sesuai
print(f"menghapus data \n{data}")

# menghapus data terakhir
data.pop()
print(f"menghapus data terakhir \n{data}")

data_terakhir = data.pop() # hanya bisa pada pop dan tidak dengan remove
print(f"data terakhir = {data_terakhir}")