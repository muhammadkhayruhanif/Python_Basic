a = ["bakso","semur","soto","sate","konro"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# adress a dan b sama
print(f"adress a = {hex(id(a))}") # perlu pakai hex agar tidak string  
print(f"adress b = {hex(id(b))}")

b[0] = "pecel"
print(f"a = {a}")
print(f"b = {b}") # akan sama karena masih satu adress

# mengcopy list agar tidak ikut berubah
c = a.copy()
print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")
print(f"adress c = {hex(id(c))}")

c[0] = "rujak"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")