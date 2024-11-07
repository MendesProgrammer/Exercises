# Importa biblioteca
from time import sleep
import os
import requests
from bs4 import BeautifulSoup
import json

# Nome do arquivo
arquivo = 'ler.json'

# Tenta abrir um arquivo ou então cria um
try:
    with open(arquivo, 'r') as file:
        dado = json.loads(file.read())
except:
    dado = {'tempo':0.12, 'site':[]}
    with open(arquivo, 'w') as file:
        file.write(json.dumps(dado))

# Laço de repetição
while True:
    # Mostra um menu
    print(' [1 - Cadastrar site                 ]')
    print(' [2 - Ler site                       ]')
    print(' [3 - Apagar site                    ]')
    print(' [4 - Alterar o tempo de visualização]')
    print(' [5 - Sair                           ]')

    # Recebe um código do usuário
    op = str(input('Digite um código: ')).strip()

    # Se op for igual a 1, cadastre um site
    if op == '1':
        nome = str(input('Digite o nome do site: ')).strip()
        conf = str(input('Confirmar? (s/n) ')).strip()
        if conf.lower() == 's':
            dado['site'].append([nome, 0])
            print('Confirmado')
            with open(arquivo, 'w') as file:
                file.write(json.dumps(dado))

    # Se op for igual a 2, ler conteúdo
    elif op == '2':
        if len(dado['site']) > 0: 
            num = 0
            while True:

                print(f'Site número {num}: {dado['site'][num]}')
                sel = str(input('Selecione um comando < ok > sair')).strip()

                if sel == '>':
                    if num + 1 == len(dado['site']):
                        num = 0
                    else:
                        num += 1

                elif sel == '<':
                    if num - 1 < 0:
                        num = len(dado['site']) - 1
                    else:
                        num -= 1

                elif sel.lower() == 'ok':
                    conf = str(input('Entrar, Confirmar? (s/n) ')).strip()
                    if conf.lower() == 's':
                        link = dado[num][0]

                        req = requests.get(link)

                        print(req)

                        site = BeautifulSoup(req.text, 'html.parser')

                        tex = site.find('div', class_='mw-content-ltr mw-parser-output')
                        titulo = site.get_text().split()

                        print('Número de palavras: ', len(titulo))
                        sleep(1.5)

                        inicio = dado['site'][num][1]

                        os.system('cls') or None
                        for c in range(inicio, len(titulo)):
                            print(f'{titulo[c]:^30}')
                            sleep(0.12)
                            os.system('cls') or None
                            dado['site'][num][1] = c
                            with open(arquivo, 'w') as file:
                                file.write(json.dumps(dado))

                        dado['site'][num][1] = 0
                        with open(arquivo, 'w') as file:
                            file.write(json.dumps(dado))

                elif sel.lower() == 'sair':
                    break

            
    # Se op for igual a 3, apage algum site
    elif op == '3':
        if len(dado['site']) > 0:
            num = 0
            while True:
                print(f'Site número {num}: {dado['site'][num]}')
                sel = str(input('Selecione um comando < ok > sair')).strip()

                if sel == '>':
                    if num + 1 == len(dado):
                        num = 0
                    else:
                        num += 1

                elif sel == '<':
                    if num - 1 < 0:
                        num = len(dado) - 1
                    else:
                        num -= 1

                elif sel.lower() == 'ok':
                    conf = str(input('Apagar, Confirmar? (s/n) ')).strip()
                    if conf.lower() == 's':
                        del dado['site'][num]
                        with open(arquivo, 'w') as file:
                            file.write(json.dumps(dado))
                        num -= 1
                        break

                elif sel.lower() == 'sair':
                    break
            
        else:
            print('Não há sites cadastrados')

    elif op == '4':
        while True:
            conf = str(input(f'Tempo atual {dado['tempo']}, modificar? (s/n) ')).strip()
            if conf.lower() == 's':
                while True:
                    temp = float(input('Digite o tempo: '))
                    if temp > 0:
                        while True:
                            conf = str(input('Confirmar? (s/n) ')).strip()
                            if conf.lower() == 's':
                                dado['tempo'] = temp
                                with open(arquivo, 'w') as file:
                                    file.write(json.dumps(dado))
                                print('Confirmado')
                                break
                            elif conf.lower() == 'n':
                                print('Retornando ao menu')
                                break
                            else:
                                print('Erro, digite apenas S ou N')
                        break
                    else:
                        print('Não é permitido valores negativos')
                break
            elif conf.lower() == 'n':
                print('Retornando ao menu principal')
                break
            else:
                print('Erro, digite apenas ou S ou N')


    # Finaliza o programa
    elif op == '5':
        break

    # Se a opção for inválida
    else:
        print('Não existe esta opção')