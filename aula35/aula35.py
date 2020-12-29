"""
Funções (def) em Python - return - (Parte 02)


def funcao(var):
    print("Isso não será executado.")
    return var

variavel = funcao("Valor que eu quero")

if variavel:
    print(variavel)
else:
    print("Nenhum valor.")


def divisao(n1, n2):

    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,3)

if divide:
    print(divide)
else:
    print("Conta inválida.")
"""

def dumb():
    return [1,2,3,4,5]

var = dumb()

print(var, type(var))