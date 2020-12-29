"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome


def saudacao(msg, nome):

    return f"{msg} {nome}, como você está?"

mensagem = saudacao("Olá", "Eduardo")

print(mensagem)
"""

"""
    2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.


def soma(num_1, num_2, num_3):

    return f"O resultado da soma é {num_1 + num_2 + num_3}"

soma = soma(2, 3, 4)

print(soma)
"""

"""
    3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual.
    Retorne o valor do primeiro número somado do aumento do percentual do mesmo.


def aumento_percentual(valor, percentual):

    valor += valor * (percentual / 100)

    return valor

valor_final = aumento_percentual(90, 10)

print(valor_final)
"""

"""
    4 - Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz,
    se o parâmetro da função for divisível por 5, retorne buzz. 
    Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado
"""
def fizzBuzz(num):


    if(num % 2 == 0):
        return "Fizz"
    elif(num % 5 == 0 and num % 3 != 0):
        return "Buzz"
    elif(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    else:
        return num

fizzBuzz = fizzBuzz(13)

print(fizzBuzz)