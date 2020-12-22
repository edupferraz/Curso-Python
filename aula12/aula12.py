"""
Operadores Lógicos
and, or, not
in e not in
"""

"""
a = 2
b = 2
c = 3

print(a == b and b > c)

print(a == b or b < c)

print(not (a == b))
"""

"""
nome = "Eduardo"

if 'u' in nome:
    print("Existe a letra U no seu nome.")

if 'e' not in nome:
    print("Não existe o texto")
"""

usuario = input("Nome de usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "Eduardo"
senha_bd = "12345"

if usuario_bd == usuario and senha_bd == senha:
    print("Você está logado no sistema")
else:
    print("Usuário ou senha inválidos!")
