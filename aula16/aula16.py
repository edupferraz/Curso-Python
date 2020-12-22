"""
    Desafio 01 - Número par/ímpar


numero_inteiro = input("Digite um número inteiro: ")

if numero_inteiro.isdigit():

    numero_inteiro = int(numero_inteiro)

    e_par = (numero_inteiro % 2 == 0)

    if e_par:
        print("O número escolhido é par")
    else:
        print("O número escolhido é ímpar")

else:
    print("O número é inválido!")
"""

"""
    Desafio 02 - Saudação de acordo com a hora do dia


hora = input("Digite a hora atual: ")

if hora.isdigit():

    hora = int(hora)

    if hora >= 0 and hora <= 23:
        if hora >= 0 and hora < 11:
            print("Bom dia!")
        elif hora >= 11 and hora < 18:
            print("Boa tarde!")
        elif hora >= 18 and hora < 23:
            print("Boa noite")
    else:
        print("Hora inválida")

else:
    print("Hora inválida!")
    
"""

"""
    Desafio 03 - Identificador de largura de nome
"""

nome = input("Digite seu nome: ")

largura_nome = len(nome)

print(f"O seu nome tem {largura_nome} letras!")

if largura_nome > 0 and largura_nome <= 4:
    print("Seu nome é curto")
elif largura_nome >= 5 and largura_nome <= 6:
    print("Seu nome é normal")
elif largura_nome > 6:
    print("Seu nome é muito grande")
