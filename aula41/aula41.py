
t1 = (1, 2, 3, 'a')
t2 = 4, 5, 6, 'b'
t3 = 1,

# print(t1[3])

# for v in t1:
    # print(v)

# print(t1 + t2)

n1, n2, *n = t1

print(n1)

# Processo para mudar valor de uma tupla
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)
