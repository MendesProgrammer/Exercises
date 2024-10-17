# Algoritmo que armazena frases do usuário, e caso queira, um sorteio destas frases e realizado
import json
from time import sleep
from random import choice

def digito(msg='', tempo=0.05):
    for d in msg:
        print(f'{d}', flush=True, end='')
        sleep(tempo)
    print('')


try:
    with open('arquivo.json', 'r') as file:
        dado = json.loads(file.read())
except:
    dado = []
    with open('arquivo.json', 'w') as file:
        file.write(json.dumps(dado))

sel = ''
while sel != 'n':
    print('-' * 50)
    sel = str(input('Deseja adicionar uma frase ou sortear? (a, s, n) ')).strip().lower()
    print('-' * 50)

    if sel == 'a':
        frase = str(input('Digite a frase: ')).strip()
        dado.append(frase)
        with open('arquivo.json', 'w') as file:
            file.write(json.dumps(dado))

    elif sel == 's':
        item = choice(dado)
        digito('Frase do dia...')
        sleep(2)
        digito(item)
        sleep(2)

    elif sel == 'n':
        digito('Finalizando!')

    else:
        digito('Opção inválida!')
