import os
import random

escolhas = {0 : 'PEDRA',
            1 : 'PAPEL',
            2 : 'TESOURA'}
Você = 0
Computador = 0

while True:
    os.system('cls')
    print('============================')
    print('Bem vindo ao jogo de Pedra, Papel e Tesoura')
    print('============================')
    print('')
    print('PLACAR:')
    print('Você: ', Você)
    print('Computador: ', Computador)
    
    lance = int(input('Escolha seu lance: \n0 - Pedra | 1 - Papel | 2 - Tesoura\n'))
    print('============================')
    
    if lance == 0:
        print('Sua jogada: PEDRA')
        lance_computador = random.choice(list(escolhas.values()))
        print('Jogada do computador: ' + lance_computador)
        if lance_computador == 'PEDRA':
            print('EMPATE!')
        elif lance_computador == 'PAPEL':
            print('DERROTA!')
            Computador += 1
        elif lance_computador == 'TESOURA':
            print('VITORIA!')
            Você += 1
        print('============================')    
    elif lance == 1:
        print('Sua jogada: PAPEL')
        lance_computador = random.choice(list(escolhas.values()))
        print('Jogada do computador: ' + lance_computador)
        if lance_computador == 'PEDRA':
            print('VITORIA!')
            Você += 1
        elif lance_computador == 'PAPEL':
            print('EMPATE!')
        elif lance_computador == 'TESOURA':
            print('DERROTA!')
            Computador += 1
        print('============================')
    elif lance == 2:
        print('Sua jogada:  TESOURA')
        lance_computador = random.choice(list(escolhas.values()))
        print('Jogada do computador: ' + lance_computador)
        if lance_computador == 'PEDRA':
            print('DERROTA!')
            Computador += 1
        elif lance_computador == 'PAPEL':
            print('VITORIA!')
            Você += 1
        elif lance_computador == 'TESOURA':
            print('EMPATE!')
        print('============================')
    else:
        print('NUMERO INVALIDO')

    jogar_novamente = int(input('Jogar novamente? 0 - SIM | 1 - NAO\n'))
    if jogar_novamente == 0:
        os.system('cls')
        continue
    else:
        break
