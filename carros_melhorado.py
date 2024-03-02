import os

carros = [
          ('Chevrolet Tracker', 120), 
          ('Chevrolet Onix', 90), 
          ('Chevrolet Spin', 150), 
          ('Hyundai HB20', 85), 
          ('Hyundai Tucson', 120), 
          ('Fiat Uno', 60), 
          ('Fiat Mobi', 70), 
          ('Fiat Pulse', 130)
          ]
alugados = []


def portifolio(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] {} - R$ {} /dia.'.format(i, car[0], car[1]))
portifolio(carros)

while True:
    os.system('cls')
    print('===============================')
    print('Bem-vindo a locadora de carros!')
    print('===============================')
    print('O que deseja fazer?')
    op = int(input('0 - Mostrar portifolio | 1 - Alugar um carro | 2 - Devolver um carro '))

    os.system('cls')
    if op == 0:
        portifolio(carros)

    elif op == 1:
        print('[ ALUGAR ] De uma olhada em nosso portifolio.')
        print('===============================')
        portifolio(carros)
        codigo_carro = int(input('Escolha o codigo do carro: '))
        dias = int(input('Por quantos dias deseja alugar esse carro? '))
        os.system('cls')
        
        print('Vc escolheu {} por {} dias'.format(carros[codigo_carro][0], dias))
        print('O aluguel totalizaria R$ {}. Deseja alugar?'.format(dias * carros[codigo_carro][1]))
        
        confirmacao = int(input('0 - SIM | 1 - NAO '))
        if confirmacao == 0:
            print('Parabens! Vc alugou o {} por {} dias.'.format(carros[codigo_carro][0], dias))
            alugados.append(carros.pop(codigo_carro))



    elif op == 2:
        if len(alugados) == 0:
            print('Nao tem carros para devolver.')
        else:
            print('Segue a lista de carros alugados. Qual vc deseja devolver?')
            portifolio(alugados)
            print('')
            devolver = int(input('Escolha o codigo do carro que deseja devolver: '))
            confirmacao = int(input('Tem certeza que deseja devolver esse carro? 0 - SIM | 1 - NAO '))
            if confirmacao == 0:
                print('Obrigado por devolver o carro {}'.format(alugados[devolver][0]))
                carros.append(alugados.pop(devolver))

    print('')
    print('===============================')
    print('0 - para CONTINUAR | 1 - para SAIR')

    if float    (input()) == 1:
        break   