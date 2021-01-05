
perguntas = {
    'Pergunta 1':{
        'pergunta':'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta':'Quanto é 3 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
    'Pergunta 3':{
        'pergunta':'Quanto é 8 / 2?',
        'respostas': {'a': '3', 'b': '4', 'c': '9',},
        'resposta_certa': 'b',
    },
    'Pergunta 4':{
        'pergunta':'Quanto é 2 ^ 3 ?',
        'respostas': {'a': '8', 'b': '4', 'c': '16',},
        'resposta_certa': 'a',
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
         print(f'[{rk}: {rv}]')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!!!')
        respostas_certas += 1
    else:
        print("Você errou!!!")

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} de {qtd_perguntas}.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')