# Importa biblioteca
from time import sleep
import os
import requests
from bs4 import BeautifulSoup
import json
import PyPDF2

# Nome do arquivo
arquivo = 'ler.json'


# Tenta abrir um arquivo ou então cria um
try:
    with open(arquivo, 'r') as file:
        dado = json.loads(file.read())
except:
    dado = {'tempo':0.12, 'site':[], 'pdf':[]}
    with open(arquivo, 'w') as file:
        file.write(json.dumps(dado))

# Laço de repetição
while True:
    # Mostra um menu
    print(' [1 - Cadastrar site]')
    print(' [2 - Cadastrar pdf ]')
    print(' [3 - Ler site      ]')
    print(' [4 - Ler pdf       ]')
    print(' [5 - Apagar site   ]')
    print(' [6 - Apagar pdf    ]')
    print(' [7 - Mudar tempo   ]')
    print(' [8 - Sair          ]')

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

    # Se op for igual a 2, cadastre um site
    if op == '2':
        nome = str(input('Digite o caminho do PDF: ')).strip()
        conf = str(input('Confirmar? (s/n) ')).strip()
        if conf.lower() == 's':
            dado['pdf'].append([nome, 0, 0])
            print('Confirmado')
            with open(arquivo, 'w') as file:
                file.write(json.dumps(dado))

    # Se op for igual a 3, ler conteúdo site
    elif op == '3':
        if len(dado['site']) > 0: 
            num = 0
            while True:

                print(f'Site número {num}: {dado["site"][num][0]}')
                sel = str(input('Selecione um comando (< ok > sair) ')).strip()

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
                        link = dado['site'][num][0]

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

    # Se op for igual a 4, ler conteúdo pdf
    elif op == '4':
        if len(dado['pdf']) > 0: 
            num = 0
            while True:

                print(f'PDF número {num}: {dado["pdf"][num][0]}')
                sel = str(input('Selecione um comando (< ok > sair) ')).strip()

                if sel == '>':
                    if num + 1 == len(dado['pdf']):
                        num = 0
                    else:
                        num += 1

                elif sel == '<':
                    if num - 1 < 0:
                        num = len(dado['pdf']) - 1
                    else:
                        num -= 1

                elif sel.lower() == 'ok':
                    conf = str(input('Entrar, Confirmar? (s/n) ')).strip()
                    if conf.lower() == 's':
                        link = dado['pdf'][num][0]
                        
                        pd = open(link, 'rb')
                        pdf = PyPDF2.PdfReader(pd)

                        # Verifica o total de páginas
                        vale = len(pdf.pages)
                        print('Número de palavras: ', vale)

                        ini = dado['pdf'][num][2]

                        for c in range(ini, vale):
                            # Obter a primeira página
                            pag = pdf.pages[1]
                            texto = pag.extract_text().split()

                            try:
                                os.system('cls') or None
                            except:
                                os.system('clear') or None

                            inicio = dado['pdf'][num][1]

                            for c in range(inicio, len(texto)):
                                print(f'{texto[c]:^30}')
                                sleep(0.12)
                                try:
                                    os.system('cls') or None
                                except:
                                    os.system('clear') or None
                                dado['pdf'][num][1] = c
                                with open(arquivo, 'w') as file:
                                    file.write(json.dumps(dado))

                            dado['pdf'][2] = c

                            dado['pdf'][num][1] = 0
                            with open(arquivo, 'w') as file:
                                file.write(json.dumps(dado))

                elif sel.lower() == 'sair':
                    break
            
    # Se op for igual a 5, apage algum site
    elif op == '5':
        if len(dado) > 0:
            num = 0
            while True:
                print(f'Site número {num}: {dado[num]}')
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
                        del dado[num]
                        with open(arquivo, 'w') as file:
                            file.write(json.dumps(dado))
                        num -= 1
                        break

                elif sel.lower() == 'sair':
                    break
            
        else:
            print('Não há sites cadastrados')

     # Se op for igual a 5, apage algum site
    
    # Se op for igual a 6, apage algum pdf
    elif op == '6':
        if len(dado['pdf']) > 0:
            num = 0
            while True:
                print(f'Site número {num}: {dado["pdf"][num]}')
                sel = str(input('Selecione um comando < ok > sair')).strip()

                if sel == '>':
                    if num + 1 == len(dado['pdf']):
                        num = 0
                    else:
                        num += 1

                elif sel == '<':
                    if num - 1 < 0:
                        num = len(dado['pdf']) - 1
                    else:
                        num -= 1

                elif sel.lower() == 'ok':
                    conf = str(input('Apagar, Confirmar? (s/n) ')).strip()
                    if conf.lower() == 's':
                        del dado['pdf'][num]
                        with open(arquivo, 'w') as file:
                            file.write(json.dumps(dado))
                        num -= 1
                        break

                elif sel.lower() == 'sair':
                    break
            
        else:
            print('Não há PDFs cadastrados')

    # Se op for igual a 7, mude o tempo
    elif op == '7':
        while True:
            conf = str(input(f'Tempo atual {dado["tempo"]}, modificar? (s/n) ')).strip()
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
    elif op == '8':
        break

    # Se a opção for inválida
    else:
        print('Não existe esta opção')
