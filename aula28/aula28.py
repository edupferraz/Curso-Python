"""
Operador ternátio em Python


logged_user = True


if logged_user:
    msg = "Usuário Logado."
else:
    msg = "Usuário precisa logar."


msg = "Usuario logado." if logged_user else "Usuário precisa logar."

print(msg)
"""

idade = input("Qual a sua idade? ")

if not idade.isdigit():
    print("Você precisa digitar apenas números")
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = "Pode acessar" if e_de_maior else "Não pode acessar."

    print(msg)