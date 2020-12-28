"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range


lista = ["A", "B", "C", "D", "E"]

print(lista[1], lista[-1])
print(lista[::-1])
print(lista[:2])
print(lista[::4])
print(lista[2:])


# extend - extender lista
# append - adicionar elemento a lista
# insert - inserir elemento em determinado índice

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)
l1.append("4")
l2.insert(0, "Banana")
l2.pop()

print(l1)
print(l2)


# del - excluir parte da lista
# max - valor máximo
# min - valor mínimo

l2 = [1,2,3,4,5,6,7,8,9]

del(l2[3:5])

print(l2)

print(max(l2))
print(min(l2))


l2 = list(range(1,10))

soma = 0

for valor in l2:
    print(valor)

for valor in l2:
    soma += valor
    print(soma)


l2 = ["String", True, 10, -20.5]

for elem in l2:
    print(f"O tipo de elemento é {type(elem)} e seu valor é {elem}")
"""

secreto = "perfume"

digitadas = []

chances = 3

while True:

    if chances == 0:
        print("Você Perdeu!!!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ahhhh isso não vale, digite apenas uma letra!")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"UHUULLL, a letra '{letra}' existe na palavra secreta!")
    else:
        print(f"AFFF, a letra '{letra}' não existe na palavra secreta.")

        chances -= 1

        print(f"Você ainda tem {chances} chances")

        digitadas.pop()

    secreto_temporario = ""

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"Que legal, Você Ganhou!!! A palavra era '{secreto_temporario}'")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")
        print()
