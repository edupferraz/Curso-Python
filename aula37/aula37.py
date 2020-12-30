"""
Funções (def) em Python - *args **kwargs
"""

def func(*args, **kwargs):
    # args = list(args)
    # args[0] = 20
    # print(args)
    # print(len(args))

    # idade = kwargs['idade'] # Causa erro caso não tenha
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
func(*lista, *lista_2, idade=17)

#lista = [1,2,3,4,5]
#print(*lista, sep='=')
