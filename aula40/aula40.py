"""
def func(arg, arg2):

    return arg * arg2

var = func(2, 2)

print(var)

a = lambda x, y: x * y

print(a(2,2))
"""

lista = [
    ["P1", 13],
    ["P2", 7],
    ["P3", 50],
    ["P4", 8],
    ["P5", 6],
]

# lista.sort(key=lambda item: item[1])
# print(lista)

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)
