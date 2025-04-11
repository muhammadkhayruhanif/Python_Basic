# list --> array, dipanggil menggunakan index
data_list = ['ini','adalah','list']
print(f"data list\n{data_list}")

# dictionary (dict) --> associative array
# identifier --> key

# dictionary = {'key':'value'}
"""
dictionary = {
    "key":"value
}
"""

data_dict = {
    'nama':'Hanif',
    'kelas':28,
    'list1':[1,3,5,7],
    'list2':data_list,
    'dict':{'gender':'laki-laki'}
}

print(data_dict)
print(data_dict['nama'])
print(data_dict['kelas'])
print(data_dict['list1'])
print(data_dict['list2'])
print(data_dict['dict'])