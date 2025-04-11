# NOT, OR, AND, XOR

# NOT (ingkaran)
"""
 p  NOT p
 1    0
 0    1     
"""
p = True
not_p = not p
print(not_p)

# OR (disjungsi) --> dijumlahkan 1+0=1
"""
p  q  p OR q
1  1    1
1  0    1
0  1    1
0  0    0
"""
p = True
q = False
p_or_q = p or q
print(p_or_q)

# AND (konjungsi) --> dikalikan 0*0=0
"""
p  q  p AND q
1  1     1
1  0     0
0  1     0
0  0     0
"""
p_and_q = p and q
print(p_and_q)

# XOR (disjungsi eksklusif)
"""
p  q  p XOR q
1  1     0
1  0     1
0  1     1
0  0     0
"""
p_xor_q = p ^ q
print(p_xor_q)