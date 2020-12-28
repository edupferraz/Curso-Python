"""
For / Else em Python
"""

variavel = ["Eduardo", "Gabriela", "Diego"]

comeca_com_e = False

for valor in variavel:
    if valor.lower().startswith("e"):
        print("Existe uma palavra que começa com J.")
        break
else:
    print("Não existe uma palavra que começa com J.")