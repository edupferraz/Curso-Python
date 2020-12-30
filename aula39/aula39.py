"""
1 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada


def funcao1(funcao):

    return funcao

def funcao2():
    return ("Teste")

executar = funcao1(funcao2())

print(executar)
"""

"""
2 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada. 
Faca a funcao1 executar duas funcoes que recebem um numero diferente de argumentos.
"""

def funcao1(funcao, *args, **kwargs):
    return funcao(*args, *kwargs)

def funcao2(nome):
    return f"Oi {nome}"

def funcao3(nome, saudacao):
    return f"{saudacao} {nome}"

executando = funcao1(funcao2, "Edu")
executando2 = funcao1(funcao3, "Edu", saudacao="Bom dia!")

print(executando2)