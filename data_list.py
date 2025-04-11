# list

# kumpulan data numbers
data_numbers = [1,2,5,7]
print(data_numbers)

# kumpulan data string
data_string = ["aku","belajar","list"]
print(data_string)

# kumpulan data boolean
data_boolean = [True,False,True,True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,2,"angka",True,"kata",3,False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,12,2) # range(start,stop,step)
print(data_range)

data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_for = [i for i in range(0,10)]
print(list_for)

# list hasil kuadrat
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuat list dengan for dan if
list_for_if = [i for i in range(0,10) if i%5 != 0]
print(list_for_if)