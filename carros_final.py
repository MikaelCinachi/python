import os
import time

opcao = 0

carros = {0 : {'nome' : 'Chevrolet Tracker', 'preco' : 120},
          1 : {'nome' : 'Chevrolet Onix', 'preco' : 90},
          2 : {'nome' : 'Chevrolet Spin', 'preco' : 150},
          3 : {'nome' : 'Hyundai HB20', 'preco' : 85},
          4 : {'nome' : 'Hyundai Tucson', 'preco' : 120},
          5 : {'nome' : 'Fiat Uno', 'preco' : 60},
          6 : {'nome' : 'Fiat Mobi', 'preco' : 70},
          7 : {'nome' : 'Fiat Pulse', 'preco' : 130}}
alugados = {}

def portifolio():
    for cod_carro, carro_info in carros.items():
        print('[{}] {}  - R$ {} /dia'.format(cod_carro, carro_info['nome'], carro_info['preco']))


def alugar():
    print('[ ALUGAR ] de uma olhada em nosso portifolio.')
    print('')
    portifolio()
    print('===================')
    cod_carro = int(input('Escolha o codigo do carro: '))
    if cod_carro in carros:
        dias = int(input('Escolha por quantos dias deseja alugar: '))
        carro_info = carros.pop(cod_carro)  
        preco_total = carro_info['preco'] * dias
        os.system('cls')
        print('Vc escolheu {} por {} dias.'.format(carro_info['nome'], dias))
        print('O aluguel totalizaria R$ {}. Deseja alugar?'.format(preco_total))
        conf = int(input('0 - SIM | 1 - NAO '))
        if conf == 0:
            print('Parabens! vc alugou o {} por {} dias.'.format(carro_info['nome'], dias))
            alugados[cod_carro] = {'nome' : carro_info['nome'], 'preco' : carro_info['preco'], 'dias' : dias}

def devolver():
    if len(alugados) == 0:
        print('Sem carros para devolver')
    else:
        print('Segue a lista de carros alugados. Qual vc deseja devolver? ')
        for cod_carro, carro_info in alugados.items():
            print('[{}] {}  - R$ {} /dia'.format(cod_carro, carro_info['nome'], carro_info['preco']))
        print('')
        devolucao = int(input('Escolha o codigo do carro que deseja devolver: '))
        if devolucao in alugados:
            conf = int(input('Tem certeza que deseja devolver esse carro? 0 - SIM | 1 - NAO'))
            if conf == 0:
                print('Obrigado por devolver o carro {}'.format(carro_info['nome']))
                carro_devolvido = alugados.pop(devolucao)
                carros[devolucao] = {'nome' : carro_devolvido['nome'], 'preco' : carro_devolvido['preco']}
                carro_sorted = dict(sorted(carros.items()))
                carros.clear()
                carros.update(carro_sorted)
        else:
            print('Codigo invalido')           
            

def main():
    while True:
        os.system('cls')
        print('===============================')
        print('Bem-vindo a locadora de carros!')
        print('===============================')
        print('O que deseja fazer?')
        op = int(input('0 - Mostrar portifolio | 1 - Alugar um carro | 2 - Devolver um carro '))
        os.system('cls')
        if op == 0:
            portifolio()
        elif op == 1:
            alugar()
        elif op == 2:
            devolver()

        print('')
        print('===============================')
        print('0 - para CONTINUAR | 1 - para SAIR')

        if float    (input()) == 1:
            break   

if opcao == 0:
    main()