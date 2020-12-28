"""
While em Python
Utilizado para realizar ações enquanto uma condição for verdadeira.
"""

"""
while True:
    nome = input("Qual o seu nome? ")
    print(nome)


x = 0
while x < 10:
    if x == 3:
        x = x + 1
        # break
        continue

    print(x)
    x = x + 1

print("Acabou!")

x = 0
y = 0

while x < 10:
    y = 0

    while y < 5:
        print(f"({x}, {y})")
        y += 1

    x += 1
"""

while True:
    print()

    sair = input("Deseja sair? [s]im ou [n]ão: ")

    if sair == "s":
        break

    num_1 = input("Digite um número: ")
    num_2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")


    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Digite um número válido!")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)
    else:
        print("Digite um operador válido")
