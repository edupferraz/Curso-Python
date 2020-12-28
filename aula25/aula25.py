"""
Spli, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list


# strip - remover espaço no início e fim da string
# capitalize - primeira letra maiúscula
string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

palavra = ""
contagem = 0
for valor in lista_1:
    # print( f"A palavra {valor} apareceu {lista_1.count(valor)}")
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra} ({contagem}x)")


string = "O Brasil é penta."
lista = string.split(" ")
string2 = "  ".join(lista)

print(string)
print(lista)
print(string2)


string = "O Brasil é penta."
lista = string.split(" ")

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])


lista = [
    [0,"Eduardo"],
    [1,"Gabriela"],
    [2,"Diego"]
]

for indice, nome in lista:
    print(indice, nome)
"""

lista = ["Eduardo", "Gabriela", "Diego"]

n1, n2, n3 = lista

print(n2)