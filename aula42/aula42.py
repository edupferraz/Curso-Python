'''
d1 = {'chave1':'valor da chave'}
d2 = dict(chave1='Valor da Chave', chave2='Valor da outra chave')


print(d1, d2)

d1 = {
    'str': 'valor',
    123: 'outro_valor',
    (1,2,3,4): 'tupla',
}

d1['nomedachave'] = 'Agora existe.'

if d1.get('nomedachave') is not None:
    print(d1.get['nomedachave'])


d1 = {}

d1.update({'nova_chave':'criacao chave'})
d1.update({'outra chave':'chave'})

print(d1)

print('criacao chave' in d1.values())

print(len(d1))

for k, v in d1.items():
    print(k, v)

del d1['nova_chave']



clientes = {
    'cliente1': {
        'nome' : 'Eduardo',
        'sobrenome': 'Ferraz',
    },

    'cliente2': {
        'nome' : 'Diego',
        'sobrenome': 'Costa',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')

    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


d1 = {1: 'a', 2: 'b', 3: 'c'}

v = d1

# v[1] = 'Eduardo'

print(d1)
print(v)

print(v == d1)

v = d1.copy()
v[1] = "Eduardo"

print(d1)
print(v)

print(v == d1)


lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)
'''

d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    'a':'b',
}

d1.pop(4)
d1.popitem()

d1.update(d2)

print(d1)