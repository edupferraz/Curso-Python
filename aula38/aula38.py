"""
variavel = "valor"

def func():
    print(variavel)

def func2(arg=None):
    # global variavel
    variavel = "Outro valor"
    print(variavel)

func()
func2()

print(variavel)
"""

var = "valor"

def func():
    # print(var) # Erro pois está sendo chamado antes da criação
    var = 1234
    print(var)

func()