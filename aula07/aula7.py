
nome = "Eduardo"
idade = 17
altura = 1.83
peso = 62
e_maior = idade > 18
imc = peso / (altura * altura)

print(nome, 'tem', idade, 'anos e seu índice de massa corponal é', imc)
print(f'{nome} tem {idade} anos e seu índice de massa corporal é {imc:.2f}')
print('{0} tem {1} anos e seu índice de massa corporal é {2}'.format(nome, idade, imc))