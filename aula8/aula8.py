# Desafio Prático

# Criar variáveis para nome, idade , altura e peso de uma pessoa

nome = "Eduardo"
idade = 17
altura = 1.83
peso = 62

# Criar variável com o ano atual

ano_atual = 2020

# Obter o ano de nascimento da pessoa

ano_nascimento = ano_atual - idade

# Obter o IMC da pessoa com 2 casas decimais

imc = (peso / (altura * altura))

# Exibir um textp com todos os valores na tela usando F-Strings (chaves)

print(f"{nome}, tem {idade}, {altura} e pesa {peso}kg")
print(f"O IMC de {nome} é {imc:.2f}")
print(f"{nome} nasceu em {ano_nascimento}")