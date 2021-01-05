"""
Iniciar com letra, pode conter números, separar _, letras minúsuclas
"""

nome = "Eduardo"
idade = 17
altura = 1.83
peso = 62
e_maior = idade > 18
imc = peso / (altura * altura)

"""
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("É maior: ", e_maior)
"""

# Desafio
print(nome, 'tem', idade, 'de idade e seu índice de massa corponal é', int(imc))
