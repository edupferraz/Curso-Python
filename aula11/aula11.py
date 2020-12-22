"""
Operadores Relacionais
== > >= < <= !=
"""

"""
num_1 = input("Digite o primeiro número: ")
num_2 = input("Digite o segundo número: ")

expressao = (num_1 == num_2)
expressao = (num_1 > num_2)
expressao = (num_1 >= num_2)
expressao = (num_1 < num_2)
expressao = (num_1 <= num_2)
expressao = (num_1 != num_2)

if expressao:
    print("Verdadeira!")
else:
    print("Falsa!")
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

idade = int(idade)

#Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar o empréstimo.")
else:
    print(f"{nome} não pode pegar o empréstimo")