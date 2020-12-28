"""
Desempacotamento de listas em Python
"""

lista = ["Eduardo", "Gabriela", "Diego", 1, 1, 1, 1, 1, 5]

n1, n2, *_, ultimo_da_lista = lista

print(*_)
