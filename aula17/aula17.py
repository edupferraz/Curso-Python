"""
Formatando valores com modificadores

:s - Texto
:d - Inteiros
:f - Float
:.(Número)f - Quantidade de casas decimais
:(Caractere)(> ou < ou ^)(Qantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^- Centro
"""

"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print( '{:.2f}'.format(divisao))


num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')
"""

# ljust, rjust,

nome = "Eduardo Ferraz"
nome_formatado = '{:@>15}'.format(nome)
print(nome_formatado)
