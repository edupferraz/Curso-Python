
cpf = input("Digite um CPF: ")
lista_cpf = []

# Insere os caracteres do cpf em uma lista
for n in cpf:
    lista_cpf += n

# Lista reduzida retirando os dois últimos dígitos
lista_reduzida = lista_cpf[:-2]

contador = 10
soma = 0

# Cálculo para somar termos do CPF
for n in lista_reduzida:
    resultado = int(n) * contador

    soma += resultado
    contador -= 1

digito_1 = 11 - (soma % 11)

if digito_1 > 9:

    digito_1 = 0
    lista_reduzida.append(str(digito_1))

# Parte 02

contador = 11
soma = 0
resultado = 0

# Cálculo para somar termos do CPF
for n in lista_reduzida:

    resultado = int(n) * contador

    # print(f"{n} * {contador} = {resultado}")

    soma += resultado
    contador -= 1

digito_2 = 11 - (soma % 11)

lista_reduzida.append(str(digito_2))

novo_cpf = ""

for n in lista_reduzida:
    novo_cpf += n

if novo_cpf == cpf:
    print("O CPF é válido")
else:
    print("O CPF é inválido")
