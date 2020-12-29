"""
Funções - def em Python (Parte 01)
"""

def funcao_01():
    print("Hello World!")

funcao_01()

def saudacao(msg = "Olá", nome = "Usuário") :
    nome = nome.replace("E", '3')
    return f'{msg}, {nome}'

variavel = saudacao()

print(variavel)



